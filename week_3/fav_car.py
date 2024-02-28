#description of my favorite car
#Date 28\02\24
#Name Abigael Mburu

G_wagon = {"model":"mercedes","color":"black","weight":"2560","year":"2022"}

print(G_wagon["model"])
print(G_wagon["color"])
print(G_wagon["weight"])
print(G_wagon["year"])

G_wagon["year"] = "2056"
G_wagon["color"] = "grey"
G_wagon["weight"] = "2667"
print(G_wagon)

bro_G_wagon = G_wagon.copy
print(G_wagon)
