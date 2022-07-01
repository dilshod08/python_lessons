# 1. Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son = float(input('Istalgan sonni kiriting:\n>>>'))
kvadrat = son**2
kub = son**3
print(f"{son} ning kvadrati {kvadrat} ga teng\n{son} ning kubi {kub} ga teng")

# 2. Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
yosh = int(input('Siz necha yoshdasiz:\n>>>'))
t_yil = 2022 - yosh
print(f'Siz {t_yil} da tug\'ilgansiz')

# 3. Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
birinchi_son = float(input('Birinchi sonni kiriting:\n>>>'))
ikkinchi_son = float(input('Ikkinchi sonni kiriting:\n>>>'))
print(f'{birinchi_son}+{ikkinchi_son}={birinchi_son+ikkinchi_son}')
print(f'{birinchi_son}-{ikkinchi_son}={birinchi_son-ikkinchi_son}')
print(f'{birinchi_son}*{ikkinchi_son}={birinchi_son*ikkinchi_son}')
print(f'{birinchi_son}/{ikkinchi_son}={birinchi_son/ikkinchi_son}')