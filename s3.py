import boto3
s3 = boto3.client('s3',
	aws_access_key_id = '',
	aws_secret_access_key = '',
	region_name = "ap-south-1"
	)
file_path = 'jay.txt'
bucket_name = 'jayanthk'
object_name = 'jay.txt'
try:
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"File '{file_path}' uploaded to '{bucket_name}' as '{object_name}'")
except Exception as e:
    print(f"An error occured : {e}")    
