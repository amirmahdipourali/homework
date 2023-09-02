from datetime import*
today=datetime.today()
age_of_user_year=int(input('hi what is the year you were born: '))
age_of_user_month=int(input('hi what is the month you were born: '))
age_of_user_day=int(input('hi what is the day you were born: '))
days=(today.year-age_of_user_year)*365+(today.month-age_of_user_month)*30+today.day-age_of_user_day
weeks=days/7
weeks=round(weeks)
seconds=((days*24)*60)*60
print('you are',days,'old')
print('you are',weeks,'old')
print('you are',seconds,'old')