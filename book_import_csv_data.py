import os
import sys
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'genebox.settings')
django.setup()
from authdetails.models import bookDet, authorDet
from django_countries import countries

def import_data():

    try:
        csv_file = input("Please Enter the CSV path: ")
        csv = pd.read_csv(csv_file)

        csv.columns = [c.lower() for c in csv.columns]
        book_count = 0

        for i,row in csv.iterrows():
            author_det = None
            date = None
            pages = 0
            rating = 0
            if not pd.isna(row['name']):
                name = row['name'].strip()
            else:
                name = 'Loaded From Csv'

            if not pd.isna(row['author']):
                author = row['author'].strip()
                author_det=authorDet.objects.get(auth_name=author)        
                
            if not pd.isna(row['date']):
                date = row['date'].strip()
            
            if not pd.isna(row['pages']):
                pages = int(row['pages'])
            
            if not pd.isna(row['ratings']):
                rating = int(row['ratings'])
            
           
            bookDet.objects.create(
                book_name = name,
                book_author = author_det,
                book_pages = pages,
                average_critics_rating = rating,
                book_date=date,
            ).save()
            book_count += 1
        print("Number of books imported: " + str(book_count))
           
    except Exception as e:
        print(repr(e))        

import_data()    