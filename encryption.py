import pyAesCrypt
import os

# функция шифрования файла
def encryption(file, password):

     # буфер шифрования
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Фаил ' " + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удяляем исходный код
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебор всех поддиректорий в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если фаил наиден, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках фалов
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для шифрования: ")
file_encr = input("Путь фаилов:")
walking_by_dirs(file_encr, password)
