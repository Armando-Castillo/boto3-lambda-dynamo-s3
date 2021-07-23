#AWS SDK for python
import boto3
#JSON and CSV libraries for format, read and write data
import json
import csv
import Decimal #Read on decimal format

#Official documentation -> https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
#Official documentation -> https://docs.aws.amazon.com/pythonsdk/

#event -> trigger lambda activation
def lamba_handler(event, context):
    #Configuration variables
    region = 'us-east-1'
    bucket_name = 'bucket_name'
    csv_list_items = [] #For read rows in the csv file
    table_name = 'TableDynamo'

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
        
        #for loop to take each item of thw row
        for item in csv_reader:
            if item:
                dynamo_item1 = item[0]
                dynamo_item2 = item[1]
                dynamo_item3 = item[2]
                
                try:
                    #conditions for write well on dynamo (cast, etc)
                    add_dynamo_items = dynamo.put_item(
                        TableName = table_name,
                        Item = {
                            'NOMBRECOLDYNAMO1': { 'N': dynamo_item1 }, #format, value
                            'NOMBRECOLDYNAMO2': { 'S': dynamo_item2 },
                            'NOMBRECOLDYNAMO3': { 'S': dynamo_item3 }
                        }
                    )
                except Exception as error:
                    print(error)
                    #maybe other try except for exceptional items/rows
                
    ######JSON EXAMPLE#####
    #For insert JSON file to dynamo we will use dynamo as resource
    dynamodb = boto3.resource('dynamodb')
    with open("file.json") as json_file:
        json_list = json.load(json_file, parse_float=Decimal)
    
    for item in json_list:
        dynamodb.Table(table_name).put_item(Item=item)    


    #In s3 put event -> gets key
    json_event_file = event['Records'][0]['s3']['object']['key']
    json_object = s3.get_object(Bucket = bucket_name, Key = json_event_file)
    #Decode file
    json_file_s3 = json_object['Body'].read()
    json_dict = json.loads(json_file_s3)
    dynamodb.table(table_name).put_item(Item=json_dict)
    
    #For requests execution status APIs
    return{
        'statusCode': 200,
        'body': json.dumps('Migration successful')
    }