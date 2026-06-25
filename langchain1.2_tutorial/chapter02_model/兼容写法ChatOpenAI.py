import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#1、读取.env配置文件中的信息。相关的环境变量以.env文件中的优先
# load_dotenv(override=True)
#
# DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
#
# #获取大模型
# model = ChatOpenAI(
#     model="deepseek-v4-flash",
#     api_key=DEEPSEEK_API_KEY,
#     base_url=DEEPSEEK_BASE_URL,
# )
#
# print(model.invoke("1+1=?"))


#加载配置文件
load_dotenv(override=True)
CLOSEAI_API_KEY = os.getenv("CLOSEAI_API_KEY")
CLOSEAI_BASE_URL = os.getenv ("CLOSEAI_BASE_URL")

#获取大模型
model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=CLOSEAI_API_KEY,
    base_url=CLOSEAI_BASE_URL,
)
print(model.invoke("一句话介绍下你自己"))