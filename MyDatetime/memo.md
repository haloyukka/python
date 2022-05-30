# ［解決！Python］datetime型の日付や時刻と、ISO 8601形式の文字列とを相互変換するには

https://atmarkit.itmedia.co.jp/ait/articles/2111/16/news019.html#_ga=2.130049096.656205166.1640609304-547168494.1627694563

```Python
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
jst_datetime = datetime.datetime(2021, 11, 16, 12, 34, 56, tzinfo=JST)
naive_datetime = datetime.datetime.now()
print(repr(jst_datetime))
#出力例：
#datetime.datetime(2021, 11, 16, 12, 34, 56, tzinfo=datetime.timezone(datetime.
#timedelta(seconds=32400), 'JST'))

print(f'jst: {jst_datetime}, timezone: {jst_datetime.tzname()}')  #
print(f'naive: {naive_datetime}, timezone: {naive_datetime.tzname()}')
# 出力例
#jst: 2021-11-16 12:34:56+09:00, timezone: JST
#naive: 2021-11-12 13:36:27.275913, timezone: None

# 日付と時刻をISOフォーマットに書式化
jst_date = jst_datetime.isoformat()
naive_date = naive_datetime.isoformat()
print(jst_date)  # 2021-11-16T12:34:56+09:00
print(naive_date)  # 2021-11-12T13:36:27.275913

# 日付と時刻をISOフォーマットで書式化（時刻の要素として含めるものを指定）
jst_dt = jst_datetime.isoformat(timespec='minutes')
print(jst_dt)
naive_dt = naive_datetime.isoformat(timespec='seconds')
print(naive_dt)

# ISOフォーマットからdatetime.datetimeインスタンスを生成
mydatetime = datetime.datetime.fromisoformat(jst_dt)
print(repr(mydatetime))
# 出力結果：
#datetime.datetime(2021, 11, 16, 12, 34, tzinfo=datetime.timezone(datetime.
#timedelta(seconds=32400)))

mydatetime = datetime.datetime.fromisoformat(naive_dt)
print(repr(mydatetime))
# 出力結果：
#datetime.datetime(2021, 11, 12, 13, 36, 27)
```

```Python
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
jst_datetime = datetime.datetime(2021, 11, 16, 12, 34, 56, tzinfo=JST)
naive_datetime = datetime.datetime.now()
print(repr(jst_datetime))
#出力例：
#datetime.datetime(2021, 11, 16, 12, 34, 56, tzinfo=datetime.timezone(datetime.
#timedelta(seconds=32400), 'JST'))

print(f'jst: {jst_datetime}, timezone: {jst_datetime.tzname()}')  #
print(f'naive: {naive_datetime}, timezone: {naive_datetime.tzname()}')
# 出力例
#jst: 2021-11-16 12:34:56+09:00, timezone: JST
#naive: 2021-11-12 13:36:27.275913, timezone: None
```

```Python
jst_dt = jst_datetime.isoformat()
naive_dt = naive_datetime.isoformat()
print(jst_dt)  # 2021-11-16T12:34:56+09:00
print(naive_dt)  # 2021-11-12T13:36:27.275913
```

```Python
jst_dt = jst_datetime.isoformat(timespec='minutes')
print(jst_dt)  # 2021-11-16T12:34+09:00
naive_dt = naive_datetime.isoformat(timespec='seconds')
print(naive_dt)  # 2021-11-12T13:36:27
```

```Python
mydatetime = datetime.datetime.fromisoformat(jst_dt)
print(repr(mydatetime))
# 出力結果：
#datetime.datetime(2021, 11, 16, 12, 34, tzinfo=datetime.timezone(datetime.
#timedelta(seconds=32400)))
print(mydatetime)  # 2021-11-16 12:34:00+09:00

mydatetime = datetime.datetime.fromisoformat(naive_dt)
print(repr(mydatetime))
# 出力結果：
#datetime.datetime(2021, 11, 12, 13, 36, 27)
```

```Python
mydatetime = datetime.datetime.fromisoformat('2022-01-01')  # OK
print(mydatetime)  # 2022-01-01 00:00:00
mydatetime = datetime.datetime.fromisoformat('12:34:56')  # ValueError
```

```Python
mydate = datetime.date.fromisoformat('2021-11-22')
print(mydate)  # 2021-11-22
mydate = datetime.date.fromisoformat('2021-11-22T00:11:22')  # ValueError

mytime = datetime.time.fromisoformat('12:34:56')
print(mytime)  # 12:34:56
mytime = datetime.time.fromisoformat('2021-11-22T01:23:45')  # ValueError
```
