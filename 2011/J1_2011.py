print("How many antennas?")
ante=int(input(""))
print("How many eyes?")
eyes=int(input(""))
if ante >= 3 and eyes<=4:
    print("TroyMartian")
if ante <= 6 and eyes>=2:
    print("VladSaturnian")
if ante <= 2 and eyes <=3:
    print("GraemeMercurian")