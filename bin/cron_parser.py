#!/usr/bin/env python

"""cron_parser.py: command line utility to check cron expressions and
parse all possible outputs for security purposes"""

"""
method to convert cron piece to 1. check if has wild cards
                                2. strip them if it does
                                3. operate via wild cards and determine all possible values for term
                                4. save all value to list
need to output cron_pieces on separate lines. cron_pieces are: minute, hour, day of month, month, day of week
"""
__author__ = "Ed Heaver"
__credits__ = ["Ed Heaver"]
__license__ = "GPL"
__version__ = "0.8"
__maintainer__ = "Ed Heaver"
__email__ = "edward.heaver01@gmail.com"
__status__ = "Development"

#import re and argv from sys
import re
from sys import argv

#accept user input from cmdline with script (hard coded cron_ex for testing purposes)
#cron_ex = argv

cron_ex = "*/15 0 1,15 * 1-5 /usr/bin/find"
#minutes, hours, day of month, month, day of week lists

minutes = []
hours = []
day_of_month = []
month = []
day_of_week = []

#split cron into pieces
cron_pieces = cron_ex.split(" ")


#funtion to strip non numeric chars and operate on numbers with wild card chars removed. currently have *,/,- and , implemented and can implement more

def cron_output (piece, time_period, values):
    
    if bool(re.match(r"^\*\/\d+$", piece)) == True:
        number = int(re.sub(r"\W+", '', piece))
        for i in range(0,time_period):
            if i%number == 0:
                values.append(i)
        return values
    elif bool(re.match(r"^\*$", piece)) == True:
        for i in range(1,time_period):
            values.append(i)
        return values
    elif bool(re.match(r"^\d+\-\d+$", piece)) == True:
        terms = piece.split('-')
        term1 = int(terms[0])
        term2 = int(terms[1])+1
        for i in range (term1, term2):
            values.append(i)
        return values 
    elif bool(re.match(r"^\d+$", piece)) == True:
            number = int(re.sub(r"\W+", '', piece))
            values.append(number)
            return values

    elif bool(re.match(r"^\d+\,\d+$", piece)) == True:
        terms = piece.split(',')
        term1 = int(terms[0])
        term2 = int(terms[1])
        values.append(term1)
        values.append(term2)
        return values
    else:
        return values
    return values   

         
#output cron pieces into grid of all possible outputs and error handling
if len(argv) != 6:
    minutes = cron_output(cron_pieces[0],60, minutes)
    hours = cron_output(cron_pieces[1], 24, hours)
    day_of_month = cron_output(cron_pieces[2], 31, day_of_month)
    month = cron_output(cron_pieces[3], 13, month)
    day_of_week = cron_output(cron_pieces[4], 7, day_of_week)

    print("Minutes: " + str(minutes))
    print("Hours: " + str(hours))
    print("Day of the Month: " + str(day_of_month))
    print("Month: " + str(month))
    print("Day of the Week: " + str(day_of_week))
    print(cron_pieces[5])
else:
    print("This is not a valid cron. There needs to be 6 arguments.")



