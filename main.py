import logging
from fastapi import FastAPI, Form, Depends, HTTPException, status, Header
from model import model_pipeline
from dotenv import load_dotenv
import os


load_dotenv()


logging.basicConfig(
    filename='app.log',  
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    encoding='utf-8'  
)

app = FastAPI()

API_TOKEN = os.getenv("API_TOKEN")

def verify_token(token: str = Header(...)):
    if token != API_TOKEN:
        logging.error("Intento de acceso con token inválido")  
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token de autenticación inválido")
    logging.info("Token de autenticación válido")  
    return token

@app.get("/")
def read_root():
    logging.info("Acceso a la ruta raíz")  
    return {"Text Generation": "GPT-2"}

@app.post("/generate")
def generate(prompt: str = Form(...), max_length: int = Form(128), temperature: float = Form(0.5), top_p: float = Form(1.0), token: str = Depends(verify_token)):
    logging.info(f"Generando texto con el prompt: {prompt}")  
    try:
        result = model_pipeline(prompt, max_length, temperature, top_p)
        logging.info("Texto generado correctamente")  
        return {"generated_text": result}
    except Exception as e:
        logging.error(f"Error al generar texto: {str(e)}")  
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error en la generación de texto")
