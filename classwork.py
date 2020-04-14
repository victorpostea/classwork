#2

name = input('Hey! What''s your name?: ')
print(f'Hi {name}, how''s it going?')

#3

width = int(input('What''s the width?: '))
length = int(input('What''s the length?: '))
print(f'The area is {(width) * (length)} units^2')

#6

price = int(input('How much did your meal cost?:'))
Tax = int(1.13 * price)
Tip = int(0.18 * price)

print(f'Tax: ${Tax}')
print(f'Tip: ${Tip}')
print(f'Total: ${Tax + Tip}')

#7

n = int(input())
total = 0
for i in range(1,n - 1):
    total += n

print(total)

# 18

radius = int(input())
height = int(input())
volume = str(3.14 * (radius ** 2) * height)
print(volume[0:6])

# 34

n = int(input())
if n % 2 == 0:
    print('Even')
else:
    print('Odd')

# 35

years = int(input())
if years < 0:
    print('Error')
elif years <= 2:
    print(10.5 * years)
else:
    print((10.5 * 2) + ((years - 2) * 4))

# 37

sides = int(input('Number of sides: '))
if sides <= 2:
    print(f'Error. No shape with {sides} side(s)')
elif sides > 10:
    print(f'Eror, this program is not designed to go up to {sides} sides')
elif sides == 3:
    print('Triangle')
elif sides == 4:
    print('Square')
elif sides == 5:
    print('Pentagon')
elif sides == 6:
    print('Hexagon')
elif sides == 7:
    print('Septagon')
elif sides == 8:
    print('Octagon')
elif sides == 9:
    print ('Nonagon')
elif sides == 10:
    print ('Decagon')

# 36

n = input()
if n == 'a' or n == 'e' or n== 'i' or n== 'o' or n== 'u':
    print('Vowel')
elif n == 'y':
    print('Sometimes Vowel')
else:
    print('Consonant')

# 38

month = input()
if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print('31 Days')
elif month == 'Feburary':
    print('28 or 29 days')
else:
    print('30 days')

# 63

i = 0 
total = 0
print('Farenheit, Celcius')
while i < 16:
    i += 1 
    total += 5 
    print('  ', total, '      ' , int(((total-32) * 5) / 9))

# 62

discount = 0.6
originalprice = [4.95, 9.95, 14.95, 19.95, 24.95]
for i in range(0,5):
    print (originalprice[i], str(int(discount * 100)) + '%', round(discount * originalprice[i], 2))

# 67

total = 0
while True:             
    age = input()
    if age == '':       
        break
    elif 3 <= int(age) <= 12:
        total += 14.00
    elif 13 <= int(age) <= 64:
        total += 23.00
    elif int(age) >= 65:
        total += 18.00

print(total)

# 81

import math
side1 = int(input())
side2 = int(input())

side3 = math.sqrt(side1 ** 2 + side2 ** 2)
print(side3)

# 82

def taxi_fare(km_travelled):
    meters_travelled = 1000 * km_travelled 
    cost_per_140_meters = 0.25
    base_fare = 4
    return (base_fare + ((meters_travelled / 140) * cost_per_140_meters))
