# bölüm 1 veri tipleri
#soru1
isim = input("Adınızı giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
boy = float(input("Boyunuzu giriniz: "))
print("Adınız:", isim)
print("Yaşınız:", yas)
print("Boyunuz:", boy)

#soru2
not_mat=int(input("matematik notunuzu giriniz:"))
not_fizik=int(input("fizik notunuzu giriniz:"))
not_kimya=int(input("kimya notunuzu giriniz:"))
ort=float((not_mat+not_fizik+not_kimya)/3)
print("ortalamnız:",ort)

#soru3
str="tahire gulnur turanlı"
print("uzunluk:",len(str))
print("ilk harf:",str[0],"son harf:",str[20])
tersi=str[::-1]
print(tersi)

#bölüm 2 operatörler

#soru4
sayi1=int(input("lütfen 1. sayıyı giriniz:"))
sayi2=int(input("lütfen 2. sayıyı giriniz:"))
toplam=sayi1+sayi2
print("toplam:",toplam)
fark=sayi1-sayi2
print("fark:",fark)
çarpım=sayi1*sayi2
print("çarpım:",çarpım)
bölüm=sayi1/sayi2
print("bölüm:",bölüm)
kalan=sayi1%sayi2
print("mod:",kalan)

#soru5
ort=float(input("lütfen not ortalamanızı giriniz:"))
ort==(ort>=50) and ort!=(ort<50)
print("geçtiniz")
ort!=(ort>50) and ort==(ort<50)
print("kaldınız")

#soru6
yas=int(input("lütfen yaşınızı giriniz:"))
print((yas>=18) and "ehliyet alabilirsiniz" or (yas<18) and "ehliyet alamazsınız")

#soru7
fiyat=float(input("lütfen alışveris tutarını giriniz:"))
indirim=int(input("lütfen indirim oranını giriniz:"))
indirim_fiyat=fiyat-(fiyat*indirim/100)
print("indirimli fiyat:",indirim_fiyat)

#soru8
p=True
q=False
print(p and q)
print(p or q)
print(not p)
print(not q)
print(p and not q)
print(q or not p)

#mini proje

#soru9
fiyat1=float(input("1. ürün fiyatı:"))
fiyat2=float(input("2. ürün fiyatı:"))
fiyat3=float(input("3. ürün fiyatı:"))
toplam= fiyat1+fiyat2+fiyat3
indirimli_fiyat=toplam-toplam*0.1
print(toplam>200 and "yüzde 10 indirim kazandınız, güncel fiyat:",indirimli_fiyat)
print(toplam<=200 and "indirimli fiyat uygulanamadı.",toplam)

#soru10
dogum_yili=int(input("doğduğunuz yılı giriniz:"))
güncel_yil=int(input("şu an olduğunuz yılı giriniz:"))
yas=güncel_yil-dogum_yili
mesaj = ("Çocuksunuz" * (yas >= 0 and yas <= 12) +
         "Ergensiniz" * (yas >= 13 and yas <= 17) +
         "Yetişkinsiniz" * (yas >= 18))

print(mesaj)



