# -*- coding: utf-8 -*-
from django.shortcuts import render


from django.views.generic.base import View
from django.template import loader
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

class HomePageView(View):
    def dispatch(self, request, *args, **kwargs):

        db = connect_to_cloudsql()
        cursor = db.cursor()
        cursor.execute("USE jojodb;")
        cursor.execute("set autocommit = 1;")

        template = loader.get_template('index/index.html')


        if request.method == 'POST':
            logging.debug("Delete Button Pressed")
            store_number = request.POST.get("store_number")
            logging.debug("Deleting : " + store_number)

            query = "DELETE FROM mytable WHERE Store_Number = '" + store_number + "';"
            logging.debug("query is : " + query)
            cursor.execute(query)

        cursor.execute("SELECT * FROM mytable WHERE BINARY StateProvince = 'CA';")
        query_results = dictfetchall(cursor)
        context = {
            'query_results': query_results,
        }
        return render(request, 'index/index.html', context)


