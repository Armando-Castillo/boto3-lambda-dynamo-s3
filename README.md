## Migrate CSV/JSON S3 to Dynamodb

Es un proceso de migración de datos en formato CSV/JSON en S3 a DynamoDB

La generación de archivos en fromato CSV o JSON desde una base de datos relacional se puede realizar con herramientas ETL como Glue en AWS

Para probar desde fuera de lambda environment o cloud9 solo se necesita instalar boto3 `pip install boto3` que es el AWS SDK for Python y maneja recursos como S3, dynamodb, entre otro.