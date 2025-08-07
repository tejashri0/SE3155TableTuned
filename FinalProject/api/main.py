import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import model_loader
from .routers import index as indexRoute  # OR .controllers.index if you move it
from .dependencies.config import conf

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models and routes
model_loader.index()
indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
