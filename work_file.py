import os.path
p = 1
k = []
ccc = -1
while p == 1 or p == 2:
    ccc += 1        
    if ccc == 0:
        print("Привет мой друг")
        print("Вот мои функции: ")
        print("0 - выход из меня(программы)")
        print("1 - счёт кол-во файлов в директории")
        print("2 - сортировка продуктов и запись в файл по возрастанию или убыванию")
        p = int(input("Что ты хочешь? Введи чило: "))
    else:
        st = input("Ты хочешь продолжить? Yes/y/1: ");
        if st == "Yes" or st == "y" or st == "1":
            print("Вот мои функции: ")
            print("0 - выход из меня(программы)")
            print("1 - счёт кол-во файлов в директории")
            print("2 - сортировка продуктов и запись в файл по возрастанию или убыванию")
            p = int(input("Что ты хочешь? Введи число: "))
        else:
            break
    if p == 1:
        path = input("Введите путь к директории: ")
        num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        print("Кол-во файлов", num_files)
    elif p == 2:
        o = input("Отсортировать по убыванию? y/n: ")
        if o != "y" and o != "n":
            print("Вы ответили не верно, сортируем по убыванию!")
            o = "y"
        f = open('products.txt', 'r');
        for l in f:
            z = l.split(";")
            if (int(z[2]) > 1700):
                k.append(z[0] + ";" + z[1] + ";" + str(int(z[2])))
        f.close()
        if o == "y":
            k = sorted(k, reverse=True)
        else:
            k = sorted(k)
        for i in k:
            print(i)
        s = input("Сохранить в файл? y/n: ")
        if s == "y":
            n = input("Введите имя файла: ")
            ff = open(n + ".txt", 'w')
            for i in k:
                ff.write(i + '\n')
            ff.close()
        
