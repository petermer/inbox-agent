import os
from dotenv import load_dotenv

load_dotenv()

USE_MODEL = claude  # Options claude, gpt

# AWS Bedrock
BEDROCK_REGION = os.getenv(AWS_DEFAULT_REGION)
BEDROCK_MODEL_ID = anthropic.claude-v2

# OpenAI
OPENAI_API_KEY = os.getenv(OPENAI_API_KEY)
OPENAI_MODEL = gpt-4
