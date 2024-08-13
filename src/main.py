# FastApi imports
from fastapi import FastAPI, status, Response, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .routers import router as api_router
# Code Block


app = FastAPI(title="Research Project",
              version="0.0.1",
              docs_url="/documentation/"
              )

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return JSONResponse(content={"message": "Application is up!"})


app.include_router(api_router)