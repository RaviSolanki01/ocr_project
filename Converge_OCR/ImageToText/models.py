import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/ravi/API/Text Detetion-6d2ed21174a6.json"

from django.db import models
import argparse
import io
import re


def detect_document(path):
    text_return = ''
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            text_return += '\n'

            for paragraph in block.paragraphs:
                text_return += '\n'

                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    text_return += ' '

                    for symbol in word.symbols:
                        text_return += symbol.text
    return text_return