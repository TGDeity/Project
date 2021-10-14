import time
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
time.sleep(7)

