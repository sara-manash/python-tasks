#yasini sorusuruq ve tam ededi yaziriq 
age = int(input("yasini daxil edin:"))
#telebe oldugunu yoxlayiriq (yes/no)
student = input("Telebe olursunuzmu? (yes/no):")
# serti yoxlayiriq
if age < 7:
    print("pulsuz")
elif age > 65:
    print("bilet 4 manat")
elif student == "yes":
    print("bilet 5 manat")
else:
    print("bilet 8 manat")
