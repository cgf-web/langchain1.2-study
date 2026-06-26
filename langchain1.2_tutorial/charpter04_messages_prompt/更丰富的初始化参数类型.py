from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate


#字符串列表
# ChatPrompt_template=ChatPromptTemplate.from_messages([
#     ("system", "你是一个友好的AI助手，你的名字叫{name}"),
#     ("human", "你好，最近怎么样?"),
#     ("ai", "我很好，谢谢"),
#     ("human", "{user_input}"),
#     ("human","你好，最近怎么样?"),
#     ]
# )

#字典列表
# chat_prompt_template = ChatPromptTemplate.from_messages(
#     [
#         {"role":"system","content":"你是一个友好的AI助手"},
#         {"role":"human","content":"你好，我是{name}"},
#     ]
# )
# chat_prompt_template.invoke({"name":"小明"})


#消息对象列表

# chat_prompt_template = ChatPromptTemplate.from_messages(
#     [
#         SystemMessage(content="你是一个友好的AI助手"),
#         HumanMessage(content="你好，我是{name}")
#     ]
# )
# chat_prompt_template.invoke({"name":"小明"})


#还有好几种方式可以定义ChatPromptTemplate
#综合使用
# 这段代码学习如何使用多种方式创建和组合ChatPromptTemplate
# 关键信息：展示了三种不同的消息类型可以混合使用在同一个ChatPromptTemplate中

from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    )
from langchain_core.messages import SystemMessage, HumanMessage

#示例1:使用 BaseMessage(已实例化的消息)
# 关键信息：直接使用已实例化的消息对象，内容固定，不支持变量替换
system_msg = SystemMessage(content="你是一个AI工程师。")
human_msg = HumanMessage(content="你好! ")

# 示例 2:使用 BaseMessagePromptTemplates
# 关键信息：使用模板化的消息，支持变量替换，可以动态生成内容
system_msg_prompt = SystemMessagePromptTemplate.from_template("你是一个{role}.")
human_msg_prompt = HumanMessagePromptTemplate.from_template("{user_input}")

# 示例 3:使用 BaseChatPromptTemplate (嵌套的 ChatPromptTemplate)
# 关键信息：展示了如何将不同类型的消息对象混合使用
# 包括：MessagePromptTemplate、ChatPromptTemplate和普通消息对象
nested_prompt = ChatPromptTemplate.from_messages([("system","嵌套提示词")])
prompt = ChatPromptTemplate.from_messages([
    system_msg_prompt,  # MessageLike (BaseMessagePromptTemplate)
    human_msg_prompt,   # MessageLike (BaseMessagePromptTemplate)
    nested_prompt,      # MessageLike (ChatPromptTemplate)
    human_msg_prompt,   # MessageLike (BaseMessagePromptTemplate)
    nested_prompt,      # MessageLike (ChatPromptTemplate)
    ]
)

# 关键信息：调用时需要提供模板中定义的所有变量
prompt.invoke({"role":"人工智能专家","user_input":"介绍一下大模型的应用场景"})











