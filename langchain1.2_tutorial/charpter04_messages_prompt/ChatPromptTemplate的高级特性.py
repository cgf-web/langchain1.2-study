#ChatPromptTemplate的高级特性

#1部分变量预填充 partial()
# from langchain_core.prompts import ChatPromptTemplate
#
# template = ChatPromptTemplate.from_messages([
#         ("system","你是{role}，目标用户是{audience}"),#{}占位符
#         ("user", "{task}")
#     ])
# result1 = template.invoke({"role":"导游","audience":"游客","task":"介绍一下北京的故宫"})
# result2 = template.invoke({"role":"导游","audience":"游客","task":"介绍一下北京的顾和园"}) #键值对填充占位符
# print(result1)  # to_string() 将所有消息拼接为字符串
# print(result2)  # to_messages() 返回 BaseMessage 列表


#优化上面代码 partial()方法
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
        ("system","你是{department}的{role}"),#{}占位符
        ("user", "{task}")  #三个占位符
    ])

it_template=template.partial(department="IT部门",role="开发人员")  #先填充两个占位符  #role关键字参数名必须与占位符中的名称完全匹配
sale_template=template.partial(department="销售部",role="销售代表")  #部分变量预填充

result1 = it_template.invoke({"task":"介绍一下Python语言"})
result2 = sale_template.invoke({"task":"介绍一下Python语言"})

print(result1)  # to_string() 将所有消息拼接为字符串
print(result2)

