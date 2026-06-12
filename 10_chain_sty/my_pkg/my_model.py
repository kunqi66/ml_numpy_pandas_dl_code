import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv()

key = os.getenv("DEEPSEEK_API_KEY")

llm = ChatDeepSeek(
    model="deepseek-v4-flash", # 根据具体模型名称调整
    api_key=key
)