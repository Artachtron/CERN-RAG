from dotenv import load_dotenv
from utils.path import PATH
import os

load_dotenv(PATH.backend / "secrets.env")

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
WCS_API_KEY = os.getenv("WCS_API_KEY")
WCS_CLUSTER_URL = os.getenv("WCS_CLUSTER_URL")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
UNSTRUCTURED_API_KEY = os.getenv("UNSTRUCTURED_API_KEY")
