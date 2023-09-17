a, b, c = map(float, input('Enter a b c coefficients separated by space: ').split())

d = b**2 - 4*a*c
if d > 0:
    x1, x2 = (-b + d**0.5) / (2*a), (-b - d**0.5) / (2*a)
    print(f'There are two solutions: {x1=: .3f}; {x2=: .3f}')
elif d == 0:
    x = -b / (2*a)
    print(f'There is one solution: {x=: .3f}')
else:
    print('There are no solutions')