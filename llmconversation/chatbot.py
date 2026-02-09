import gradio as gr
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def chatter(message, history):
    res = completion(
        model="groq/moonshotai/kimi-k2-instruct",
        messages=history + [{"role": "user", "content": message}],
    )
    return res.choices[0].message.content

view = gr.ChatInterface(fn=chatter)
view.launch()
