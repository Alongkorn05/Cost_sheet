import pandas as pd
import json
from fastapi import FastAPI, File , Request
from pydantic import BaseModel
from util import convert,super_ai

app = FastAPI()



@app.get("/")
async def A():
    return '200'

#load Data
@app.post("/getdata")
async def load(request:Request , encodeing = 'utf-8'):
    r = await request.json()
    
    convert(r)
    result = super_ai(r)
    return result


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
    