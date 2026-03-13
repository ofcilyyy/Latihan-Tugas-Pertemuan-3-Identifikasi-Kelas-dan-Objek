# KELAS RESTORAN
# ==============================
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Restoran ini bernama {self.restaurant_name} " 
              f"dan menyajikan masakan {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} sudah buka!\n")

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, additional):
        self.number_served += additional
        print(f"Jumlah pelanggan bertambah menjadi {additional} pelanggan. Total pelanggan sekarang {self.number_served}.")

# INSTANCE 
# ==============================
restaurant = Restaurant("Pagi Sore", "Padang, Indonesia")

print("--- NAMA RESTORAN ---") # >>> mencetak atribut secara terpisah
print("Nama Restoran:", restaurant.restaurant_name)
print("Jenis Masakan:", restaurant.cuisine_type)

# MEMANGGIL METODE 
# ==============================
restaurant.describe_restaurant()
restaurant.open_restaurant()

# MENCETAK JUMLAH PELANGGAN AWAL
# ==============================
print("Jumlah pelanggan yang dilayani:", restaurant.number_served)

# MENGUBAH JUMLAH PELANGGAN
# ==============================
restaurant.number_served = 20
print("Jumlah pelanggan yang telah dilayani sekarang:", restaurant.number_served)

# MENAMBAH JUMLAH PELANGGAN
# ==============================
restaurant.increment_number_served(15)

