a = input("inserisci il numero di contributi al 31/12 dell' anno precedente a questo ")
z = input("digita anno corrente ")
z = int(z)
z = z-1
a = int(a)
b=52
while a <= 2227 :
  a += 52
  z += 1
  print (z,a)
a = a - 52
z = z -1
print ("")
print ("")
while a < 2227 :
  a+=5
  print (a,'gennaio',z) 
  if a >2227:
    break
  a+=4
  print (a,'febbraio',z)
  if a >2227:
    break
  a+=4
  print (a,'marzo',z)
  if a >2227:
    break
  a+=4
  print (a,'aprile',z)
  if a >2227:
    break
  a+=5
  print (a,'maggio',z) 
  if a >2227:
    break
  a+=4
  print (a,'giugno',z)
  if a >2227:
    break
  a+=4
  print (a,'luglio',z)
  if a >=2227:
    break
  a+=5
  print (a,'agosto',z)
  if a >2227:
    break
  a+=4
  print (a,'settembre',z) 
  if a >2227:
    break
  a+=5
  print (a,'ottobre',z)
  if a <=2227:
    break
  a+=4
  print (a,'novembre',z)
  if a <2227:
    break
  a+=4
  print (a,'dicembre',z)
print ("")
print ("")
print (" + 3 mesi di finestra mobile")
print ("")
print ("decorrenza soggetta a incremento dell'aspettativa di vita") 
