from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render


from django.views.generic.base import View
from django.template import loader
from .forms import LocationForm

import os
import MySQLdb
import logging

CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')

def connect_to_cloudsql():
    cloudsql_unix_socket = os.path.join(
        '/cloudsql', CLOUDSQL_CONNECTION_NAME)

    db = MySQLdb.connect(
        unix_socket=cloudsql_unix_socket,
        user=CLOUDSQL_USER,
        passwd=CLOUDSQL_PASSWORD)
    return db

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class Add_Loc(View):
    def dispatch(self, request, *args, **kwargs):

        db = connect_to_cloudsql()
        cursor = db.cursor()
        cursor.execute("USE jojodb;")
        cursor.execute("set autocommit = 1;")

        if request.method == 'POST':
            form = LocationForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                data = form.cleaned_data
                store_number = data['store_number']
                store_name = data['store_name']
                ownership = data['ownership']
                address = data['address']
                city = data['city']
                postcode = data['postcode']
                country = data['country']
                phone = data['phone']

                query = """INSERT INTO mytable ( Store_Number , Store_Name ,Ownership_Type, Street_Address, City, StateProvince, Postcode, Country, Phone_Number, Timezone, Longitude, Latitude)
VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
;""".format(store_number, store_name, ownership, address, city, 'CA', postcode, country, phone, "GMT-08:00 America/Los_Angeles","-121.83","-121.83")
                cursor.execute(query)
                logging.debug("Create Button Press query : " + query )
                return HttpResponseRedirect('https://composed-setup-158400.appspot.com/')

    # if a GET (or any other method) we'll create a blank form
        else:
            form = LocationForm()

        return render(request, 'newLoc/newLoc.html', {'form': form})


