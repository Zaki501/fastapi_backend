from fastapi import FastAPI
from api.routes import auth, users
import core.models as models
from core.database import engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
async def hello_world():
    return {"message": "Hello Application!"}


if __name__ == "__main__":
    pass