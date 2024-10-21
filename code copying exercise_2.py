birth_year, birth_month, birth_date = [int(x) for x in input().split('.')]
now_year, now_month, now_date = [int(x) for x in input().split('.')]

delta_year = now_year - birth_year
if birth_month > now_month or (birth_month == now_month and birth_date > now_date):
    delta_year -= 1

print(delta_year)

