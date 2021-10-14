"""while True:
    s=1
    while s<=10:
        print(s)
        s+=1
    c =(input("Çıkış için X girin"))
    if c=="x":
        print("program sonlandı")
        break

"""# Bir şeyler belli değil ise while komutu kullanıyoruz
"""
for s in range(10,0,-2):
    print(s)
for harf in("speCtra"):
    print(harf)
"""
adsoyad = input("Adınızı soyadınızı girer misiniz: ")
print("Hoşgeldin" ,adsoyad)
calisilangün =int(input("Kaç gün çalıştın"))
günlükücret = int(input("günlük ücretiniz nedir?: "))
brüt = calisilangün*günlükücret
fazlamesai = int(input("Kaç gün fazla mesai yaptınız?: "))
fazlamesaic =(günlükücret*1.5*fazlamesai)
damgavergisi = brüt*(0.004)
gelirvergisi = brüt%25
sgkkesintisi = brüt%14
kesintitoplami = damgavergisi+gelirvergisi+sgkkesintisi
netücret = brüt-kesintitoplami+fazlamesaic
print("Bu Ay ki Net ücretiniz")
print(netücret)


