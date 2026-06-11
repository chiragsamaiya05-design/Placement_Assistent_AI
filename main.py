from fastapi import FastAPI

app = FastAPI(
    title="Placement Assistant AI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Placement Assistant AI Running"
    }