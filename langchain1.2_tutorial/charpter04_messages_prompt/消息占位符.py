#消息占位符
"""
当你不确定消息提示模板使用什么角色，或者希望在格式化过程中插入消息列表时该怎么办?
这就需要使用消息占位符，负责在特定位置添加消息列表。
使用场景:多轮对话系统存储历史消息以及Agent的中间步骤处理此功能非常有用。
"""
# 使用占位符placeholder

from langchain_core.prompts import ChatPromptTemplate

# template = ChatPromptTemplate.from_messages([
#      ("system","我是一个AI助手"),
#      ("placeholder","{conversation}")#消息占位符    不只是存一条消息
# ])
# # 调用模板
# result = template.invoke({
#     "conversation":[   #conversation是占位符的名称，用于存储消息列表   整个消息列表还回去
#         # ("human","你好，请问明天的天气如何?"),
#         # ("ai","明天天气晴朗"),
#         ("human","后天的天气怎么样?"),
#         ("ai","后天天气晴朗")
#      ]
# })
# print(result)

# 2.2使用MessagesPlaceholder
# MessagesPlaceholder 是一个特殊的消息占位符，用于在模板中插入消息列表。
# 它的语法是 {name}，其中 name 是占位符的名称。
# from langchain_core.prompts import MessagesPlaceholder
# template = ChatPromptTemplate.from_messages([(
#     "system","我是一个AI助手"),
#     MessagesPlaceholder(variable_name="conversation")
# ])

# result = template.invoke({
#     "conversation": [
#         ("human","你好，请问明天的天气如何?"),
#         ("ai","明天天气晴朗"),
#         ("human","后天的天气怎么样?")
#     ]
# })
#
# print(result)


from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import MessagesPlaceholder

# 创建模板：使用 MessagesPlaceholder 支持插入消息列表
# template = ChatPromptTemplate.from_messages([  #这是 LangChain 中创建对话提示模板的核心方法
#     #1. ChatPromptTemplate
#         # 这是 LangChain 中的一个类
#         # 专门用于构建和管理对话式AI的提示模板
#         # 支持多种消息类型（系统、用户、AI、工具等）
#     # 2. from_messages()
#         # 这是一个类方法（工厂方法）
#         # 作用：从给定的消息列表创建提示模板
#         # 参数：一个包含消息的列表
#     ("system", "我是一个AI助手"),
#     MessagesPlaceholder(variable_name="conversation")#把整个消息列表原样展开插入到提示词的指定位置，非常适合多轮对话中插入历史消息记录。
# ])
#
# result = template.invoke({
# "conversation":[
#     HumanMessage("你好，请问明天的天气如何?"),
#     AIMessage("明天天气晴朗"),
#     HumanMessage("后天的天气怎么样?")
#     ]
# })
# print(result)

# #工厂方法是一种创建对象的方式，它不直接调用类的构造函数（__init__），而是通过类上的一个特殊方法来生成对象。
# # 假设直接创建，需要手动组装内部结构，非常繁琐
# template = ChatPromptTemplate(
#     messages=[SystemMessagePromptTemplate(...), HumanMessagePromptTemplate(...)],
#     input_variables=["conversation"]
# )
# # 只需传入简单的元组列表，工厂方法帮你处理内部复杂的转换逻辑
# template = ChatPromptTemplate.from_messages([
#     ("system", "我是一个AI助手"),
#     MessagesPlaceholder(variable_name="conversation")
# ])
# 工厂方法 = 一个类的静态/类方法，专门负责"制造"该类的实例，目的是隐藏复杂的初始化逻辑，让调用更简洁。

#存储历史消息

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个非常友好的AI助手"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{question}")
])

prompt_template.invoke({
    "history": [
        ("human", "5 + 2 = ?"),
        ("ai","5 +2=7")
    ],
    "question":"结果再乘以4呢?"
})

#templates/
    #_init__.py
    # common.py  #通用模板
    # translation.py  #翻译相关
    # coding.py     #编程相关

#common.py
from langchain_core.prompts import ChatPromptTemplate

FRIENDLY_ASSISTANT = ChatPromptTemplate.from_messages([
    ("system","你是一个友好的助手"),
    ("user","{input}")
])

# 2.4.4 模板组合
# 将多个模板片段组合成复杂的提示词。
# 方法1:字符串组合
#定义可复用的部分
role_part ="你是一个{domain}专家。"
style_part = "回答风格:{style}。"
constraint_part = "限制:{constraint}."

#组合
full_system = role_part + style_part + constraint_part
template = ChatPromptTemplate.from_messages([   #类的方法实例化了一个模板对象
    ("system",full_system),
    ("user","{question}")
])

#方法二：使用+运算符
template1 = ChatPromptTemplate.from_messages([
    ("system","你是助手")
])
template2 = ChatPromptTemplate.from_messages([
    ("user","{input}")
])
#组合(LangChain1.0支持)
combined = template1 + template2


