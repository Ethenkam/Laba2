import re
import urllib.request
import urllib.error


def validate_snils(snils: str) -> bool:
    # проверка формата СНИЛС
    SNILS_PATTERN = re.compile(r'^\d{3}-\d{3}-\d{3} \d{2}$')

    if not SNILS_PATTERN.match(snils):
        return False
    digits = re.sub(r'\D', '', snils)
    # проверка длины СНИЛС
    if len(digits) != 11:
        return False
    # проверка контрольной суммы
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

    if control == expected:
        return True
    else:
        return False


def extract_snils_from_text(text):
    pattern = r'\b\d{3}[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{2}\b'
    matches = re.findall(pattern, text)

    formatted_matches = []
    for match in matches:
        digits = re.sub(r'\D', '', match)
        if len(digits) == 11:
            formatted = f"{digits[:3]}-{digits[3:6]}-{digits[6:9]} {digits[9:]}"
            formatted_matches.append(formatted)

    unique_matches = []
    for item in formatted_matches:
        if item not in unique_matches:
            unique_matches.append(item)

    return unique_matches


def validate_snils_from_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            encoding = response.headers.get_content_charset() or 'utf-8'
            html = response.read().decode(encoding)
            snils_candidates = extract_snils_from_text(html)

            valid_snils = []
            for candidate in snils_candidates:
                if validate_snils(candidate):
                    valid_snils.append(candidate)

            return valid_snils
    except urllib.error.URLError as e:
        print(f"Проблема открытия {url}: {e}")
        return []


def validate_snils_from_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            snils_candidates = extract_snils_from_text(content)

            valid_snils = []
            for candidate in snils_candidates:
                if validate_snils(candidate):
                    valid_snils.append(candidate)

            return valid_snils
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Проблема открытия файла {file_path}: {e}")
        return []


