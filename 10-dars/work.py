# 1. Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft
# emas" degan xabarni chiqaring.
json = int(input('Juft son kiriting:\n>>>'))
if json%2==0:
    print('Rahmat!')
else:
    print("Bu juft son emas")

# 2. Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
    # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
    # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
    # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
f_yoshi = int(input('Yoshingiz nechada:\n>>>'))
if f_yoshi<=4 or 60<=f_yoshi:
    price = 'bepul'
elif f_yoshi<18:
    price = 10000
else:
    price = 20000
print(f"Sizga muzeyga kirish {price}.")

# 3. Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring.
son_1 = float(input('Birinchi sonni kiriting:\n>>>'))
son_2 = float(input('Ikkinchi sonni kiriting:\n>>>'))
if son_1 == son_2:
    natija = 'ga teng'
elif son_1>son_2:
    natija = 'dan katta'
else:
    natija = 'dan kichik'
print(f'Birinchi son ikkinchi son{natija}.')

# 4. mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan
# savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ['un','tuxum','nok','olma','guruch','karam','choy','shakar','non','banan']
savat = []
for m in range(5):
    savat.append(input(f'{m+1}-mahsulotni kiriting:\n>>>'))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")

# 5. Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor
# mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas
# ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda
# yo'q: ....." degan xabarni chiqaring.
mahsulotlar = ['un','tuxum','nok','olma','guruch','karam','choy','shakar','non','banan']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for fm in range(5):
    savat.append(input(f'{fm+1}- mahsulotni kiriting:\n>>>'))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if len(mavjud_emas)==0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print(f'Quyidagi mahsulotlar do\'konimizda yo\'q: .....\n{mavjud_emas}')

# 6. foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
foydalanuvchilar = ['mrcoder_99','dbz008','farrukh','admin','zafar']
login = input('Iltimos yangi login tanlang:\n>>>')
if login.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login}!")

# 7. Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz
# bo'linishini konsolga chiqaring.
butunson = int(input('Butun son kiriting:\n>>>'))
for n in range(2,11):
    if butunson%n == 0:
        print(f"{butunson} soni {n} ga qoldiqsiz bo'linadi")