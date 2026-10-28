# ceki ve bileti daxil edirik
ceki = float(input("Ceki daxil edin:"))
bilet = input("Bileti daxil edin (econom/business):")
#serti yoxla
if ceki > 32:
    print("Ceki coxdur qebul olunmur")

    # business serleri
elif bilet == ("business"):
    print  ("pulsuz")
elif bilet == "econom" and ceki <= 23:
    print("pulsuz")
else:
    print("30 azn")
