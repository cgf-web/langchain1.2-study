from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv(override=True)     #从.env文件中加载环境变量
model = init_chat_model(
    model="deepseek-v4-pro",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

#json格式的消息
messages =[
    {"role":"system","content":"你是一个友好的AI助手"},
    {"role":"user","content":"1 + 2 = ?"},
    {"role":"assistant","content":"3"},
    {"role":"user","content":"我刚才问了什么问题?"}
]
response = model.invoke(messages)
print(response)
