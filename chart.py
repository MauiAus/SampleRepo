import sqlite3
import time
from datetime import datetime
import model

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

pathname = __file__
pathname = pathname[:-8]

#added code
#Cristelle was here

def plot_myPlot():
    conn = sqlite3.connect('cov.db')
    c = conn.cursor()
    wordUsed = 'DATE_TIME'
    sql = "SELECT DATE_TIME FROM cov_tracker "

    graphArray = []

    for row in c.execute(sql):
        startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
        splitInfo = startingInfo.split(',')
        graphArrayAppend = splitInfo[0]+''+splitInfo[1]
        graphArray.append(graphArrayAppend)

   # dt_string = "2021-02-11 15:27:03.734578"

    #Sample Code Here
    #Sample Date 2021-02-11 15:27:03.734578
    #dates = ["01/02/2020", "01/03/2020", "01/04/2020"] #Convert to Datetime
    #dates = ''.join(graphArray) # Convert graphArray List to String before putting it to dates
    dates = graphArray
    print(dates)

    x_values = [datetime.strptime(d,"%Y-%m-%d %H:%M:%S.%f").date() for d in dates]
    y_values = [datetime.strptime(d,"%Y-%m-%d %H:%M:%S.%f").date() for d in dates] 

    ax = plt.gca() #getting axis
    formatter = mdates.DateFormatter("%d/%m/%Y")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)
    plt.plot(x_values, y_values)
    #End

    #datestamp, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                                # converters={0: datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S.%f')})
            

    #ax1 = fig.add_subplot(1,1,1, axisbg='white')
    #plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=2)
