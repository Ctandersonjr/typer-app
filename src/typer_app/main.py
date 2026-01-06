from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
   return {"status":"ok"}

@app.get("/")
def table():
   return {"table":"Initialized"}