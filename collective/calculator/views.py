from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import calculator
from django.contrib import messages
import sqlite3


# Create your views here.
def index(request):
    print(request.POST)
    return render(request, "index.html")


def submitquery(request):
    tally = request.POST['tally']
    if request.method == 'POST':
        if request.POST.get('tally') and request.POST.get('result'):
            saverecord=calculator()
            saverecord.tally= request.POST.get('tally')
            saverecord.result= request.POST.get('result')
            saverecord.save()
            messages.success(request,'Record saved success..')
    try:
        result = eval(tally)
        mydictionary = {
            "tally" : tally,
            "result" : result,
            "error" : False,
            "answer" : True
        }
        return render(request, 'index.html', context=mydictionary)
    
    except:
        mydictionary = {
            "error": True,
            "answer" : False

        }
        return render(request, 'index.html', context=mydictionary)

#-- try:
#   # conn = sqlite3.connect('db.sqlite3')
#
#  #  cursor = conn.cursor()
#    print("Successfully Connected to SQLite")
#
#    sqlite_insert_query = """INSERT INTO calculator
#                          (tally, result,) 
#                           VALUES 
#                          ('20,'200')"""
#
#    count = cursor.execute(sqlite_insert_query)
#    conn.commit()
#    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
#    cursor.close()
#
#except sqlite3.Error as error:
#    print("Failed to insert data into sqlite table", error)
#finally:
#    if conn:
#        conn.close()
#        print("The SQLite connection is closed")
#