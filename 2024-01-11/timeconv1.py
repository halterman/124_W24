hours = int(input('Please enter hours: '))
minutes = int(input('Please enter minutes: '))
seconds = int(input('Please enter seconds: '))

print('hours =', hours)
print('minutes =', minutes)
print('seconds =', seconds)

total_seconds = 3600*hours + 60*minutes + seconds

print(f'The total number of seconds equals {total_seconds:,}')