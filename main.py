import datetime
#
# #---------------------1
# chislo = str(20201212)
#
# temp = datetime.datetime.strptime(chislo, '%Y%m%d').date()
# print(temp)

#---------------------2

# day = 10
# month = 3
# year = 2021
#
# temp = datetime.date(year,month,day)
# print(temp)

#---------------------3
#
# s = "19901204"
#
# t = datetime.datetime.strptime(s, '%Y%m%d').date()
# print(t)


#---------------------4

# today = datetime.datetime.now() - datetime.timedelta(days = 30)
# r = today + datetime.timedelta(days=365)
# print(r)
# print(r.weekday() + 1)

#---------------------5
# n = int(input('Введите день : '))
# if 1 <= n <= 365:
#     res = datetime.datetime(2021,1,1) + datetime.timedelta(days=n)
#     print(res)
# else:
#     print('ERROR!')

#---------------------6
# _res = datetime.datetime.today() -datetime.datetime(2021,1,1)
# print(_res + datetime.timedelta(1))

#---------------------7

today = datetime.datetime(2021, 3, 1)
print(today.strftime("%B %e, %y"))