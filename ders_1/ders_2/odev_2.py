#Hedef
# • Koşullu durumları (if/elif/else) uygulamak
# • Döngüler (for, while) ile veri işlemek
# • String metotları ve listeler üzerinde alıştırmalar yapmak
# • Temel veri işleme becerilerini geliştirmek

#soru 1 sayı analizi
sayi=int(input("lütfen bir sayı giriniz:"))
if sayi<0 and sayi%2==0:
    print("negatif çift")
elif sayi<0 and sayi%2!=0:
    print("negatif tek")
elif sayi>0 and sayi%2==0:
    print("pozitif çift")
elif sayi>0 and sayi%2!=0:
    print("pozitif tek")
else:
    print("sıfır")

#soru2 harf frekansı
kelime=input("lütfen bir kelime giriniz:")
frekans={}
for harf in kelime:
    if harf in frekans:
        frekans[harf]+=1
    else:
        frekans[harf]=1

print(frekans)

#soru3 şifre kontrolü
password = input("Şifre giriniz: ")

length_ok = len(password) >= 8
upper_ok = any(char.isupper() for char in password)
digit_ok = any(char.isdigit() for char in password)

if length_ok and upper_ok and digit_ok:
    print("Şifre başarılı! Tüm koşullar sağlandı.")
else:
    print("Hata! Şifre en az 8 karakter, en az 1 büyük harf ve en az 1 rakam içermeli.")


#soru4
total=0
numbers=[12,4,9,25,30,7,18]
total_elements = len(numbers)
for i in numbers:
    total +=i
print(total,total_elements)
avr=total/total_elements
print(avr)

big_numbers=list()
for i in numbers:
    if i>avr:
        big_numbers.append(i)
print(big_numbers)


#soru5
for i in range(1,6):
   print("*"*i)


#soru6
numbers=[]
total=0
number=int(input("please neter a number:"))
while number!=0:
    numbers.append(number)
    print(number)
    number=int(input("please neter a number:"))
print(numbers)
total_numbers=len(numbers)

for i in numbers:
    total+=i
print(total)
avr=total/total_numbers
print(avr)

#soru 7
word=input("please enter a word:")
reverse_word=word[::-1]
if word==reverse_word:
 print(word +" is a palindrome word!")
else:
 print(word + " is not a palindrome word!")

soru8
numbers=[]
for i in range(1,101):
    if i%3==0 and i%5==0:
        numbers.append(i**2)
print(numbers)

#soru9
sentence=input("please enter a senctece:")
the_words=sentence.split()
new_words=[]
for word in the_words:
    new_words.append(word.capitalize())
    new_sentence= " ".join(new_words)
print(new_sentence)

#soru10
#mini proje- film yorum analizi
comments = input("Please enter your comments (separate multiple comments with ';'): ").split(';')
lengths = []
good_count = 0

for comment in comments:
    comment = comment.strip()
    lengths.append(len(comment))
    if "good" in comment:
        good_count += 1

longest = max(comments, key=len)
shortest = min(comments, key=len)
average = sum(lengths) / len(lengths)

print("Comments:", comments)
print("Length of each comment:", lengths)
print('Number of comments containing "good":', good_count)
print("Longest comment:", longest)
print("Shortest comment:", shortest)
print("Average comment length:", average)

		
		
		
		
		
		
		














    



        

