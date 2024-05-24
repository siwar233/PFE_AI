import cv2
import numpy as np
import pytesseract
import psycopg2
import os



# Function to insert experience record
def insert_experience(cursor, title, start_date, end_date, company):
    cursor.execute('''INSERT INTO "Experience" (Title, StartDate, EndDate, Company) VALUES (%s, %s, %s, %s)''',
                   (title, start_date, end_date, company))

# Method to extract text from PDF
def extract_text_from_pdf_file(filepath):
    # to do 
   pass 

# Method to extract text from image
def extract_text_from_image(image):
    # to do 
   pass 





