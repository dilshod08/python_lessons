# 1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ['Turkiya','Rossiya','Ukraina','O\'zbekiston','Eron']
print(davlatlar)

# 2. Ro'yxatning uzunligini konsolga chiqaring
davlatlar = ['Turkiya','Rossiya','Ukraina','O\'zbekiston','Eron']
print(len(davlatlar))

# 3. sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
davlatlar = ['Turkiya','Rossiya','Ukraina','O\'zbekiston','Eron']
print(sorted(davlatlar))

# 4. sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
davlatlar = ['Turkiya','Rossiya','Ukraina','O\'zbekiston','Eron']
print(sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qaytadan konsolga chiqaring.
davlatlar = ['Turkiya','Rossiya','Ukraina','O\'zbekiston','Eron']
print(davlatlar)

# 6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar = ['Turkiya','Rossiya','Ukraina','O\'zbekiston','Eron']
davlatlar.reverse()
print(davlatlar)

# 7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar = ['Turkiya','Rossiya','Ukraina','O\'zbekiston','Eron']
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
sonlar = list(range(120,1200,2))
print(sonlar)

# 9. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
sonlar = list(range(120,1200))
print(sum(sonlar))

# 10. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
sonlar = list(range(120,1200))
ayirma = max(sonlar)-min(sonlar)
print(ayirma)
print(max(sonlar)-min(sonlar))

# 11. Ro'yxatdagi elementlar sonini hisoblang
sonlar = list(range(120,1200))
print(len(sonlar))

# 12.Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
sonlar = list(range(120,1200))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[410:430])

# 13. taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['Osh','Manti','Somsa','Sho\'rvo','Mastava']

# 14. nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

# 15.Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta = taomlar[:]
nonushta.remove('Osh')
nonushta.append('Gamburger')
nonushta.insert(2, 'Pitsa')
del nonushta[0]

# 16. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
print(nonushta)



