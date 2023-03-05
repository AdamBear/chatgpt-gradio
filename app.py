import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
#openai.api_key = os.environ[""]


prompt = "请在这里输入您的问题后点'提交'按钮"

def openai_create(prompt):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "你是一名全能的信息助手"},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
    )

    return response.choices[0]['message']['content']



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>ChatGPT API测试演示</center></h1>
    """)
    chatbot = gr.Chatbot(label="ChatGPT")
    message = gr.Textbox(label="问题输入", placeholder=prompt)
    state = gr.State()
    submit = gr.Button("提交")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(server_name="0.0.0.0", server_port=8889, share=True, debug = True)
