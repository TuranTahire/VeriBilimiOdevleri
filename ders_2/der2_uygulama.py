#üyelik operatörleri
from unittest import case


fruits=['Elma','Armut','Kiraz','Portakal','Vişne','Kayısı']
var_mi='Elma' in fruits
print(var_mi)
yok_mu= 'Kayısı' not in fruits
print(yok_mu)

a1= '25'
print(type(a1))

a1_int=int(a1)
print(type(a1_int))

print(bool(0))
print(bool(1))

print(bool(''))
print(bool('Selam'))

veri= 'SELAM BEN ÖMER'
liste1=list(veri)
print(liste1)

age=int(input('lütfen yaşınızı giriniz:'))
if age>=18:
    print("reşitsiniz. ehliyet alabilirsiniz.")
else:
    print("reşit değilsiniz,ehliyet alamazsınız.")

sayi1=int(input("lütfen bir sayı giriniz:"))
if sayi1>0:
    print("girmiş olduğunuz sayı pozitiftir.",sayi1)
elif sayi1==0:
    print("girmiş olduğunuz sayı sıfırdır.")
else:
    print("girmiş olduğunuz sayı negatifitir.")

sayi2 = int(input("lütfen bir sayı giriniz:"))

if sayi2>10:
    print("sayı 10dan büyük.")
    if sayi2>15:
     print("sayi değeri 15ten büyüktür")


# ternary if
yas=46
mesaj= "reşitsiniz ehliyet alınır" if yas>=18 else 'reşit değilsiiz.'
print(mesaj)

#match-case
gun=int(input("lütfen 1 ile 7 arasında bir rakm giriniz: "))
gun_adi= None
match gun: 
 case 1:
      gun_adi="pazartesi"
 case 2:
      gun_adi= "salı"
 case 3:
        gun_adi="çarşamba"  
 case 4:
        gun_adi="perşembe"
 case 5: 
        gun_adi="cuma" 
 case 6:
        gun_adi="cuamretsi" 
 case 7:
        gun_adi= "pazar" 
 case __:
          gun_adi= "geçersiz karakter girdiniz." 

print(gun_adi)

# 1-7 ile arası rakam haftaiçi mi oksa hafta sonu mu?
hafta=int(input("lütfwn 1 ile 7 arasında bir rakam giriniz:"))
hafta_adi= None
match hafta:
     case 1|2|3|4|5:
          hafta_adi =" hafta içi"
     case 6|7:
          hafta_Adi= "hafta sonu"
     case __:
          hafta_adi =" geçersiz rakam girdiniz!"


#dögüler:tekrarlı işlemlerde kullanılır.

for i in range(6):
  print("merhaba")

#1 de 20ye kadar tüm sayıları ekran çıktısı olarak giriniz.
for i in range(1,21,2):
    print(i)   

#1den 10a kadar tüm sayıları çift mi tek mi kontrol et 
for i in range(1,11):
     if i%2==0:
          print("cift sayı:",i)
     else:
          print("tek sayı",i)

for i in range(100,-1,5):
     print(i)



 

cities=["istanbul","ankara","izmir","bursa","çanakkale"]
for city in cities:
     print(city)
     




#enumarate
for index,value in enumerate(cities):
     print(index+1,". şehir",value)

#değer üretmeyen fonksiyonlar
#fonksiyon tanımlama
def hello_world(): #tanımlama
 print("merhabalar")
hello_world()#çağırma

def info(name):
     print("hoşgeldin", name)
info("ömer")
info(1)

def person_info(name,surname="doğan"):
     print(f"merhaba benim adım {name}, soyadım{surname}")
person_info("buse"," doğan")

a:int=5
print(type(a))
def toplam(num1:float,num2:float):
     print(num1+num2)
toplam(25,37)

#args
def carpim(*sayi):
     carpim=1
     for num in sayi:
          carpim*= num
     print(carpim)
carpim(1,78,2)


my_list=[1,2,3,4]
my_tuple=(1,2,3,4)
my_list.append("yeni veri")

#tuple is an immutable data type.
renkler=("kirmizi","sarı","siyah")
print(renkler)
#dividing tuples
red,yellow,bl =("kirmizi","sarı","siyah")
print(red)

#code-review 
#mini proje

adet = int(input("lütfen kaç adet meyve alacağınızı belirtiniz:"))
meyve_adlari=list()
birims= []
kgs=list()

for i in range(1,adet+1):
     meyve_adi=input(f'{i}.meyvenin adını giriniz:')
     birim=int(input(f'{i}. meyvenin birim fiyatını  giriniz:'))
     kg=int(input(f"{i}. meyvenin kilogramını giriniz:"))

     meyve_adlari.append(meyve_adi)
     birims.append(birim)
     kgs.append(kg)

for i in range(adet):
    
    print(f"meyve adi: {meyve_adlari[i]}, birim fiyatı:{birims[i]}₺, kilogram:{kgs[i]}kg")

kdvsiz_toplam_tutar=0
kdvli_toplam_tutar=0
kdvsiz_liste=list()
kdvli_liste=list()
print("meyve toplam tutarlari")     
for i in range(adet):
    toplam_fiyat=birims[i]*kgs[i]
    kdvli_toplam=toplam_fiyat*(1.2)
    kdvli_liste.append(kdvli_toplam)
    kdvsiz_liste.append(toplam_fiyat)
    kdvsiz_toplam_tutar+=toplam_fiyat
    kdvli_toplam_tutar+=kdvli_toplam
    print(f"meyve adi: {meyve_adlari[i]}, birim fiyatı:{birims[i]}₺, kilogram:{kgs[i]}kg, toplam tutar(kdvsiz):{kdvsiz_liste[i]}₺, toplam(kdvli):{kdvli_liste[i]}")

print(f"kdvsiz toplam tutar :{kdvsiz_toplam_tutar}") 
print(f"kdvli tutar:{kdvli_toplam_tutar}")  


#max ,min -listeler,str,dics,

