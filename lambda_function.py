{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1205cd19-d47e-40f9-890b-cc9c04bbd934",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import requests\n",
    "import boto3\n",
    "import os\n",
    "import logging\n",
    "\n",
    "logger = logging.getLogger()\n",
    "logger.setLevel(logging.INFO)\n",
    "\n",
    "s3 = boto3.client('s3')\n",
    "bucket_name = \"asp-project-jayasree\"\n",
    "\n",
    "def lambda_handler(event, context):\n",
    "    #zillow api url\n",
    "    url = \"https://zillow56.p.rapidapi.com/search\"\n",
    "\n",
    "    api_key = os.environ.get('Zillow_api_key')\n",
    "    if not api_key:\n",
    "        return{\n",
    "            'statusCode' : 400,\n",
    "            'body' : 'API Key not found in environment variables.'\n",
    "        }\n",
    "    \n",
    "    headers = {\n",
    "        \"x-rapidapi-host\": \"zillow.p.rapidapi.com\",\n",
    "        \"x-rapidapi-key\": api_key\n",
    "    }\n",
    "\n",
    "    location = os.environ.get('location')\n",
    "    querystring = {\"location\":location,\"output\":\"json\",\"status\":\"forSale\",\"sortSelection\":\"priorityscore\",\"listing_type\":\"by_agent\",\"doz\":\"any\"}\n",
    "\n",
    "    try:\n",
    "        response = requests.get(url, headers=headers, params=querystring)\n",
    "        if response.status_code != 200:\n",
    "            return {\n",
    "                'statusCode': response.status_code,\n",
    "                'body': f\"API request failed with status code {response.status_code}\"\n",
    "            }\n",
    "\n",
    "        # Parsing the API response\n",
    "        data = response.json()\n",
    "        \n",
    "        # Save data to S3 bucket \n",
    "        s3.put_object(Bucket=bucket_name, Key='data.json', Body=json.dumps(data))\n",
    "\n",
    "        return {\n",
    "            'statusCode': 200,\n",
    "            'body': json.dumps('Data ingestion completed successfully')\n",
    "        }\n",
    "    except requests.exceptions.RequestException as e:\n",
    "        logger.error(\"Error occurred during API request: %s\", str(e))\n",
    "        return {\n",
    "            'statusCode': 500,\n",
    "            'body': 'An error occurred while making the API request.'\n",
    "        }"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
