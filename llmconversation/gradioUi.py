import gradio as gr
from langchain_groq import ChatGroq
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

groqky=ChatGroq(model="moonshotai/kimi-k2-instruct")
groq=completion(model="groq/moonshotai/kimi-k2-instruct")
def AskQuestion(question):
    res=groq[{"role": "user", "content":question}]
    return res.choices[0].content
def vanakkam(greet):
    return greet


demo=gr.Interface(
    fn=AskQuestion,
    inputs="textbox",
    outputs="textbox",
    flagging_mode="never"
)

demo.launch()

