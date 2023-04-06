import boto3
import json

s3 = boto3.client("s3")
bucket_name = "my-serverless-data-pipeline-bucket"

raw_data = {
    "text": "This is a sample text for NLP processing.",
    "image_url": "https://example.com/sample-image.jpg"
}

s3.put_object(Bucket=bucket_name, Key="raw-data/sample-data.json", Body=json.dumps(raw_data))