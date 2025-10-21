import re

def validate_snils(snils: str) -> bool:
    # проверка формата СНИЛС
    SNILS_PATTERN = re.compile(r'^\d{3}-\d{3}-\d{3} \d{2}$')
    
    if not SNILS_PATTERN.match(snils):
        return False
    digits = re.sub(r'\D', '', snils)
    #проверка длины СНИЛС
    if len(digits) != 11:
        return False
    #проверка контрольной суммы
    number = digits[:9]
    control = int(digits[9:])
    total = sum(int(digit) * (9 - i) for i, digit in enumerate(number))
    
    if total < 100:
        expected = total
    elif total in (100, 101):
        expected = 0
    else:
        с = total % 101
        expected = с if с < 100 else 0
    
    if control==expected:
        return True
    else:
        return False
