a, b = map(int, input().split())
a, b = (a+b)/2, (a*b)**0.5
print('>') if a>b else print('<') if a<b else print('=')
