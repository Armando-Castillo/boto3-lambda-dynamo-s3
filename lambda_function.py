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

    #Connections -> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    s3 = boto3.client('s3') #S3 only can be a client
    dynamo = boto3.client('dynamodb', region_name = region) #Could be resource or client (different ops)

    ######CSV EXAMPLE READ DIRECTORIES/FULL BUCKET######
    #Directories don´t exist on S3, but prefix are used
    #Map keys (direction of objects in s3) from a bucket and prefix or directory dir1/dir2/
    for key in s3.list_objects(Bucket = bucket_name, Prefix='dir1/dir2')['Contents']: #Returns directories
        llave = key['Key'] #Other directory
        #Read one csv file
        csv_file = s3.get_object(Bucket = bucket_name, Key = llave)
        #Split rows
        csv_list_items = csv_file['Body'].read().decode('utf-8').split('\n')   
        #Split values by separator or commas
        csv_reader = csv.reader(csv_list_items, delimiter=',', quotechar='*')

    ######JSON EXAMPLE#####

    #For requests execution status APIs
    return{
        'statusCode': 200,
        'body': json.dumps('Migration successful')
    }