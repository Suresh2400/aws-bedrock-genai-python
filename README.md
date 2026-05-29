# AWS Bedrock Generative AI Project

This project demonstrates the implementation of Generative AI applications using AWS Bedrock foundation models with Python and LangChain.

## Project Description

The application integrates AWS Bedrock services to interact with multiple AI foundation models for text generation, embeddings, and Retrieval-Augmented Generation (RAG) workflows.

The project was implemented as part of hands-on practice with AWS Bedrock services, model invocation, vector embeddings, and LLM integrations.

## Implemented Features

* AWS Bedrock service integration
* Multiple foundation model invocation
* Amazon Titan embedding model integration
* Claude model response generation
* llama model response generation
*titan model response generation

## AI Models Used

* Amazon Titan Text Models
* Amazon Titan Embedding Models
* Claude Foundation Models

## Technologies Used

* Python
* AWS Bedrock
* LangChain
* Boto3
* Streamlit
* FAISS
* PyPDF

## Workflow

1. Load and process PDF documents
2. Split content into text chunks
3. Generate embeddings using Bedrock models
4. Store vectors in FAISS vector database
5. Retrieve relevant context based on user queries
6. Send retrieved context to foundation models
7. Generate intelligent AI responses

## Learning Outcome

This project helped in understanding:

* Foundation model integration
* Prompt engineering
* AWS Bedrock model invocation
* End-to-end Generative AI workflows

## Future Improvements

* Multi-document support
* Conversational memory
