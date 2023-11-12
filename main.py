import uvicorn
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Annotated
from model_pipeline import predict_step

app = FastAPI()


class Data(BaseModel):
    item: str


@app.get("/data", response_model=Data)
async def get_data() -> Data:
    """
    Get Data
    """
    return Data(item="devops")


@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict[str, str]:
    """
    Get an Item
    """
    return {"item_id": item_id}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    image_paths = []
    for file in files:
        contents = await file.read()
        # Save the file to images folder
        with open(f"images/{file.filename}", "wb") as f:
            f.write(contents)

        image_paths.append(f"./images/{file.filename}")

    # Use os.listdir to get all files in the directory
    # files = os.listdir("./images/tmp")

    print(image_paths)
    preds = predict_step(image_paths)

    return {"predictions": [pred for pred in preds]}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
