'''x = 3
y = 5
z = x + y
print(f"{x} + {y} = {z}")

z = x - y
print(f"{x} - {y} = {z}")

z = x * y
print(f"{x} * {y} = {z}")

z = x / y
print(f"{x} / {y} = {z}")

z = x ** y
print(f"{x} ** {y} = {z}")

z = x // y
print(f"{x} // {y} = {z}")

z = int(x / y)
print(f"int({x} / {y}) = {z}")
'''

x = 5
y = 3

# x / y = 1r2

print(x < y)
print(x > y)
print(x == y)
print(x != y)
print(x <= y)
print(x >= y)

z = not(x < y) and x == 5

is_noon = False
is_morning = False
is_hungry = True

is_lunch_time = is_noon and is_hungry
is_breakfast_time = is_morning and is_hungry

is_dinner_time = not(is_lunch_time and is_breakfast_time)



print(is_noon and is_hungry)
print(is_noon or is_hungry)
print(not is_hungry)

print(not(is_noon and is_hungry) or is_noon)