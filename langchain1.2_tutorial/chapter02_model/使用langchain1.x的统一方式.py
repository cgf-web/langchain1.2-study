#使用langchain1.x的统一方式
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 读取.env配置文件中的信息。相关的环境变量以.env文件中的优先
load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

# 模型的初始化
llm_deepseek = init_chat_model(

    # model="deepseek-v4-flash",
    # model_provider="deepseek",
    #或者
    model="deepseek:deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,
)

# 模型的调用
response = llm_deepseek.invoke("请用一句话介绍你自己")
print(response)


#5.小结
# DeepSeek官网的DeepSeek模型:ChatDeepSeek()、 ChatOpenAI()、 init_chat_model()
# 阿里云百炼平台的DeepSeek模型:ChatTongyi()、ChatOpenAI()、 init_chat_model()
# OpenRouter平台的DeepSeek模型:ChatOpenRouter() ChatopenAI()、 init_chat_model()
# CloseAI平台的DeepSeek模型:CharOpenAI()、init_chat_model()