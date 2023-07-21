import uvicorn
from fastapi import FastAPI

from config import config

app = FastAPI()


@app.get("/")
async def is_alive() -> str:
    return "I'm running"


def main():
    uvicorn.run("main:app", host=config.host, port=config.port, reload=True)


if __name__ == '__main__':
    main()
