from rag.template import get_table_prompt
from llama_index.core import Document
from typing import Iterable
import copy


def get_table_summary(model, table_data: dict) -> dict:
    table_data = copy.deepcopy(table_data) or {}
    table_text = table_data["text"]
    prompt = get_table_prompt(table_text)
    chat_prompt = model.format_prompt(prompt)
    summary = model.text_generation(chat_prompt)
    table_data["text"] = summary
    return table_data


def get_image_summary(model, image_path):
    return model.image_to_text(image_path)


def format_document(text: str, reference: int, category: str) -> Document:
    return Document(text=text, metadata={"reference": reference, "category": category})


def images2docs(images: Iterable) -> list[Document]:
    return [
        format_document(image_text, key, "Image") for key, image_text in images.items()
    ]


def tables2docs(tables: Iterable) -> list[Document]:
    return [
        format_document(table_text, key, "Table") for key, table_text in tables.items()
    ]


def texts2docs(texts: Iterable) -> list[Document]:
    return [format_document(text, key, "Text") for key, text in texts.items()]