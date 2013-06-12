#print out a date, given year,month and day as number

months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
]

#A list with one ending for each number from 1 to 31

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
	+ ['st', 'nd', 'rd'] + 7 *['th'] \
	+ ['st']

year = raw_input('year: ')
month = raw_input('month (1-12): ')
day = raw_input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

#Remember to subtract 1 from month and day to get the correct index

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print month_name + ' ' + ordinal + ', ' + year
