#description of my laptop
#Date 28\02\24
#Name Abigael Mburu



laptop = {"make":"hp","color":"black grey","weight":"1.2","year":"2019"}

print(laptop["make"])
print(laptop["color"])
print(laptop["year"])

laptop["color"] = "red"
laptop["year"] = "2030"
laptop["size"] = "1200mm x 600mm"
print(laptop)

del laptop ["color"]

print(laptop)

siz_laptop = laptop.copy
print(laptop)

"""

for key , value in laptop.items():
    print(key)
    print("\n")
    print(value)

"""

