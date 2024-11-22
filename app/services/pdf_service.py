import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from fastapi import UploadFile
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

import nltk
nltk.download("stopwords")
nltk.download("punkt")

STOPWORDS = set(stopwords.words("english"))

def extract_text_from_pdf(file: UploadFile) -> str:
    try:
        # Try PyPDF2 for text extraction
        reader = PdfReader(file.file)
        text = "".join(page.extract_text() for page in reader.pages)
        if not text.strip():
            logger.warning("No text extracted with PyPDF2. Using OCR.")
            text = extract_text_using_ocr(file)
        return preprocess_text(text)
    except Exception as e:
        logger.error(f"Error parsing PDF: {e}")
        raise ValueError("Invalid or low-quality PDF file")


def extract_text_using_ocr(file: UploadFile) -> str:
    try:
        images = convert_from_path(file.file, dpi=300)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image, lang="eng")
        return text
    except Exception as e:
        logger.error(f"OCR processing failed: {e}")
        raise ValueError("Failed to process PDF with OCR")


def preprocess_text(text: str) -> str:
    logger.info("Preprocessing extracted text")
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower()
    tokens = word_tokenize(text)
    cleaned_text = " ".join(word for word in tokens if word not in STOPWORDS)
    return cleaned_text
