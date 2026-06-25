import os
from langchain调用本地模型.chat_models import init_chat_model

from dotenv import load_dotenv
#加载配置文件
load_dotenv(override=True)
CLOSEAI_API_KEY = os.getenv("CLOSEAI_API_KEY")
CLOSEAI_BASE_URL = os.getenv("CLOSEAI_BASE_URL")
#获取大模型
model = init_chat_model(
    model="openai:gpt-5.4-mini",temperature=0,
    api_key=CLOSEAI_API_KEY,
    base_url=CLOSEAI_BASE_URL,
)
for i in range(3):
    print(model.invoke("帮我写一首关于春天的七言绝句").content)



 #temperature  控制输出随机性，范围0.0-2.0，温度越高输出越随机。

# 2、Token是什么?
# 基本单位:大模型通过分词器(Tokenizer)将文本拆分后的最小语义单元是token(相当于自然语言中的词或字)。
# 不同的模型采用不同的分词算法(如BPE、WordPiece)，因此同一段文本在不同模型中的Token数量可能不同。
# 收费依据:大语言模型通常也是以token的数量作为其计量(或收费)的依据。

# 1个中文Token≈1-1.8个汉字，1个英文Token≈3-4个字符
# Token与字符转化的可视化工具:
# OpenAI是供: https://platform.openai.com/tokenizero
# 百度智能云提供:https://console.bce.baidu.com/support/#/tokenizer

