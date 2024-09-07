from fastapi import FastAPI
from routes.routes import router
from database import create_tables

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    create_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)