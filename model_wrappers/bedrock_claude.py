from langchain.llms import Bedrock
from config import BEDROCK_REGION, BEDROCK_MODEL_ID

def get_claude_llm():
    return Bedrock(
        region_name=BEDROCK_REGION,
        model_id=BEDROCK_MODEL_ID,
        model_kwargs={"temperature": 0.3}
    )