from fastapi import FastAPI

app = FastAPI()

@app.get('/o/{to}/{from}')