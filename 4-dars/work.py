kocha="Elobod"
mahalla="Birlik"
tuman="Urgut"
viloyat="Samarqand"
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

kocha=input("Ko'changiz nomini kiriting: \n>>>")
mahalla=input("Mahallangiz nomini kiriting: \n>>>")
tuman=input("Tumaningiz nomini kiriting: \n>>>")
viloyat=input("Viloyatingiz nomini kiriting: \n>>>")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati".title())
print(f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati".title())

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(f"{manzil.title()}\n{manzil.upper()}\n{manzil.lower()}\n{manzil.capitalize()}")