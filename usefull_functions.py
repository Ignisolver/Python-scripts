def szyfr(ciong):
	klucz = {1: 'a', 2: 'ą', 3: 'b', 4: 'c', 5: 'ć', 6: 'd', 7: 'e', 8: 'ę', 9: 'f', 11: 'g', 12: 'h', 13: 'i', 14: 'j',
			 15: 'k', 16: 'l', 17: 'ł', 18: 'm', 19: 'n', 21: 'ń', 22: 'o', 23: 'ó', 24: 'p', 25: 'r', 26: 's', 27: 'ś',
			 28: 't', 29: 'u', 31: 'w', 32: 'y', 33: 'z', 34: 'ź', 35: 'ż'}
	ciong = ciong.replace("000", "0")
	while True:
		if ciong[-1] == "0":
			ciong = ciong[0:-1]
		elif ciong[0] == "0":
			ciong = ciong[1:]
		else:
			break
	ciongi = list(ciong.split("00"))
	wyn = [[],[]]
	for j in ciongi:
		ciong = list(j.split("0"))
		for i in ciong:
			try:
				wyn[0].append(klucz[int(i)])
			except:
				wyn[0].append(str(int(i)))
			wyn[1].append(i)
		wyn[0].append(" ")
		wyn[1].append(" ")
	print(klucz)
	print(" ".join(wyn[1]))
	print("".join(wyn[0]))


def del_int(tekst):
	wyn = ''
	for el in tekst[::-1]:
		try:
			int(el)
		except:
			wyn += el
	return wyn[::-1]

def linki(txt):
	with open("/media/ignacy/TERA/PLIKI/Dokumenty/Myśli/strony2.txt","r") as strony:
		strony = list(strony)
		for i in strony:
			try:
				i = list(i)
				i.remove("\n")
			except: pass
			print(txt, "".join(i))

#linki(input("haslo: "))
#del_int(input("tekst:")
szyfr(input("przepisz wiadomosc"))


