from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to moringa tribune')


def news_of_day(request):
    date = dt.date.today()
    # function to convert date object to find exact day
    day = convert_dates(date)
    html = f'''
            <html>
            <body>  
                <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
            </html>
            '''
    return HttpResponse(html)


def convert_dates(dates):
    #Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    #retuning the actual day of the week
    day = days[day_number]
    return day



def past_days_news(request, past_date):
    try:
        #converts data from the strinf url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # raise 404 error when valueerror is thrown
        raise Http404()
        
    # converts data from the string url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convert_dates(date)
    html = f'''
            <html>
            <body>  
                <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
            </html>
            '''
    return HttpResponse(html)
