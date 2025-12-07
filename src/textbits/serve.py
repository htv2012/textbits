import fastapi


def serve(args: list[str]):
    """Serve the bits"""
    print(f"Entering serve({args})")


app = fastapi.FastAPI()


@app.get("/")
def get_root():
    return {"status": "under construction"}
