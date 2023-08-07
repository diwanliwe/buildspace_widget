from typing import Optional

from fastapi import FastAPI

from data import houses

app = FastAPI()

@app.get("/")
async def root():
    print ("someone pinged the root")
    return { "gaudmire" : {"live" :{"widget_type":"person-related","author_username" : "farza", "author_ppURL" : "https://diwanliwe.github.io/sparkles_api/farza.png", "context" : "3 weeks ago", "quote_text" : "Welcome to the alternative life path","footer" : "#bsfondamentals","nameSpacer" : 6,"contextSpacer" : 4,"quoteSpacer": 25,"alignBottom" : 100,"quoteSize": 16, "background_URL" : "https://diwanliwe.github.io/sparkles_api/mountain.png","logo_URL" : "https://diwanliwe.github.io/sparkles_api/bslogo.png","content_url" : "https://twitter.com/FarzaTV/status/1678561092308705281"}}}   

@app.get("/gaudmire")
async def gaudmire():
    return {"data": houses["gaudmire"]["live"]}

@app.get("/alterok")
async def alterok():
    return {"data": houses["alterok"]["live"]}

@app.get("/spectreseek")
async def spectreseek():
    return {"data": houses["spectreseek"]["live"]}

@app.get("/erevald")
async def ereval():
    return {"data": houses["ereval"]["live"]}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
