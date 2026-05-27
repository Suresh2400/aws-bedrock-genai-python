import boto3
import json

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

prompt = "Write leave request email"

body = json.dumps({
    "prompt": prompt,
    "max_gen_len": 512,
    "temperature": 0.5,
    "top_p": 0.9
})

response = bedrock.invoke_model(
    modelId="meta.llama3-8b-instruct-v1:0",
    body=body,
    contentType="application/json",
    accept="application/json"
)

response_body = json.loads(response["body"].read())

print(response_body)