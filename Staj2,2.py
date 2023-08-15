"""
string parametre alip her iki tek sayı arasına tire ('-') ekle
Örn: parametre 454793 ise çıktı 4547-9-3 olmalıdır. Sıfırı tek sayı olarak sayma"""
"""
def add_dash_between_odd_digits(number_str):
    result = []
    prev_odd = False # önceki karakter tek mi 
    
    for digit in number_str:
        if digit.isdigit():
            if int(digit) % 2 == 1:
                if prev_odd:
                    result.append('-')
                result.append(digit)
                prev_odd = True
            else:
                result.append(digit)
                prev_odd = False
        else:
            result.append(digit)
            prev_odd = False
            
    return ''.join(result)

input_str = input("Bir sayı girin: ")
output_str = add_dash_between_odd_digits(input_str)
print("Sonuç:", output_str)
"""
# Aynı tip çift sayıların arasına (-) koyma örneği, 0 dahil edilmedi. 
def add_dash_between_even_digits(number_str):
    result = []
    prev_even = False

    for digit in number_str:
        if digit.isdigit():
            if digit != '0' and int(digit) % 2 == 0:
                if prev_even:
                    result.append('-')
                result.append(digit)
                prev_even = True
            else:
                result.append(digit)
                prev_even = False
        else:
            result.append(digit)
            prev_even = False
    return ''.join(result)

input_string = input("Sayı girin: ")
output_string = add_dash_between_even_digits(input_string)
print("Sonuç: ", output_string)
