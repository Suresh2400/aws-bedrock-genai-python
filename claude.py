import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 200,
    "messages": [
        {
            "role": "user",
            "content": "Hello Claude"
        }
    ]
})

response = client.invoke_model(
    modelId="anthropic.claude-3-7-sonnet-20250219-v1:0",
    body=body,
    contentType="application/json",
    accept="application/json"
)

response_body = json.loads(response["body"].read())

print(response_body["content"][0]["text"])