# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

date =[int(x) for x in input().split()]
print(calendar.day_name[calendar.weekday(date[2],date[0],date[1])].upper())