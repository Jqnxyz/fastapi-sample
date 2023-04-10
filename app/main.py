from dotenv import load_dotenv
import sys
import os
from fastapi import FastAPI
from .routers import api

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()
sys.path.append(BASE_DIR)

app = FastAPI()
app.include_router(api.router)
