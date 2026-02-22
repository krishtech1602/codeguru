import requests
import json
import gradio as gr

headers = {
    'Content-Type': 'application/json',
}

url = "http://localhost:11434/api/generate"

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codeguru",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = response.json()
        return data['response']
    else:
        return "Error: " + response.text

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt here..."),
    outputs="text"
)

interface.launch()