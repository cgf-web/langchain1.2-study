
from langchain_core.prompts import ChatPromptTemplate


#ChatPromptTemplate的实例化

# chat_prompt_template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "你是一个友好的AI助手，你的名字叫{name}"),
#         ("human", "你好，最近怎么样?"),
#         ("ai", "我很好，谢谢"),
#         ("human", "{user_input}")
#     ]
# )
#
# #调用
# result = chat_prompt_template.invoke({"name":"小智","user_input":"2 + 2 = ? "})
# print(result)
# print(type(result))


#ChatPromptTemplate的调用
# chat_prompt_template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "你是一个友好的AI助手，你的名字叫{name}"),
#         ("human", "你好，最近怎么样?"),
#         ("ai", "我很好，谢谢"),
#         ("human", "{user_input}")
#     ]
# )
#
# #调用
# result = chat_prompt_template.invoke({"name":"小智","user_input":"2 + 2 = ? "})
# print(result)
# print(type(result))


#format()方法
# 参数类型:变量值     返回值类型：字符串
# chat_prompt_template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "你是一个友好的AI助手，你的名字叫{name}"),
#         ("human", "你好，最近怎么样?"),
#         ("ai", "我很好，谢谢"),
#         ("human", "{user_input}")
#     ]
# )
#
# #调用
# result = chat_prompt_template.format(name="小智",user_input="2 + 2 = ? ")
# print(result)
# print(type(result))


#format_messages()方法
#传入参数：变量值    #返回值：消息列表
# chat_prompt_template = ChatPromptTemplate.from_messages(
#     [
#         ("system", "你是一个友好的AI助手，你的名字叫{name}"),
#         ("human", "你好，最近怎么样?"),
#         ("ai", "我很好，谢谢"),
#         ("human", "{user_input}")
#     ]
# )
#
# #调用
# result = chat_prompt_template.format_messages(name="小智",user_input="2 + 2 = ? ")
# print(result)
# print(type(result))



from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain.chat_models import init_chat_model
######1、提供大模型#######

load_dotenv(override=True)
#
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

model = init_chat_model(  #初始化模型     创建大模型对话对象model，后续调用.invoke()就能发消息提问
    model="deepseek-v4-pro",  #模型名称
    model_provider="openai",  #模型提供者    DeepSeek 兼容 OpenAI 请求格式，填这个代表走 OpenAI 通用协议
    api_key=os.getenv("DEEPSEEK_API_KEY"),  #API密钥     读取环境变量，找不到会返回None，不会直接程序崩溃
    base_url=os.getenv("DEEPSEEK_BASE_URL")  #基础接口地址
)

######2、提供提示词模板#########
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个友好的AI助手，你的名字叫{name}"),
        ("human", "你好，最近怎么样?"),
        ("ai", "我很好，谢谢"),
        ("human","{user_input}")
    ]
)
#调用
prompt_value = chat_prompt_template.invoke({"name":"小智","user_input":"2 + 2 = ? "})

######3、模型调用#########
response = model.invoke(prompt_value) #invoke能识别
print(response)
