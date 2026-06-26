#消息占位符
#当你不确定消息提示模板使用什么角色，或者希望在格式化过程中插入消息列表时该怎么办?
# 这就需要使用消息占位符，负责在特定位置添加消息列表。
#使用场景:多轮对话系统存储历史消息以及Agent的中间步骤处理此功能非常有用。
import template
#使用占位符placeholder

from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
     ("system","我是一个AI助手"),
     ("placeholder","{conversation}")#消息占位符    不只是存一条消息
])
# 调用模板
result = template.invoke({
    "conversation":[   #conversation是占位符的名称，用于存储消息列表   整个消息列表还回去
        ("human","你好，请问明天的天气如何?"),
        ("ai","明天天气晴朗"),
        ("human","后天的天气怎么样?"),
        ("ai","后天天气晴朗")
     ]
})
print(result)
