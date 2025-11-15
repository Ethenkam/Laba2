from validate_snils import validate_snils, validate_snils_from_url, validate_snils_from_file


while True:
    print("\nВыберите способ ввода СНИЛС:")
    print("1. Ввести вручную")
    print("2. Проверить по URL")
    print("3. Проверить в файле")
    print("4. Выход")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        a = input('Введите номер СНИЛС: ')
        if validate_snils(a):
            print('СНИЛС верный')
        else:
            print('СНИЛС не верный')

    elif choice == "2":
        url = input('Введите URL веб-страницы: ')
        valid_snils_list = validate_snils_from_url(url)
        if valid_snils_list:
            print('Найдены действительные СНИЛС:')
            for snils in valid_snils_list:
                print(f'  {snils}')
        else:
            print('Действительных СНИЛС не найдено')

    elif choice == "3":
        file_path = input('Введите путь к файлу: ')
        valid_snils_list = validate_snils_from_file(file_path)
        if valid_snils_list:
            print('Найдены действительные СНИЛС:')
            for snils in valid_snils_list:
                print(f'  {snils}')
        else:
            print('Действительных СНИЛС не найдено')

    elif choice == "4":
        print("Выход из программы")
        break

    else:
        print("Некорректный выбор, попробуйте снова")


