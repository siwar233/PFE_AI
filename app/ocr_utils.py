#method to extract text from pdf 
# method  text from image 
#config

from pdfminer.high_level import extract_text as extract_text_from_pdf
import cv2
import numpy as np
import pytesseract
import psycopg2
import re
import os

# Function to create PostgreSQL connection and cursor

# Method to extract text from PDF
def extract_text_from_pdf_file(filepath):
    return extract_text_from_pdf(filepath)

# Method to extract text from image
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

# Method to deskew image
def deskew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]
    
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated


