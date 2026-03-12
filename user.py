# KELAS USER
# ==============================

class User:
    def __init__(self, first_name, last_name, age, city, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")
        print(f"Usia        : {self.age}")
        print(f"Asal        : {self.city}")

    def greet_user(self):
        print(f"Halo {self.first_name}, selamat menikmati perjalanan!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        # print(f"Nilai login bertambah {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Nilai login telah direset")

# INSTANCE 
# ==============================
user1 = User("Tan", "Malaka", 51, "Sumatera Barat")
user2 = User("Pramoedya", "Ananta Toer", 60, "Jawa Tengah")
user3 = User("Biru Laut", "Wibisana", 20, "Yogyakarta")

for u in (user1, user2, user3):
    u.describe_user()
    u.greet_user()

# MEMANGGIL INCREMENT LOGIN ATTEMPTS
# ==============================
u.increment_login_attempts()
u.increment_login_attempts()
u.increment_login_attempts()

# MENCETAK NILAI LOGIN ATTEMPTS
# ==============================
print(f"Nilai login saat ini: {u.login_attempts}")

# MEMANGGIL RESET LOGIN ATTEMPTS
# ==============================
u.reset_login_attempts()
print(f"Nilai login setelah reset: {u.login_attempts}")
