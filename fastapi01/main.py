from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/")
def get_user():
    return {"name": "John", "age": 20}

@app.post("/user/")
def create_user(name: str, age: int):
    return {"name": name, "age": age}

# hello 222
# hello world
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
