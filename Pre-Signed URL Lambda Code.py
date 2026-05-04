import json
import boto3


s3 = boto3.client('s3')
bucket_name = "example"

def lambda_handler(event, context):
 
    
    # Get filename from the frontend request
    body = json.loads(event.get('body', '{}')) # ramndom value after comma is used in case there is not an actual 'body' value
    file_name = body.get('fileName', 'unknown_asset.stl')
    content_type = body.get('contentType', 'application')

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
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'uploadUrl': url})
    }