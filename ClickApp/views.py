from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection
from datetime import datetime
import calendar

# All clicks
@csrf_exempt
def clickApi(request):
    try:
        if request.method=='POST':
            click_data=JSONParser().parse(request)
            campaign = click_data['Campaign']
            if isinstance(campaign, int):
                def clicks_sql():
                    with connection.cursor() as cursor:  
                        cursor.execute("SELECT COUNT (*) FROM Clicklog WHERE campaign=%s", [str(campaign)])
                        clicks = cursor.fetchone()
                    return clicks
                resp = {
                    "Status": 200, 
                    "Number_of_clicks":clicks_sql()[0],
                    "Message": "Success"
                }
                return JsonResponse(resp)
            else:
                return JsonResponse({
                    "Status": 302, 
                    "Message": "Incorrect values"
                    })
            
    except:
        return JsonResponse({
            "Status": 301, 
            "Message": "Incorrect parameters"
            })

# Clicks between two dates
@csrf_exempt
def clickTimeApi(request):
    try:
        if request.method=='POST':
            click_data=JSONParser().parse(request)
            campaign = click_data['Campaign']
            start = click_data['Start_date']
            end = click_data['End_date']
            # if isinstance(campaign, int) and isinstance(start, str) and isinstance(end, str):
            if (isinstance(campaign, int) and isinstance(start, str) and isinstance(end, str)):
                # Datetime
                start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
                end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

                # UTC timestamp
                start_date = datetime(start_dt.year, start_dt.month, start_dt.day, start_dt.hour, start_dt.minute, start_dt.second)
                start_utc = calendar.timegm(start_date.utctimetuple())

                end_date = datetime(end_dt.year, end_dt.month, end_dt.day, end_dt.hour, end_dt.minute, end_dt.second)
                end_utc = calendar.timegm(end_date.utctimetuple()) 
                
                def clicks_sql():
                    with connection.cursor() as cursor:  
                        cursor.execute("SELECT COUNT (*) FROM Clicklog WHERE campaign=%s AND timestamp BETWEEN %s AND %s", [str(campaign), str(start_utc), str(end_utc)])
                        clicks = cursor.fetchone()
                    return clicks
                resp = {
                    "Status": 200, 
                    "Number_of_clicks":clicks_sql()[0],
                    "Message": "Success"
                }
                return JsonResponse(resp)
            else:
                return JsonResponse({
                    "Status": 302, 
                    "Message": "Incorrect values"
                    })
            
    except:
        return JsonResponse({
            "Status": 301, 
            "Message": "Incorrect parameters"
            })