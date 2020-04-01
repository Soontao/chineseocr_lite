from flask import Flask, request
from PIL import Image
import numpy as np
from model import text_predict, crnn_handle
from application import trainTicket, idcard

app = Flask(__name__)


@app.route("/")
def entry():
    return {"service": "chinese ocr", "status": "up"}


@app.route("/ocr", methods=["POST"])
def ocr():
    if 'image' not in request.files:
        return {"error": "'image' not found"}

    img = Image.open(request.files["image"]).convert("RGB")
    img = np.array(img)

    result = text_predict(img)

    res = [
        {
            'text': x['text'],
            'name': str(i),
            'box': {
                'cx': x['cx'],
                'cy': x['cy'],
                'w': x['w'],
                'h': x['h'],
                'angle': x['degree']
            }
        } for i, x in enumerate(result)
    ]

    return {"result": res}


@app.route("/trainTicket", methods=["POST"])
def trainTicketOCR():

    if 'image' not in request.files:
        return {"error": "'image' not found"}

    img = Image.open(request.files["image"]).convert("RGB")
    img = np.array(img)

    result = text_predict(img)
    res = trainTicket.trainTicket(result)
    res = res.res
    res = [{'text': res[key], 'name':key} for key in res]
    return {"result": res}


@app.route("/IDCard", methods=["POST"])
def idCardOCR():

    if 'image' not in request.files:
        return {"error": "'image' not found"}

    img = Image.open(request.files["image"]).convert("RGB")
    img = np.array(img)

    result = text_predict(img)
    res = idcard.idcard(result)
    res = res.res
    res = [{'text': res[key], 'name':key} for key in res]
    return {"result": res}
