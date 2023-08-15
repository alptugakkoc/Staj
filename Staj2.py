#Regex kullanımı
# findall > Liste döndürmek
# search > true ya da false döndürür
# split > stringi bölüyor
# sub > kelimeyi yer değiştirmek

"""
Python Regex ile isim göbek adı soy isim kontrol eden bir program yaz:
İsimin ilk harfi büyük olacak
Soy isim hep büyük harf olacak
isim ve soy isim zorunlu olacak
Göbek adı opsiyonel olacak fakat eğer var ise ilk harfi büyük olacak
"""

import re

def valid_name(name):
    return name and name[0].isupper() and name[1:]. islower()

def valid_surname(surname):
    return surname and surname.isupper()

def main():
    print("İsim bilgileri: ")

    while True:
        first_name = input("İsim: ")
        middle_name = input("Göbek adı(Boş bırakabilirsiniz: )")
        last_name = input("Soyisim: ")

        if(
            valid_name(first_name) and
            (not middle_name or valid_name(middle_name))
            and valid_surname(last_name)
        ):
            print("Bilgiler geçerli. ")
            break
        else:
            print("Bilgiler geçersiz. ")

if __name__ =="__main__":
    main()

