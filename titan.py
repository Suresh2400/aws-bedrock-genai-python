import boto3
import json

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

inputText= "Explain cloud computing"

body = json.dumps({
      "inputText":inputText,
    "textGenerationConfig": {
        "maxTokenCount": 100,
        "temperature": 0.7
    }
})

response = bedrock.invoke_model(
    modelId="amazon.titan-text-premier-v1:0",
    body=body,
    contentType="application/json",
    accept="application/json"
)

result = json.loads(response["body"].read())

print(result)