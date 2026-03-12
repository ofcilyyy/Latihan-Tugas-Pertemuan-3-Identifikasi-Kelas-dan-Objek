from restaurant import Restaurant

restaurant1 = Restaurant("Ichiban Sushi", "Jepang")
restaurant2 = Restaurant("La Pergola", "Italia")
restaurant3 = Restaurant("Tacitos", "Mexico")

for r in (restaurant1, restaurant2, restaurant3):
    r.describe_restaurant()
