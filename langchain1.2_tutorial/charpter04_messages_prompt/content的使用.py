
# 将图片转换成 Base64编码的 Data URI字符串
# import base64
# def encode_image(img_path, img_type='jpeg'):
#     """将一张本地图片转换成 Base64编码的 Data URI字符串，方便在文本中嵌入图片数据"""
#     with open(img_path,"rb") as img_file:
#         return f"data:image/{img_type};base64, {base64.b64encode(img_file.read()).decode("utf-8")}"
#
# #图像路径
# img_path = "image_test.png'
# #获取图像base64编码字符串
# base64_image = encode_image(img_path)
# response = model.invoke(
#     [  HumanMessage(
#         content=[
#             {'type':"text","text":"这张图里有什么?"},
#             {
#                 'type':'image_url',
#                 "image_url":base64_image,
#             }
#         ]
#     )
# ]
# )
# print(response.content)
# print(response.content)


#content blocks使用

import os
import base64
from langchain.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv(override=True)
#2.初始化模型                 #deepseek模型不支持图片输入，会报错
model = init_chat_model(  #初始化模型     创建大模型对话对象model，后续调用.invoke()就能发消息提问
    model="deepseek-v4-pro",  #模型名称
    model_provider="openai",  #模型提供者    DeepSeek 兼容 OpenAI 请求格式，填这个代表走 OpenAI 通用协议
    api_key=os.getenv("DEEPSEEK_API_KEY"),  #API密钥     读取环境变量，找不到会返回None，不会直接程序崩溃
    base_url=os.getenv("DEEPSEEK_BASE_URL")  #基础接口地址
)

def encode_image(img_path, img_type='jpeg'):
    """将一张本地图片转换成 Base64编码的 Data URI字符串，方便在文本中嵌入图片数据"""
    with open(img_path,"rb") as img_file:
        return f"data:image/{img_type};base64, {base64.b64encode(img_file.read()).decode('utf-8')}"


#图像路径
img_path = "image_test.png"
#获取图像base64编码字符串
base64_image = encode_image(img_path)
response = model.invoke(
    [HumanMessage(content="你好，请简单介绍一下你自己")]
)
print(response.content)

# 图片输入示例（需要换用支持视觉的模型如 GPT-4o 才能运行）
# response = model.invoke(
#     [
#         HumanMessage(
#             content_blocks=[
#             {'type':'text','text':"这张图里有什么?"},
#             {
#                 'type':'image',  #LangChain 会自动将其转换为 OpenAI 格式的 image_url 字段发送给 API，但 DeepSeek 不认识这个格式，所以返回了 400 错误。
#                 'base64': base64_image,
#                 'mime_type':'image/png',
#             }
#             ]
#         )
#     ]
# )
# print(response.content)



















