import os
from http.client import responses
#写法一
if 0:
    from dotenv import load_dotenv
    from langchain_deepseek import ChatDeepSeek


    #读取.env配置文件中的信息。相关的环境变量以.env文件中的优先
    load_dotenv(override=True)

    DEEPSEEK_API_KEY = os.getenv ("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = os.getenv ("DEEPSEEK_BASE_URL")

    #模型的初始化
    llm_deepseek = ChatDeepSeek(
        model="deepseek-v4-flash",
        api_key=DEEPSEEK_API_KEY,
        api_base=DEEPSEEK_BASE_URL,
    )

    #模型的调用
    response=llm_deepseek.invoke("请用一句话介绍你自己")
    print(response)
if 1:
    #写法二
    from langchain_deepseek import ChatDeepSeek

    # 模型的初始化
    llm_deepseek = ChatDeepSeek(
        model="deepseek-v4-flash",
        api_key="sk-01323021c664464b8a4187d9444259f7",
        api_base="https://api.deepseek.com",
    )

    # 模型的调用
    response = llm_deepseek.invoke("请用一句话介绍你自己")
    print(response)
