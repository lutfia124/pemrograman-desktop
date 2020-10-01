username = "nama saya"
password = 123456

a = 1
while a <= 3:
    b = str(input("masukkan username :"))
    c = int(input("Masukkan password : "))
    if b == username and c == password:
        print ("anda berhasil masuk")
        break
    else:
        print ("maaf username dan password anda salah")
    a = a+1
if a == 4:
    print ("anda terblokir")
