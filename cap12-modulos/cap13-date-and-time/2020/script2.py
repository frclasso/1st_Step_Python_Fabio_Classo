import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
# 1
print(my_date)

# 2
data_formatada = '{: %B %d, %Y}'.format(my_date)
print(data_formatada)

# 3
# March 01, 2016 fell on Tuesday and was 061 day of the year
sentence2 ='{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence2)