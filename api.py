from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import random
import string

api = FastAPI()

db_name = "urls.db"

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class URLRequest(BaseModel):
    long_url: str
    custom_url: str = None

@api.post("/shorten")
def shorten_url(data: URLRequest):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    short_url = data.custom_url if data.custom_url else generate_short_url()
    
    cursor.execute("SELECT short_url FROM urls WHERE short_url = ?", (short_url,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="Custom URL already taken")
    
    cursor.execute("INSERT INTO urls (long_url, short_url) VALUES (?, ?)", (data.long_url, short_url))
    conn.commit()
    conn.close()
    
    return {"short_url": f"http://localhost:5000/{short_url}"}