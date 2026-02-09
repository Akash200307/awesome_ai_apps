from typing import Never
from litellm import completion
import gradio as gr
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

message_input=gr.Textbox(label="Your msg",info="Enter your prompt")
message_output=gr.Markdown(label="Response")

view=gr.Interface(
    fn=streamKimi,
    title="kimi",
    inputs=[message_input],
    outputs=[message_output],
    examples=["powerful programming languages top5 with their use"],
    flagging_mode="never"
)

view.launch()

