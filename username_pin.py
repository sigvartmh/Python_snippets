#check user name and pin
#use box function for print
database = [
	['albert',  '1234'],
	['dilbert', '4242'],
	['smith',   '7224'],
	['john', 	'9843']
]

print len(database)
print max(database)
print min(database)
print min(9,2,3,7,4)

print list('Hello')


username = raw_input('User: ')
pin		 = raw_input('Pin: ' )



if [username,pin] in database: print 'Access granted'
else: print 'Acess denied'