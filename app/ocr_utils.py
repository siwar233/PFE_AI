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

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to create PostgreSQL connection and cursor
def create_connection():
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_username",
        password="your_password"
    )
    cursor = conn.cursor()
    return conn, cursor

# Function to insert experience record
def insert_experience(cursor, title, start_date, end_date, company):
    cursor.execute('''INSERT INTO "Experience" (Title, StartDate, EndDate, Company) VALUES (%s, %s, %s, %s)''',
                   (title, start_date, end_date, company))

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

# Method to extract experience details from text
def extract_experience_details(text):
    title_match = re.search(r'Title:\s*(.*)', text)
    start_date_match = re.search(r'Start Date:\s*(.*)', text)
    end_date_match = re.search(r'End Date:\s*(.*)', text)
    company_match = re.search(r'Company:\s*(.*)', text)
    
    if title_match and start_date_match and end_date_match and company_match:
        title = title_match.group(1)
        start_date = start_date_match.group(1)
        end_date = end_date_match.group(1)
        company = company_match.group(1)
        return title, start_date, end_date, company
    return None, None, None, None
