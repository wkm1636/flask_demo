from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/")
def get_user():
    return {"name": "John", "age": 20}

# 写一个注释

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
