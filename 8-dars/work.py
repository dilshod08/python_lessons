# 1. Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing.
ismlar = ['Aziz','Temur','Shoxnazar','Adham','Javohir']
for i in ismlar:
    print(f"Salom, {i}.")

# 2. Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing).
ismlar = ['Aziz','Temur','Shoxnazar','Adham','Javohir']
for i in ismlar:
    print(f"Salom, {i}.")
print(f"Kod {len(ismlar)} marta takrorlandi.")

# 3. 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for l in sonlar:
    print(l, 'ning kubi', l ** 3, 'ga teng')

# 4. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#for kino in range(5):
#   kinolar.append(input(f'{kino+1}-sevimli kinongizning nomi nima?\n>>>'))
#print(kinolar)

# 5. Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odam_soni =int(input('Bugun nechta odam bilan suhbatlashdingiz?\n>>>'))
suhbatlashganlar = []
for o in range(odam_soni):
    suhbatlashganlar.append(input(f"{o+1}-odamning ismi nima edi?"))
print(suhbatlashganlar)