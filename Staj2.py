import re

def validate_name(name):
    name_pattern = r'^[A-Z][a-z]*$'
    return re.match(name_pattern, name)

def validate_surname(surname):
    surname_pattern = r'^[A-Z]+$'
    return re.match(surname_pattern, surname)

def validate_middle_name(middle_name):
    if middle_name == '':
        return True
    middle_name_pattern = r'^[A-Z][a-z]*$'
    return re.match(middle_name_pattern, middle_name)

def validate_input(input_str):
    parts = input_str.split()
    if len(parts) < 2 or len(parts) > 3:
        return False
    
    first_name = parts[0]
    last_name = parts[1]
    middle_name = '' if len(parts) == 2 else parts[2]
    
    if not (validate_name(first_name) and validate_surname(last_name) and validate_middle_name(middle_name)):
        return False
    
    return True

input_name = input("Lutfen isim-soyisim bilgisini girin: ")
if validate_input(input_name):
    print("Gecerli bir isim-soyisim girildi.")
else:
    print("Gecerli bir isim-soyisim girilmedi.")
