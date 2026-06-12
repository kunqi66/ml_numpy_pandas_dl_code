from langchain_core.messages import SystemMessage,HumanMessage
import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from my_pkg import my_model

sys_message = SystemMessage(content='你是我得助手')
human_message = HumanMessage(content='如何可以健康减肚子上的肥肉')
message = [sys_message,human_message]
print(message)

response = my_model.llm.invoke(message)

print(response)
