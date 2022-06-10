import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
jst_datetime = datetime.datetime(2021, 11, 16, 12, 34, 56, tzinfo=JST)
naive_datetime = datetime.datetime.now()
print(repr(jst_datetime))