# 1. ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting.
ismlar = ['Azizbek', 'Temubek', 'Oybek']

# 2. Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

ismlar = ['Azizbek', 'Temubek', 'Oybek']
print(f"{ismlar[0]} bugun to'garakka borasanmi?")
print(ismlar[1], 'Bugun ona tili dari bormi?')
print(ismlar[2] + ' ' + 'nima uchun kecha maktabga kelmading?')

# 3. sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [628, -9, 63.8, -36.6, 992, 0, 1, -65, 6423.25,-996.5 ]
sonlar[0] = sonlar[0] - 600
sonlar[3] = 56
sonlar[-1] = sonlar[-1]//5
print(sonlar, sonlar[0], sonlar[3], sonlar[-1])

# 4. t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Amir Temur', 'Ibn Sino', 'Mirzo Ulug\'bek']
z_shaxslar = ['Elon Musk', 'Pavel Durov', 'Mark Zuckerberg']
print()

# 5. Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
t_shaxslar = ['Amir Temur', 'Ibn Sino', 'Mirzo Ulug\'bek']
z_shaxslar = ['Elon Musk', 'Pavel Durov', 'Mark Zuckerberg']
print(t_shaxslar.pop(2), '1018 ta yulduzni tadqiq qilgan.', z_shaxslar.pop(1), 'Telegram ilovasining premium versiyasini 2022-yil iyun oyida e\'lon qildi')

# 6. friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('Javohir')
friends.append('Aziz')
friends.append('Shohnazar')
friends.append('Temur')
friends.append('Adham')
friends.append('Oybek')
print(friends)

# 7. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove('Adham')
friends.remove('Javohir')
print(friends)

# 8. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Beknazar')
friends.insert(2, 'Islom')
friends.insert(0, 'Karimbek')
print(friends)

# 9. Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(0))
print(mehmonlar)