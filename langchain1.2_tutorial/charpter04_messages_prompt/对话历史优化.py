from langchain.chat_models import init_chat_model  #导入 LangChain 封装的统一模型初始化函数，兼容 DeepSeek、GPT、通义千问等所有 OpenAI 格式接口
from dotenv import load_dotenv     #导入第三方库函数load_dotenv，自动读取项目里.env文件的密钥、接口地址
import os   #导入系统内置os模块，用来读取环境变量（存 API 密钥）

load_dotenv(override=True)  #加载.env文件，override=True代表文件里的值会覆盖系统已有的同名变量   比如环境变量有设置  冲突时， 优先.env里的配置
model = init_chat_model(  #初始化模型     创建大模型对话对象model，后续调用.invoke()就能发消息提问
    model="deepseek-v4-pro",  #模型名称
    model_provider="openai",  #模型提供者    DeepSeek 兼容 OpenAI 请求格式，填这个代表走 OpenAI 通用协议
    api_key=os.getenv("DEEPSEEK_API_KEY"),  #API密钥     读取环境变量，找不到会返回None，不会直接程序崩溃
    base_url=os.getenv("DEEPSEEK_BASE_URL")  #基础接口地址
)

def keep_recent_messages(messages,max_pairs=3):   #定义函数，保留最近的N轮对话     def 函数名(参数1, 参数2=默认值):
    """"                                          #messages传入完整的对话列表（必传参数）   max_pairs=3：形参默认值，不传参数就默认保留 3 轮对话
    保留最近的N轮对话
    max_pairs: 保留对话的轮数(每轮=user + assistant)
    """

    # 分离system消息和对话消息
    system_messages = [m for m in messages if m.get("role") == "system"]   #作用：把角色为 system的消息单独挑出来，系统提示词必须永远放在对话最前面，不能被删掉。
    # system_messages = []   列表推导式展开
    # for m in messages:
    #     if m.get("role") == "system":
    #         system_messages.append(m)
    # 作用：把角色为system的消息单独挑出来，系统提示词必须永远放在对话最前面，不能被删掉。
    # m.get("role")：字典安全取值语法，如果字典m里没有role键，不会报错，返回None；如果写m["role"]，缺失键会直接程序崩溃。

    conversation_messages = [m for m in messages if m.get("role") != "system"]   #m遍历整个对话  m.get(键)存在时返回值，不存在时返回None
    # conversation_messages=[]
    # for m in messages:
    #     if m.get("role")!="system":
    #         conversation_messages.append(m)
    #把所有的对话消息，除了系统消息，都挑出来
    # 只保留最近的消息对
    #recent_messages = conversation_messages[-(max_pairs * 2):]  #max_pairs=3 最近的3轮对话*2 = 6条消息  既保留最新6条消息
    #recent_messages = conversation_messages[-(max_pairs * 2)::1]   #完整写法
    recent_messages=conversation_messages[-1:-(max_pairs * 2)-1:-1]
    #列表[-n:]：切片语法，取列表最后 n 个元素
    #只取末尾最新的几轮问答，更早的历史全部丢弃，控制上下文长度，防止超长文本消耗 token、卡顿

    # 返回系统消息和最近的消息对
    return system_messages + recent_messages    #两个列表用+拼接，把固定的系统提示词放在最前面，再拼接裁剪后的最新问答，生成全新的对话列表返回。


#初始化
long_conversation = [
    {"role":"system","content":"你是一个 Python 导师"}, #系统消息，给系统设定角色
]
# 整体是列表套字典结构：
# 外层[]：所有对话按顺序存在列表里
# 内层{}：单条消息，固定两个键：role角色、content消息内容
# system角色：全局人设，全程不变，永远在列表第一条


#第1轮
long_conversation.append({"role":"user","content":"什么是列表?用一句解释"}) #用户消息
r1 = model.invoke(long_conversation)
long_conversation.append({"role": "assistant", "content": r1.content})

# 列表.append(元素)：往对话列表末尾追加用户提问字典
# model.invoke(完整对话列表)：把全部历史消息发给大模型，返回模型响应对象
# r1.content：提取模型返回的文本内容，封装成 assistant 消息，再次追加到对话列表
# 第 2、3 轮完全重复这个流程，实现多轮连续对话

#第2轮
long_conversation.append({"role":"user","content":"列表和元组有什么区别?用一句解释"})
r2 = model.invoke(long_conversation)
long_conversation.append({"role": "assistant", "content": r2.content})
#第3轮
long_conversation.append({"role":"user","content":"什么是字典呢?用一句解释"})
r3 = model.invoke(long_conversation)
long_conversation.append({"role": "assistant", "content": r3.content})
print(f"原始消息数:{len(long_conversation)}") #7

#优化:只保留最近2轮
optimized = keep_recent_messages(long_conversation, max_pairs=2)
print(f"优化后消息数:{len(optimized)}")
print(f"保留的内容:system + 最近2轮对话")  #5
# 添加新的用户问题
optimized.append({"role":"user","content":"我第一个问题问的是什么?"}) # 使用优化后的历史
response = model.invoke(optimized)
print(f"\nAI 回复:{response.content}")








