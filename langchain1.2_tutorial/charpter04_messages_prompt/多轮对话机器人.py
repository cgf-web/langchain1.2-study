from langchain.chat_models import init_chat_model  #导入 LangChain 封装的统一模型初始化函数，兼容 DeepSeek、GPT、通义千问等所有 OpenAI 格式接口
from dotenv import load_dotenv     #导入第三方库函数load_dotenv，自动读取项目里.env文件的密钥、接口地址
import os   #导入系统内置os模块，用来读取环境变量（存 API 密钥）

load_dotenv(override=True)  #加载.env文件，override=True代表文件里的值会覆盖系统已有的同名变量   比如环境变量有设置  冲突时， 优先.env里的配置

def keep_recent_messages(messages,max_pairs=3):
    system_messages = [m for m in messages if m.get("role") == "system"]
    conversation_messages = [m for m in messages if m.get("role") != "system"]
    recent_messages = conversation_messages[-(max_pairs * 2):]
    return system_messages + recent_messages

#1.基础配置
MODEL_NAME = "deepseek-v4-pro"
MAX_PAIRS_HISTORY = 10
EXIT_WORD = "quit"

#2.初始化模型
model = init_chat_model(  #初始化模型     创建大模型对话对象model，后续调用.invoke()就能发消息提问
    model="deepseek-v4-pro",  #模型名称
    model_provider="openai",  #模型提供者    DeepSeek 兼容 OpenAI 请求格式，填这个代表走 OpenAI 通用协议
    api_key=os.getenv("DEEPSEEK_API_KEY"),  #API密钥     读取环境变量，找不到会返回None，不会直接程序崩溃
    base_url=os.getenv("DEEPSEEK_BASE_URL")  #基础接口地址
)

#维护一个消息列表，用来存储对话历史
messages=[
    {
        "role": "system",
        "content": "你是一个温柔可爱的ai助手,叫做小美"
    }
]

i=1   #描述对话轮数
print("\n","欢迎来到ai助手,~##~,",f"输入{EXIT_WORD}退出程序","\n")
while True:

    print(f"第{i}轮对话开始",end="\n")
    user_input=input("请输入问题:")

    #判断是否结束当前会话
    if user_input==EXIT_WORD:
        print("退出程序")
        break

    #将用户信息添加到消息列表中
    messages.append({
        "role": "user",
        "content": user_input
    }
    )
    print("ai助手：",end="",flush=True)#等待模型回复

    #拼接Ai回复的信息消息
    reply_content=""

    #优化历史记忆
    memory_messages=keep_recent_messages(messages,max_pairs=MAX_PAIRS_HISTORY)
    for chunk in model.stream(memory_messages):   #遍历模型生成的每个chunk  流式生成，实时打印
        if chunk.content:
            print(chunk.content,end="",flush=True)#
            reply_content+=chunk.content

    print("\n",f"第{i}轮对话结束!","\n")

    i+=1#轮数加1

    messages.append({   #将Ai回复的信息添加到消息列表中
        "role": "assistant",
        "content": reply_content
    })





