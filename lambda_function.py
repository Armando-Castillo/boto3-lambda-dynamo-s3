#AWS SDK for python
import boto3
#JSON and CSV libraries for format, read and write data
import json
import csv

#Official documentation -> https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
#Official documentation -> https://docs.aws.amazon.com/pythonsdk/

#event -> trigger lambda activation
def lamba_handler(event, context):
    #Configuration variables
    region = 'us-east-1'
    bucket_name = 'bucket_name'
    csv_list_items = [] #For read rows in the csv file

    #Connections
    s3 = boto3.client('s3')

    ######CSV EXAMPLE######


    ######JSON EXAMPLE#####

    #For requests execution status APIs
    return{
        'statusCode': 200,
        'body': json.dumps('Migration successful')
    }