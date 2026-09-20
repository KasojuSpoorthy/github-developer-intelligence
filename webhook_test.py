from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/webhook")
async def github_webhook(request: Request):
    data = await request.json()

    print("Webhook received!")
    print(data)

    return {"status": "received"}