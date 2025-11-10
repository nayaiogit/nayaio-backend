from fastapi import FastAPI
from api.routes import employees

app = FastAPI()

app.include_router(employees.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Nayaio Backend — Core Engine running"}
