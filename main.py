file = open ("N.txt", 'r')

min_days = 111111111111111111111
min_date = ""
for line in file.readlines():
    date = line.strip().split('-')
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    days = day + month * 30 + year*365
    if days < min_days:
        min_days = days
        min_date = line

print(min_date)
