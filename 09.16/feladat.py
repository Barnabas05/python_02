import math

# 1
ar = int(input("mennyibe kerül 1kg krumpli? "))
kg = int(input("hany kg-ot szeretnél venni? "))
print(ar*kg)

# 2
fizetes = int(input("mennyi a jelenlegi fizetésed? "))
emeles = int(input("hány százalékkal emelkedett a fizetésed "))
print(fizetes*((emeles/100)+1))

# 3
sporolas = int(input("havonta mennyi pénzt tud félre rakni? "))
ar = int(input("mennyibe kerul a kivalasztott eszköz? "))
print(ar/sporolas)

# 4
kolcson = int(input("kölcsön összege? "))
ido = int(input("futamidő hónapban számmal megadva: "))
print(kolcson/ido)

# 5
szelessseg = int(input("a szoba szélessége m-ben megadva: "))
magassag = int(input("a szoba magassága m-ben megadva: "))
terulet = (szelessseg*magassag)*4
csterulet = 0.2*0.2
print((terulet/csterulet)*1.1)

# 6
print("első időpont: ")
ido1 = int(input("adja meg az órát: "))
ido2 = int(input("adja meg a percet: "))
ido3 = int(input("adja meg a masodpercet: "))
print("masodik idopont: ")
ido4 = int(input("adja meg az órát: "))
ido5 = int(input("adja meg a percet: "))
ido6 = int(input("adja meg a masodpercet: "))

h = ido1-ido4
m = ido2-ido5
s = ido3-ido6

print(h*3600+m*60+s)

# 7
d = float(input("adja meg a dinnye atmerojet meterben: "))
db = int(input("adja meg a dinnyek szamat: "))
kerulet = d*3.14
print(((kerulet*2)+0.6)*db)

# 8
szelesseg = int(input("adja meg a kert szelesseget meterben: "))
hossz = int(input("adja meg a kert hosszat meterben: "))
print(round((szelesseg*hossz)/5))

# 9
szam1 = int(input("adjon meg egy egesz szamot: "))
szam2 = int(input("adjon meg egy egesz szamot: "))
print(math.sqrt(szam1+szam2))

# 10
