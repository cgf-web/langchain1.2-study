from langchain_ollama import ChatOllama

#
# model = ChatOllama(
#     model="qwen2.5:7b",
#     #base_url="http://localhost:11434"
# )
# print(model.invoke("介绍一下你自己"))


from langchain.chat_models import init_chat_model
model = init_chat_model(
    model_provider="ollama",
    model="qwen2.5:7b",
    base_url="http://localhost:11434"
)
print(model.invoke("介绍一下你自己"))