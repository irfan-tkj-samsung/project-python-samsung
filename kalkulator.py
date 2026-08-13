import os
import math
import sys

class Kalkuator:
    def __init__(self, nama_user):
        self.nama_user = str(nama_user).strip().title()
        self.history = []
        self.hasil_kalkulasi = 0.0

    def tampilkan_menu(self):
        print(f"\n{'='*40}")
        print(f"   Kalkulator Ajin - {self.nama_user}")
        print(f"{'='*40}")
        print("1. TAMBAH (+)")
        print("2. KURANG (-)")
        print("3. KALI (*)")
        print("4. BAGI (/)")
        print("5. PANGKAT (^)")
        print("6. MODULUS (%)")
        print("7. HISTORY")
        print("8. DELETE HISTORY")
        print("0. KELUAR")
        print(f"{'='*40}")

    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            return "Error: Pembagian dengan nol!"
        return a / b

    def pangkat(self, a, b):
        return a ** b

    def modulus(self, a, b):
        if b == 0:
            return "Error: Modulus dengan nol!"
        return a % b

    def catat_history(self, operasi, hasil):
        self.history.append(f"{operasi} = {hasil}")

    def show_history(self):
        if len(self.history) == 0:
            print("\nBELUM ADA HISTORY")
        else:
            print("\nHISTORY KALKULASI")
            print("-" * 30)
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
            print("-" * 30)

    def delete_history(self):
        self.history.clear()
        print("\nHISTORY BERHASIL DIHAPUS")

    def ambil_input_angka(self, pesan):
        while True:
            try:
                val = float(input(pesan))
                return val
            except ValueError:
                print("Input tidak valid! Masukkan angka yang benar.")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("PILIH MENU (0-8): ").strip()

            if pilihan == "0":
                print(f"\nTERIMAKASIH SUDAH MENGGUNAKAN SAYA, {self.nama_user.upper()}!")
                sys.exit()

            elif pilihan in ["1", "2", "3", "4", "5", "6"]:
                num1 = self.ambil_input_angka("Masukkan angka pertama: ")
                num2 = self.ambil_input_angka("Masukkan angka kedua  : ")

                if pilihan == "1":
                    hasil = self.tambah(num1, num2)
                    op = f"{num1} + {num2}"
                elif pilihan == "2":
                    hasil = self.kurang(num1, num2)
                    op = f"{num1} - {num2}"
                elif pilihan == "3":
                    hasil = self.kali(num1, num2)
                    op = f"{num1} * {num2}"
                elif pilihan == "4":
                    hasil = self.bagi(num1, num2)
                    op = f"{num1} / {num2}"
                elif pilihan == "5":
                    hasil = self.pangkat(num1, num2)
                    op = f"{num1} ^ {num2}"
                elif pilihan == "6":
                    hasil = self.modulus(num1, num2)
                    op = f"{num1} % {num2}"

                print(f"\nHASIL: {hasil}")
                if not isinstance(hasil, str):
                    self.catat_history(op, hasil)

                input("\nTEKAN ENTER UNTUK KEMBALI...")

            elif pilihan == "7":
                self.show_history()
                input("\nTEKAN ENTER UNTUK KEMBALI...")

            elif pilihan == "8":
                self.delete_history()
                input("\nTEKAN ENTER UNTUK KEMBALI...")

            else:
                print("\nPilihan menu tidak valid!")
                input("\nTEKAN ENTER UNTUK KEMBALI...")


def main():
    nama = input("Masukkan Nama Anda: ")
    app = Kalkuator(nama)
    app.jalankan()

if __name__ == "__main__":
    main()