from langchain_community.llms import Ollama
llm=Ollama(model="mistral")
print(llm("Give me meal plan for today"))
