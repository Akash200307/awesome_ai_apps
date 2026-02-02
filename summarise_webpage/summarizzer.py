from bs4 import BeautifulSoup
import requests
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
class website:
    url:str
    title:str
    text:str
    def __init__(self,url) -> None:
        self.url=url
        response=requests.get(url=url)

        soup=BeautifulSoup(response.content,'html.parser')
        self.title=str(soup.title.string) if soup.title else "No title found"
        if soup.body:
         for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
            self.text=soup.body.get_text(separator="\n",strip=True)

def user_prompt(website):
   user_prompt=f"This is website title:{website.title}"
   user_prompt+=f"Generate a short summary alligned with the contents of the website\
   as below \n\n{website.text}"
   return HumanMessage(user_prompt)

def create_ai():
   agent=create_agent(
      model=ChatGroq(model="moonshotai/kimi-k2-instruct"),
      system_prompt="You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown"
   )
   return agent

def summarize(url):
   web=website(url)
   message=user_prompt(web)
   agent=create_ai()

   return agent.invoke({
      "messages":[message]
   })
       
res=summarize("https://edwarddonner.com")

print(res["messages"][-1].content)