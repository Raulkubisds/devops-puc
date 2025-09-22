from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API funcionando no Docker!"}


def read_root():
    return {"mensagem": "API funcionando!"}
