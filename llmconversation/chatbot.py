import gradio as gr
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def chatter(message, history):
    res = completion(
        model="groq/moonshotai/kimi-k2-instruct",
        messages=history + [{"role": "user", "content": message}],
        stream=True
    )
    result =" "

    for chunk in res:
        result+=chunk.choices[0].delta.content or " "
        yield result

view = gr.ChatInterface(fn=chatter)
view.launch()
