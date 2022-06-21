from fastapi import FastAPI

app = FastAPI(
    title='Claimfy API',
    openapi_url='/openapi.json',
    docs_url="/"
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8081, log_level="debug")
