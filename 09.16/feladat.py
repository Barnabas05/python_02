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
