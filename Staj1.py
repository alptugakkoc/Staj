
# 2000 ile 3200 arasında 7 ile bölünebilen ancak 5'in katı 
# olmayan tüm sayıları bulan bir program yazın

""" for num in range (2000,3201):
    if num %7 == 0 and num %5 !=0:
        print(num) """


# a. Verilen sayının faktöriyelini hesaplayan iteratif (for-loop kullanan) bir program yazınız.
#  Sonuçlar, tek bir satırda virgülle ayrılmış bir sırayla yazdırılmalıdır.

#Programa aşağıdaki girdinin sağlandığını varsayalım: 8 O zaman çıktı şöyle olmalıdır: 40320

#b. Recursive Yaz

# a
"""def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Sayi Giriniz: "))
result = factorial_iterative(number)
print(result)"""

# b 
# Recursive  olarak yazıldı
"""def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı girin: "))
result= factorial(number)
print(f"{number} factorial: {result}")"""

#Kullanıcının verdıgı parolaya kontrollü yapan bir program:
#Büyük harf icermelidir.
#En az bir sayı içermelidir.
#Bir noktalama işareti veya matematiksel sembol içermelidir.
#Dizede "parola" kelimesi olamaz.
#7 karakterden uzun 31 karakterden kısa olmalıdır.

import re 
def check_password(password):
    return(
    7<= len(password)<=31 and
    "parola" not in password and 
    any(char.isupper()for char in password )and
    any(char.isdigit() for char in password )and
    any(char in "!@#$%^&*()_-+=<>?/." for char in password)
    )

password = input ("Enter Your Password: ")
if check_password(password):
    print("You're entered a valid password ")
else:
    print("You're entered a invalid password ")
