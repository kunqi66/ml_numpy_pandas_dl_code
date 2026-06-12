import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv()

key = os.getenv("DEEPSEEK_API_KEY")
if not key:
    print('读取失败')
else:
# 3. 初始化 ChatDeepSeek 模型
# 这里使用 "deepseek-chat" 模型，它功能完整，支持工具调用和结构化输出[reference:2]
    llm = ChatDeepSeek(
        model="deepseek-v4-pro", # 根据具体模型名称调整
        api_key=key
    )
response = llm.invoke("你好")
# 4. 调用模型并打印回复
print(response.content)

