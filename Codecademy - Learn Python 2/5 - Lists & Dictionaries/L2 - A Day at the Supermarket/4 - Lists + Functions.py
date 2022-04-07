# Write your function below!
def fizz_count(x):
  count = 0
  for n in x:
    if n == "fizz":
      count += 1
  return count