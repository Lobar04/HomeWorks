N = int(input())
def summ(b):
  a = [6,2,5,5,4,5,6,3,7,6]
  s = 0
  for i in str(b):
    s+=a[int(i)]
  return s
print(summ(N))
