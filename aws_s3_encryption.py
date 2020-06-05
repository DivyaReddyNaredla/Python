import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

response = s3.list_buckets()
#print(response)
new_resp = []

for bucket in response['Buckets']:
  try:
    enc = s3.get_bucket_encryption(Bucket=bucket['Name'])
    rules = enc['ServerSideEncryptionConfiguration']['Rules']
    #print('Bucket: %s, Encryption: %s' % (bucket['Name'], rules))

    
  except ClientError as e:
    if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
      ('Bucket: %s, no server-side encryption' % (bucket['Name']))
      new_resp.append(bucket['Name'])
      
    else:
      print("Bucket: %s, unexpected error: %s" % (bucket['Name'], e))
print("The updated List is:",new_resp)
