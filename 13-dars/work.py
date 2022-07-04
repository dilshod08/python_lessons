# 1. otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi
# Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam = {'ism':'Zafar','t_yil':'1972','viloyat':'Samarqand'}
print(f"Dadamning ismi {otam['ism']}, {otam['t_yil']}-yilda, {otam['viloyat']} viloyatida tu'g'ilgan.")

# 2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining
# sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
taomlar = {'akam':'manti', 'dadam':'chuchvara', 'biyim':'shashlik', 'bobom':'shashlik','anam':'chuchvara'}
print(f"Akamning sevimli taomi {taomlar['akam']}.")
print(f"Dadamning sevimli taomi {taomlar['dadam']}.")
print(f"Biyimning sevimli taomi {taomlar['biyim']}.")

# 3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float,
# string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
python = {'if':'agar','else':'aks holda','string':'matn','print':'konsolga chiqarish','variable':"o'zgaruvchi",'integer':"Butun son",'float':"O'nlik son",'list':"Ro'yxat",'tuple':"O'zgarmas ro'yxat"}
keyword = input(f"Kalit so'zni kiriting:\n>>>")
print(python.get(keyword,"Bunday so'z mavjud emas"))

# 4. Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
dict = {'apple':'olma','book':'kitob','car':'avtomobil','day':'kun','elephant':'fil','fish':'baliq','green':'yashil','hello':'salom','ink':'siyoh','jam':'murabbo'}
tarjima = input('So\'z kiriting:\n>>>')
print(dict.get(tarjima.lower(),'Bunday so\'z mavjud emas'))

# 5. Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
dict = {'apple':'olma','book':'kitob','car':'avtomobil','day':'kun','elephant':'fil','fish':'baliq','green':'yashil','hello':'salom','ink':'siyoh','jam':'murabbo'}
tarjima = input('So\'z kiriting:\n>>>')
if tarjima in dict:
    print(dict.get(tarjima))
else:
    print('Bunday so\'z mavjud emas')



