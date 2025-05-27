import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/api/hello") 
async def hello(name:str="World"):
#Небольште вычисления на сторонние сервера
    greeting_length=len(f"Hello,{name}!")
    return{
        "message":f"Hello, {name}!",
        "length": greeting_length,
        "reversed": name[::-1]
    }

if __name__ =="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8001)