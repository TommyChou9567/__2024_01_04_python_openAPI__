from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('rediss://red-cmjja4un7f5s73cc1f1g:m6m3RSKfbGMKqHpBE3S5NKOjAWE1UdWb@singapore-redis.render.com:6379'))

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}