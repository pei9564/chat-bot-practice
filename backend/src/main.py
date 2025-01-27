from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes import router
import uvicorn

app = FastAPI()

# 註冊全局例外處理器
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Something went wrong!", "error": str(exc)}
    )

# 註冊路由
app.include_router(router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7717, reload=True)