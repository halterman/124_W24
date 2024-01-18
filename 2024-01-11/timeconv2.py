total_seconds = int(input('Please enter total seconds: '))

hours = total_seconds // 3600
# total_seconds = total_seconds % 3600
total_seconds %= 3600

minutes = total_seconds // 60
total_seconds = total_seconds % 60

print('hours =', hours)
print('minutes =', minutes)
print('seconds =', total_seconds)
