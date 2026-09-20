from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Solar Digital Twin backend is running"}
