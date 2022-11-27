import os
import sys
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'genebox.settings')
django.setup()
from authdetails.models import authorDet
from django_countries import countries

def import_data():

    try:
        csv_file = input("Please Enter the CSV path: ")
        csv = pd.read_csv(csv_file)

        csv.columns = [c.lower() for c in csv.columns]
        author_count = 0

        for i,row in csv.iterrows():
            if not pd.isna(row['name']):
                name = row['name'].strip()
            else:
                name = 'Loaded From Csv'

            if not pd.isna(row['age']):
                age = row['age']
            else:
                age = 'Loaded From Csv'
                
            if not pd.isna(row['gender']):
                gender = row['gender'].strip()
            else:
                gender = 'Loaded From Csv'

            if not pd.isna(row['country']):
                country = row['country'].strip()
                for code, name in list(countries):
                    if name.lower() == country.lower():
                        country=code
                        break
            else:
                country = 'Loaded From Csv'
            
           
            authorDet.objects.create(
                auth_name = name,
                auth_age = age,
                auth_gender = gender,
                auth_country = country,
            ).save()
            author_count += 1
        print("Number of authors imported: " + str(author_count))
           
    except Exception as e:
        print(repr(e))        

import_data()    