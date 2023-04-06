import boto3
import os
import json
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

s3 = boto3.client("s3")
comprehend = boto3.client("comprehend")
rekognition = boto3.client("rekognition")

BUCKET = os.environ["S3_BUCKET"]
RAW_DATA_PREFIX = "raw-data/"
PROCESSED_DATA_PREFIX = "processed-data/"

def lambda_handler(event, context):
    for record in event["Records"]:
        # Get the S3 object key
        key = record["s3"]["object"]["key"]

        # Load the raw data
        response = s3.get_object(Bucket=BUCKET, Key=key)
        raw_data = json.loads(response["Body"].read())

        # Process the data using NLP and/or Computer Vision
        processed_data = process_data(raw_data)

        # Save the processed data to S3
        s3.put_object(Bucket=BUCKET, Key=PROCESSED_DATA_PREFIX + key, Body=json.dumps(processed_data))

def process_data(raw_data):
    # Implement your NLP and/or Computer Vision processing logic here
    # For example, using Amazon Comprehend and Rekognition:

    text = raw_data["text"]
    sentiment_response = comprehend.detect_sentiment(Text=text, LanguageCode="en")
    sentiment = sentiment_response["Sentiment"]

    if "image_url" in raw_data:
        image_url = raw_data["image_url"]
        image_labels = detect_labels(image_url)
    else:
        image_labels = []

    return {
        "text": text,
        "sentiment": sentiment,
        "image_labels": image_labels
    }

def detect_labels(image_url):
    response = requests.get(image_url)
    image_bytes = bytearray(response.content)

    rekognition_response = rekognition.detect_labels(Image={"Bytes": image_bytes})
    labels = [label["Name"] for label in rekognition_response["Labels"]]

    return labels
