anni = input(
    "inserisci l'eta'")
settimane = input(
    "inserisci il numero di contributi al 31/12 dell' anno precedente al corrente ")
anno = input("digita anno corrente ")
anno = int(anno)
anno = anno-1
annox= anno
settimane = int(settimane)
settimanex = settimane

#calcolo anticipata donne
print("")
print("calcolo pensione anticipata donne")
print("")
while settimane <= 2175:
    settimane += 52
    anno += 1
    print(anno, settimane)
settimane = settimane - 52
anno = anno - 1
print("")
print("")
while settimane < 2175:
    settimane += 5
    print(settimane, 'gennaio', anno)
    if settimane < 2175:
      settimane += 4
    print(settimane, 'febbraio', anno)
    if settimane < 2175:
      settimane += 4
      print(settimane, 'marzo', anno)
    if settimane < 2175:
      settimane += 4
      print(settimane, 'aprile', anno)
    if settimane < 2175:
      settimane += 5
      print(settimane, 'maggio', anno)
    if settimane < 2175:
      settimane += 4
      print(settimane, 'giugno', anno)
    if settimane < 2175:
      settimane += 4
      print(settimane, 'luglio', anno)
    if settimane < 2175:
     settimane += 5
     print(settimane, 'agosto', anno)
    if settimane< 2175:
     settimane += 4
     print(settimane, 'settembre', anno)
    if settimane < 2175:
     settimane += 5
     print(settimane, 'ottobre', anno)
    if settimane < 2175:
     settimane += 4
     print(settimane, 'novembre', anno)
    if settimane < 2175:
     settimane += 4
     print(settimane, 'dicembre', anno)

print("")
print("")
print(" + 3 mesi di finestra mobile")
print("")
print("decorrenza soggetta a incremento dell'aspettativa di vita")

#calcolo pensione anticipata uomini
settimanem = settimanex
annom = annox
print("")
print("calcolo pensione anticipata uomini")
print("")
while settimanem <= 2227:
    settimanem += 52
    annom += 1
    print(annom, settimanem)
settimanem = settimanem - 52
annom = annom - 1
print("")
print("")
while settimanem < 2227:
    settimanem += 5
    print(settimanem, 'gennaio', annom)
    if settimanem < 2227:
      settimanem += 4
    print(settimanem, 'febbraio', annom)
    if settimanem < 2227:
      settimanem += 4
      print(settimanem, 'marzo', annom)
    if settimanem < 2227:
      settimanem += 4
      print(settimanem, 'aprile', annom)
    if settimanem < 2227:
      settimanem += 5
      print(settimanem, 'maggio', annom)
    if settimanem < 2227:
      settimanem += 4
      print(settimanem, 'giugno', annom)
    if settimanem < 2227:
      settimanem += 4
      print(settimanem, 'luglio', annom)
    if settimanem < 2227:
     settimanem += 5
     print(settimanem, 'agosto', annom)
    if settimanem< 2227:
     settimanem += 4
     print(settimanem, 'settembre', annom)
    if settimanem < 2227:
     settimanem += 5
     print(settimanem, 'ottobre', annom)
    if settimanem < 2227:
     settimanem += 4
     print(settimanem, 'novembre', annom)
    if settimanem < 2227:
     settimanem += 4
     print(settimanem, 'dicembre', annom)

print("")
print("")
print(" + 3 mesi di finestra mobile")
print("")
print("decorrenza soggetta a incremento dell'aspettativa di vita")

#calcolo pensione di vecchiaia
print("")
print("calcolo pensione di vecchiaia")
print("")
annov = anno
while anni <= 67:
    anni += 1
    annov += 1
    print(annov, anni)

print("")
print("")
print("dal mese successivo al compimento dei 67 anni")
print("")
print("decorrenza soggetta a incremento dell'aspettativa di vita")

