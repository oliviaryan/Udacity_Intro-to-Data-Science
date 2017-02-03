# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#


	
	
def between_year(year1,year2):
	day_y=0
	if year1!=year2:
		for i in range(year1+1, year2):
			if i%400==0 or (i%4==0 and i%100!=0):
				day_y=day_y+366
			else:
				day_y=day_y+365
	return day_y
			
	
def year_first(year1,month1, day1):
	day_first= -day1
	for k in range(month1, 13):
		if k == 4 or k==6 or k==9 or k==11:
			day_first=day_first+30
		elif k==2:
			if year1%400==0 or (year1%4==0 and year1%100!=0):
				day_first=day_first+29
			else:
				day_first=day_first+28
		else:
			day_first=day_first+31
	return day_first
	
def year_last(year2,month2,day2):
	day_last=day2
	for k in range(1,month2):
		if k == 4 or k==6 or k==9 or k==11:
			day_last=day_last+30
		elif k==2:
			if year2%400==0 or (year2%4==0 and year2%100!=0):
				day_last=day_last+29
			else:
				day_last=day_last+28
		else:
			day_last=day_last+31
	return day_last	
		
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
	if year1!=year2:
		result=between_year(year1,year2)+year_first(year1,month1,day1)+year_last(year2,month2,day2)
	else:
		if year2%400==0 or (year2%4==0 and year2%100!=0):
			result= year_last(year2,month2,day2)+year_first(year1,month1,day1)-366
		else:
			result= year_last(year2,month2,day2)+year_first(year1,month1,day1)-365
	return result
		
		
	
	


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()