#SyntaxError:
    #print"Hello World!"
print("Hello World!")

#EOL va EOF xatolik:
    #print("Hello World! EOL
print("Hello World!")
    #print("Hello World!" EOF
print("Hello World!")
#IndentationError:
    #print("O'ngacha sanaymiz")
    # for n in range(10):
    # print(n+1)
print("O'ngacha sanaymiz")
for n in range(10):
    print(n+1)
    # son = 50
    # if son>=0:
    #     print("Musbat son")
    # else:
    # print("Manfiy son")
son = 50
if son>=0:
    print("Musbat son")
else:
    print("Manfiy son")
#TypeError
    # son = input("Istalgan son kiriting: ")
    # print(f"{son} ning kvadrati {son**2} ga teng")
son = int(input("Istalgan son kiriting: "))
print(f"{son} ning kvadrati {son**2} ga teng")
#NameError
    # prit("Hello World!")
print("Hello World!")
    # mevalar = ['olma','uzum','nok','anor','anjir']
    # for meva in mvealar:
    #     print(meva)
mevalar = ['olma','uzum','nok','anor','anjir']
for meva in mevalar:
    print(meva)
#IndexError
    # mevalar = ['olma','anor','uzum']
    # print(mevalar[3])
mevalar = ['olma','anor','uzum']
print(mevalar[2])
#ZeroDivisionError
    # x, y = 50, 50
    # z = 250/(x-y)
x, y = 60, 50
z = 250/(x-y)