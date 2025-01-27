import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda" if torch.cuda.is_available() else "cpu"


model_name = "gpt2-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def validate_prompt(prompt: str):
    if len(prompt.strip()) == 0:
        raise ValueError("El prompt no puede estar vacío.")
    return True

def model_pipeline(prompt: str, max_length: int = 128, temperature: float = 0.5, top_p: float = 1.0):
    try:
        validate_prompt(prompt)
    except ValueError as e:
        return f"Error: {e}"
    
    encoding = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
    input_ids = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)  
    
    
    model.config.pad_token_id = tokenizer.pad_token_id  
    
    with torch.no_grad():
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,  
            max_length=max_length,
            num_beams=5,
            do_sample=True,
            top_p=top_p,
            no_repeat_ngram_size=2,
            temperature=temperature
        )
    
    
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    return generated_text
