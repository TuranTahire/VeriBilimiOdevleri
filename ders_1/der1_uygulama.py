print("merhabalar bugün ilk dersimiz")
print(147*852)
#merhaba nasılsın

#SOLID
#DRY- DON'T REPEAT YOURSELF
# DEĞİŞKEN OLUŞTURMA:değikene_takma_adı =değişkenin değeri
metin="galatasaray dün oynanan karagümrik maçında 3 0lık bir skor ile galip oldu."
print(metin)

sayi1=256
sayi2=147
carpim=sayi1*sayi2
print(carpim)

#str: metinsel ifadelere karşılık gelen veri tipidir.
#int: tam sayılara karşılık gelir.
print(type(carpim))


#float: ondalıklı sayılara karşılık gelen 
pi=3.14
yaricap= 12
# örnek bir yarıçap değeri atandı
cevre=2*pi*yaricap
print(cevre)

#complex: matematikteki karmaşık sayılara karşılık gelir.
z=2 +3j
print(z)
print(type(z))

#list: birden fazla veri grubu ile çalışmak istiyorsak list veri tipini kullanırız.
cities=['istabul','ankara','izmir','bursa']
plakalar=[34,6,35,16]
print(cities)
print(type(cities))

#cities listesi içerisindeki 2. eleman 
print(cities[1])

#bool: True veya False değeri aalır.
dogru=True
yanlis=False
print(dogru)
print(type(dogru))

#operatörler
#aritmetik operatörler
# +, -, *, /
# % mod alma
#** üs alma 
x=5
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

name= "Ömer Faruk"
surname= "Doğan"
full_name=name+surname #yanyana yazmada kullanlır.
print(full_name)

print(name*2)

#karşılaştırma operatörleri
#<,>,<=,>=
# == eşit midir.
#!= eşit değil mdir?
print(5<65)
print(25>140)
print(25>=25)
print(35<=34)
print(35!=35)
print(35==35)

print('Buse'=='Buse')
print('Buse'=='BUSE')
print('Evren' > 'Uzay') # ASCII



