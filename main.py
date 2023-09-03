from fastapi import FastAPI, UploadFile
import requests
from PIL import Image
from inference import inference

import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"id": item_id }

@app.post("/ask")
def ask(question: str, img_url: str):
    # url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    image = Image.open(requests.get(img_url, stream=True).raw)
    answer = inference(question, image)
    return { "answer": answer }

@app.post("/guess")
def guess(question: str, image: UploadFile):
    content = image.file.read()
    img = Image.open(io.BytesIO(content))
    # img = Image(image.file)
    result = inference(question, img)
    return result