berat_badan = float(input("Masukkan berat badan anda = "))
tinggi_badan= float(input("Masukkan tinggi badan anda = "))
massIndex = berat_badan/((tinggi_badan/100)**2)
if massIndex < 18.5:
    print("Berat badan kurang")
elif 18.5 <= massIndex <= 22.9:
    print("Berat badan normal")
elif 23 <= massIndex <= 29.9:
    print("Berat badan berlebih")
elif massIndex > 30:
    print("Obesitas")
else:
    print("maaf inputan salah")
