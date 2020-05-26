import redis
import os

host = os.getenv("REDIS_HOST") or "localhost"
port = os.getenv("REDIS_PORT") or 6379
r = redis.Redis(host, port)

def set_value(key: str, value):
  r.set(key, value)

def get_value(key: str):
  return r.get(key) or "Value not found"
