# Serverless Data Engineering Pipeline

This project aims to create a serverless data engineering pipeline that can process and analyze large amounts of data using Natural Language Processing (NLP) and/or Applied Computer Vision techniques. The pipeline will be built using serverless technologies to ensure scalability and cost-effectiveness. In this project, we will attempt to reproduce the architecture of an existing serverless data engineering project or develop a similar solution.

## Features

Serverless architecture for scalability and cost optimization
NLP analysis with entity extraction and key phrase extraction
Optional Applied Computer Vision functionality
Easy deployment and maintenance
## Technologies

AWS Lambda
AWS Step Functions
AWS S3
AWS Glue
Amazon Comprehend
Amazon Rekognition (Optional for Applied Computer Vision)
## Three-Week Plan

Week 1: Research and Planning
Research existing serverless data engineering projects and their architecture
Decide on the project to reproduce or create a custom solution
Define the requirements and functional specifications
Create an initial project plan and timeline
Week 2: Implementation
Set up the serverless infrastructure using AWS services
Implement data ingestion and processing using AWS Lambda and Step Functions
Create data storage and processing solutions with AWS S3 and Glue
Implement NLP analysis with Amazon Comprehend for entity extraction and key phrase extraction
(Optional) Implement Applied Computer Vision using Amazon Rekognition
Week 3: Testing and Deployment
Test the serverless data engineering pipeline thoroughly, ensuring data processing and analysis functionality
Optimize the pipeline for cost and performance
Document the project, including architecture, setup, and usage instructions
Deploy the final solution to the production environment
Handover the project to the client or end-users
## Requirements

To use this serverless data engineering pipeline, you will need the following:

An AWS account with appropriate permissions to create and manage AWS resources
Basic knowledge of AWS services, such as Lambda, Step Functions, S3, Glue, Comprehend, and Rekognition (if using Applied Computer Vision)
Familiarity with NLP techniques, such as entity extraction and key phrase extraction
(Optional) Knowledge of Applied Computer Vision techniques if implementing that feature
Getting Started

Clone the repository or download the project files
Follow the setup instructions provided in the documentation
Deploy the serverless data engineering pipeline to your AWS account
Start processing and analyzing your data using the pipeline
Support and Contribution

If you encounter any issues or have suggestions for improvements, please open an issue in the GitHub repository. Contributions are also welcome via pull requests.


## Usage
1. Set up an S3 bucket to store raw data and processed data: ```aws s3api create-bucket --bucket my-serverless-data-pipeline-bucket --region us-west-2```

2. Create an AWS Glue Crawler to infer the schema of your raw data and store it in the AWS Glue Data Catalog: ```aws glue create-crawler --name my-data-crawler --role MyGlueServiceRole --database-name my-data-db --targets S3Targets=[{Path=s3://my-serverless-data-pipeline-bucket/raw-data/}] --region us-west-2```

3. Deploy to AWS ```aws lambda create-function --function-name my-data-processing-function --runtime python3.9 --role MyLambdaServiceRole --handler lambda_function.lambda_handler --zip-file fileb://lambda_function.zip --environment Variables={S3_BUCKET=my-serverless-data-pipeline-bucket} --region us-west-2```

4. Set up an event notification ``` aws s3api put-bucket-notification-configuration --bucket my-serverless-data-pipeline-bucket --notification-configuration file://notification_configuration.json```

## License

This project is licensed under the MIT License.
## References

* [rust-cli-template](https://github.com/kbknapp/rust-cli-template)
