import boto3

client = boto3.client('s3')
response = client.get_bucket_acl(
    Bucket='surbhi-boto3',
)

for grant in response['Grants']:
    grantee = grant['Grantee']['DisplayName']
    permission = grant['Permission']
    print(f"Grant to '{grantee}' with permission '{permission}'")


