from typing import Optional

from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse("/docs")
    
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)