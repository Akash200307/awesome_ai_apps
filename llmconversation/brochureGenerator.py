from typing import Never
from litellm import completion
import gradio as gr

from brochure_project.brochure import fetch_web_contents 


system_message="you are a helpful tamil assistant answers any question in tanglish from any language"


def streamKimi(prompt):
    kimi = completion(
        model="groq/moonshotai/kimi-k2-instruct",
        stream=True,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    result=""
    for chunk in kimi:
        result+= chunk.choices[0].delta.content or ""
        yield result  # Yield only new content, not accumulated
        
def brochure(companyName,url):
    yield ""
    prompt =f"Please generate a brochure for {companyName} . Here is their landing page:\n"
    prompt+=fetch_web_contents(url)
    result =streamKimi(prompt)
    yield from result
message_input=gr.Textbox(label="Your msg",info="Enter your prompt")
message_output=gr.Markdown(label="Response")
name_input=gr.Textbox(label="Enter company name")
url_input=gr.Textbox(label="Enter url here")
view=gr.Interface(
    fn=brochure,
    title="kimi",
    inputs=[url_input,name_input],
    outputs=[message_output],
    examples=[["Edward Donner", "https://edwarddonner.com"]],
    flagging_mode="never"
)

view.launch()

