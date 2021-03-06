from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application():
    app = FastAPI(title="Meory", version="0.0.1")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = get_application()
