
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
load_dotenv()

def fetch_web_contents(url):

    res=requests.get(url)
    soup=BeautifulSoup(res.content,"html.parser")
    if soup.title and soup.title.string:
        title=soup.title.string
    else:
        title="no text"
    if soup.body:
        for noMatch in soup.body(["script","style","img","input"]):
            noMatch.decompose()
        text=soup.body.get_text(separator="\n",strip=True)
    else:
        text=" "
    return (title+"\\n\\n"+text)[:2_000]

def fetch_links(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.content,"html.parser")
    links=[link.get("href") for link in soup.find_all("a")]

    return [link for link in links if link]


def create_ai():
   agent=create_agent(
      model=ChatGroq(model="moonshotai/kimi-k2-instruct"),
      system_prompt = """
You are provided with a list of links found on a webpage.
Identify ALL links relevant for a professional brochure, including:
- About/Bio pages
- Company information
- Services/Products/Curriculum
- Portfolio/Projects
- Blog/News (if substantive)
- Related company websites
You should respond in JSON as in this example:


{
"links": [
{"type": "about page", "url": "https://full.url/goes/here/about"},
{"type": "careers page", "url": "https://another.full.url/careers"}
]
}

Exclude: email links (mailto:), social media, terms of service, privacy policies.
Return ALL relevant links in JSON format.
"""

   )
   
   return agent

def get_links_user_prompt(url):
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
    links = fetch_links(url)
    user_prompt += "\n".join(str(link) for link in links)
    return HumanMessage(user_prompt)

print(get_links_user_prompt("https://edwarddonner.com"))


res=create_ai().invoke({
    "messages":[get_links_user_prompt("https://edwarddonner.com")]
})


def create_brochure(url):
    contents=fetch_web_contents(url)
    links=fetch_links(url)