from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from decouple import config



access_token = config('access_token')
print(access_token)

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.api_route("/api/text", methods=["GET", "POST"])
async def sendText(psid :str, text : str):
    out = {
        psid : psid,
        text : text
    }
    return JSONResponse(content=out)

@app.get("/api/echo")
async def get_user_info(text :str):
    out = {
        output : text,
    }
    return JSONResponse(content=out)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
