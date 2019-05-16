car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
res = list(car.items())
print(res)

x = [x for x,y  in res if y == "Ford"]
print(x)