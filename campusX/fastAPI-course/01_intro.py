from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"msg": "Hello world"}


@app.get("/about")
def about():
    return {
        "msg": "I am polymath have different interest like in AI, DE and SE etc, who wants to make a trading bot which will manage my portfolio"
    }
