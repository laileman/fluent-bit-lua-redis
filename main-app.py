import argparse
from fastapi import FastAPI
import logging
from pydantic import BaseModel
from pythonjsonlogger import jsonlogger


parser = argparse.ArgumentParser()
parser.add_argument("--log_file", type=str, default="app.log", help="log file")
args = parser.parse_args()


# 创建 logger
logger = logging.getLogger("jsonLogger")
logger.setLevel(logging.DEBUG)

# 创建 StreamHandler 输出到控制台
logHandler = logging.StreamHandler()

# JSON formatter（重点）
formatter = jsonlogger.JsonFormatter(
    "%(asctime)s %(levelname)s %(message)s %(app)s %(age)s %(from)s %(ip)s %(city)s",

)
logHandler.setFormatter(formatter)

# 创建 FileHandler，输出到文件
file_handler = logging.FileHandler(args.log_file)  # 👈 输出到 app.log 文件
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.addHandler(file_handler)


app = FastAPI()


class Req(BaseModel):
    age: int = None
    ip: str = None
    from_: str = None
    city: str = None


@app.post("/")
def root(request: Req):
    logger.info(
        "Hello Leman",
        extra={
            "app": "main-app.py",
            "age": request.age,
            "from": request.from_,
            "ip": request.ip,
            "city": request.city,
        },
    )
    return {"message": "Hello Leman"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
