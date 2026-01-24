from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()
llm=ChatGroq(model='moonshotai/kimi-k2-instruct-0905')

SystemMessage=SystemMessage("ROLE:You are a sentence complete assistant"
                            "Goal:Produce a perfect sentence without grammar mistake" \
                            "Instructions:" \
                            "-Add a header Here is the completed sentence:" \
                            "-below the header list 10 completed sentences with starting trail of * and space" \
                            "Now proceed to generate the sentence")

agents=create_agent(
    model=llm,
    
)

user_input=HumanMessage(input("Enter the incomplete sentence:"))
response=agents.invoke({
    "messages":[SystemMessage,user_input]
})

print(response["messages"][-1].content)


