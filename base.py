from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def index():
    return {}

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.get("/hello/{id}")
def hello_id(id: str = Path(pattern=r'^[a-zA-Z0-9\-]+$')):
    return_id = f"MyId-{id}"
    return {"message": "Hello World", "id": return_id}
