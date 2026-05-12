import gradio as gr
from transformers import pipeline
import torch

# Define the model ID
model_id = "Hamzasajjad38/pakistan-leaders-tinyllama-peft-merged"

# Initialize the text-generation pipeline
print("Loading model...")
try:
    pipe = pipeline("text-generation", model=model_id, device_map="auto", torch_dtype=torch.bfloat16)
except Exception as e:
    pipe = pipeline("text-generation", model=model_id)

def generate_response(message, history, system_prompt, temperature, max_new_tokens, top_p):
    messages = []
    
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
        
    # Safely handle different history formats across Gradio versions
    for item in history:
        if isinstance(item, dict):
            messages.append({"role": item.get("role", "user"), "content": item.get("content", "")})
        elif hasattr(item, "role") and hasattr(item, "content"):
            messages.append({"role": item.role, "content": item.content})
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            user_msg, asst_msg = item
            if user_msg:
                messages.append({"role": "user", "content": user_msg})
            if asst_msg:
                messages.append({"role": "assistant", "content": asst_msg})
            
    if isinstance(message, dict):
        messages.append({"role": "user", "content": message.get("text", message.get("content", ""))})
    elif hasattr(message, "content"):
        messages.append({"role": "user", "content": message.content})
    else:
        messages.append({"role": "user", "content": str(message)})
    
    try:
        prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    except:
        prompt = ""
        for msg in messages:
            prompt += f"<|{msg['role']}|>\n{msg['content']}\n"
        prompt += "<|assistant|>\n"
    
    outputs = pipe(
        prompt,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
        pad_token_id=pipe.tokenizer.eos_token_id
    )
    
    generated_text = outputs[0]["generated_text"][len(prompt):]
    return generated_text

demo = gr.ChatInterface(
    fn=generate_response,
    additional_inputs=[
        gr.Textbox(label="System Prompt", value="You are a helpful AI assistant knowledgeable about the leaders of Pakistan.", lines=2),
        gr.Slider(label="Temperature", minimum=0.1, maximum=2.0, value=0.7, step=0.1),
        gr.Slider(label="Max New Tokens", minimum=1, maximum=1024, value=512, step=1),
        gr.Slider(label="Top P", minimum=0.1, maximum=1.0, value=0.95, step=0.05),
    ]
)

if __name__ == "__main__":
    demo.launch()
