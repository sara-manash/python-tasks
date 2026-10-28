# mesafe ve vaxt daxil etmeek
mesafe = float(input("Mesafeni daxil edin:"))
vaxt = int(input("Vaxti daxil edi:"))
# serti yaxkayiriq, 2 azn baslayir ve 1 km 0,8 azn odenis
qiymet = 2 + (mesafe * 0.8)
# gece vaxt qiymet 20% artir (23:00-06:00)
if vaxt >= 23 or vaxt <= 6:
    qiymet = qiymet * 1.2
    print("yekun qiymet:")
# min gedis 3 azn
if qiymet < 3:
    qiymet = 3
print(qiymet)