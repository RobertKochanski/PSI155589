from datetime import datetime


print('{:_<10}'.format("text"))
print('{:>10}'.format("text"))
print('{:+d}'.format(42))

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))

print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))