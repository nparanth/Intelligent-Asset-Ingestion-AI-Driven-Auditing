import json
import boto3
import os


s3 = boto3.client('s3')
bucket = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
 
    
    # Get filename from the frontend request
    body = json.loads(event.get('body', '{}')) # fallback value after comma is used in case there is not an actual 'body' value
    file_name = body.get('fileName', '{})
    content_type = body.get('contentType', '{}')

    # Generate the pre-signed URL (Valid for 5 minutes)
    url = s3.generate_presigned_url('put_object',
        Params={
            'Bucket': bucket_name,
            'Key': file_name,
            'ContentType': content_type
        },
        ExpiresIn=300
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'uploadUrl': url})
    }
