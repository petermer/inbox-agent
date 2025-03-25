from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL

def get_gpt_llm():
    return ChatOpenAI(
        temperature=0.3,
        openai_api_key=OPENAI_API_KEY,
        model_name=OPENAI_MODEL
    )