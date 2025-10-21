from validate_snils import validate_snils


a = input('Введите номер СНИЛС: ')
if validate_snils(a):
    print('СНИЛС верный')
else:
    print('СНИЛС не верный')