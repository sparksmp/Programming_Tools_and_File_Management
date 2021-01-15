import pandas
import datetime
import calendar
import numpy as np
import matplotlib.pyplot as plt

class Assignment1(object):
    def __init__(self, file_name):
        self.filename = file_name
        self.data = pandas.read_csv(self.filename, names = ['Station ID', 'Station Name', 'Date', 'Day Type', 'Rides'], skiprows = [1], low_memory = False)

    def get_column(self, column):
        return self.data[column].tolist()

def assignment2(data):
    station_id = data.get_column('Station ID')
    date = data.get_column('Date')
    rides = data.get_column('Rides')
    n = len(station_id)
    L_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    L_sum_of_rides = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        if station_id[i] == '40350':
            month = int(date[i][:2])
            day = int(date[i][3:5])
            month = int(date[i][:2])
            year = int(date[i][6:])
            L_num[month-1] += 1
            L_sum_of_rides[month-1] += int(rides[i])

    for m in range(1, 13):
        avg = L_sum_of_rides[m-1]/L_num[m-1]
        month = calendar.month_name[m]
        print('{}: {}'.format(month, avg))

def getWeekday(year, month, day):
    date = datetime.date(year, month, day)
    return calendar.day_name[date.weekday()]

def assignment3(data):
    Days_Rides = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    Days_Count = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    station_id = data.get_column('Station ID')
    date = data.get_column('Date')
    rides = data.get_column('Rides')
    n = len(station_id)
    for i in range(n):
        if station_id[i] == '40350':
            day = int(date[i][3:5])
            month = int(date[i][:2])
            year = int(date[i][6:])
            weekday = getWeekday(year, month, day)
            Days_Rides[weekday] += int(rides[i])
            Days_Count[weekday] += 1
    week_avg = {key: Days_Rides[key] / Days_Count[key] for key in Days_Rides}
    for k, v in week_avg.items():
        print('{}: {}'.format(k, v)) 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = list(week_avg.values())
    p = np.polyfit(x, y, 6)
    F = np.poly1d(p)
    print('\nPredicted number of rides on a Wednesday: {}'.format(F(3)))
    max = int(np.argmax(y))
    busy = calendar.day_name[max]
    min = int(np.argmin(y))
    slow = calendar.day_name[min]
    print('Busiest day of the week for UIC-Halsted stop: {}'.format(busy))
    print('Slowest day of the week for UIC-Halsted stop: {}'.format(slow))
    plt.plot(x, y, 'ro')
    xspace = np.linspace(1, 7, 50)
    yspace = F(xspace)
    plt.plot(xspace, yspace, 'b-')
    plt.show()
  
def main():
    data = Assignment1('Ridership.csv')
    print('Monthly Average Rides:')
    assignment2(data)
    print('\nWeekday Average Rides:')
    assignment3(data)

main()