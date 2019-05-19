def display(n):
  if n == 0:
    return 0
  display(n - 1)
  print(n)

n = 5
display(n)
