import os

from langchain调用本地模型.chat_models import ChatZhipuAI
from dotenv import load_dotenv
#1、读取.env配置文件中的信息。相关的环境变量以.env文件中的优先

load_dotenv(override=True)
ZHIPUAI_API_KEY = os.getenv ("ZHIPUAI_API_KEY")
ZHPPUAI_BASE_URL = os.getenv("ZHPPUAI_BASE_URL")
#2、模型的初始化
llm_zhipu = ChatZhipuAI(
    model="glm-5.1",
    api_key=ZHIPUAI_API_KEY,
    api_base=ZHPPUAI_BASE_URL,
)
#3、模型的调用
response= llm_zhipu.invoke("请用一句话介绍你自己")
print(response)