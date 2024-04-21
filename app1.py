from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
prompt_template=PromptTemplate.from_template(
    "Explain {topic} like I am {number} years old."
)
llm=Ollama(model="mistral")
chain=prompt_template|llm
print(
    chain.invoke({
        "topic":"what is generative AI",
        "number":"five"}))
