from datetime import date, time, datetime, timedelta

date_obj = date(2020,10,9)
time_obj = time(15,23,21)
print("클래스의 속성 이용 {0}-{1}-{2}".format(date_obj.year, date_obj.month, date_obj.day))


date_obj_2 = date(2020,10,15)
diff_date = date_obj_2 - date_obj
print(diff_date)

# 날짜만 출력하려면
print("두 날짜의 차이 : {}일".format(diff_date.days))

# timedelta 객체 사용
date_org = date(2022, 5, 15)
date_result = date_org - timedelta(weeks=1)
print("지정 날짜 : {0}, 일주일 전 날짜 : {1}".format(date_org, date_result))

today = date.today()
now = datetime.now()
