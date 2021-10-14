import time
print("Merhaba vizeni hesaplamak istiyorum lütfen bilgilerini girer misin")
ad= input("Adın nedir: ")
print("Hoşgeldin ",ad)
vize1=int(input("1.Vize Notunu girer misin: "))
vize2=int(input("2.Vize Notunu girer misin: "))
vizeort = (vize1+vize2)/2
final=int(input("Final Notunu girer misin :"))
ödevnotu=int(input("Ödev Notunu girer misin :"))
yoklama=int(input("Lütfen yoklama notunuzu giriniz (1-100) :"))
basarinotu=((vizeort/100)*25+(yoklama/100)*5+(ödevnotu/100)*10+(final/100)*60)
b = basarinotu
if b>=92.5:
    print("Başari Notunuz",b, 'A Geçtiniz.')
elif b>=82.5:
    print("Başari Notunuz",b,"A- Geçtiniz.")
elif b>=75:
    print("Başari Notunuz",b,"B+ Geçtiniz.")
elif b>=67:
    print("Başari Notunuz",b, "B Geçtiniz.")
elif b>=57.5:
    print("Başari Notunuz",b, "B- Geçtiniz.")
elif b==50:
    print("Başari Notunuz",b, "C+ Geçtiniz.")
elif b>=42.5:
    print("Başari Notunuz",b, "C Şartlı başarılı geçtiniz.")
elif b>=32.5:
    print("Başari Notunuz",b, "C- Şartlı başarılı geçtiniz.")
elif b>=25:
    print("Başari Notunuz",b, "D+ Şartlı başarılı geçtiniz.")
elif b>=17.5:
    print("Başari Notunuz",b, "D- Şartlı başarılı geçtiniz.")
elif b>=0:
    print("Başari notunuz F Kaldınız")

time.sleep(7)


