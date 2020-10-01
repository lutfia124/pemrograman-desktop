a = int(input("berapa banyak angka yang anda masukkaan :"))
List = []
for i in range(a):
    angka = int(input("masukkan angka ke{} :".format(i)))
    List.append(angka)
print(List)
print("nilai maksimal adalah : {}".format(max(List)))
print("nilai minimal adalah : {}".format(min(List)))


