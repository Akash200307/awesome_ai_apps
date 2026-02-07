from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

# Initialize models with system messages
kimi = ChatGroq(model="moonshotai/kimi-k2-instruct")
gpt = ChatGroq(model="openai/gpt-oss-120b")

# System prompts
kimi_system = "you are romantic and non toxic assistant"
gpt_system = "you are an angry lovable person"

# Initialize message histories with system prompts
kimi_messages = [SystemMessage(content=kimi_system)]
gpt_messages = [SystemMessage(content=gpt_system)]

# Starting messages
gpt_start = "Hi"
kimi_start = "Hi, there"

print(f"GPT: {gpt_start}\n")
print(f"Kimi: {kimi_start}\n")

# Add initial exchanges to histories
gpt_messages.append(AIMessage(content=gpt_start))
kimi_messages.append(HumanMessage(content=gpt_start))
kimi_messages.append(AIMessage(content=kimi_start))

# Conversation loop
for i in range(5):
    # GPT's turn - receives Kimi's last message
    last_kimi = kimi_start if i == 0 else kimi_messages[-1].content
    gpt_messages.append(HumanMessage(content=last_kimi))
    
    gpt_res = gpt.invoke(gpt_messages)
    gpt_content = gpt_res.content
    gpt_messages.append(AIMessage(content=gpt_content))
    print(f"GPT: {gpt_content}\n")
    
    # Kimi's turn - receives GPT's response
    kimi_messages.append(HumanMessage(content=gpt_content))
    
    kimi_res = kimi.invoke(kimi_messages)
    kimi_content = kimi_res.content
    kimi_messages.append(AIMessage(content=kimi_content))
    print(f"Kimi: {kimi_content}\n")
