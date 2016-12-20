print('Unesite broj:')
broj = int(input())
def konverzija_bin_dec(broj):
	suma = 0
	ob = broj[::-1]
	for i in range(len(ob)):
		if int(ob[i]) != 0:
			suma += 2 ** i
	return suma

def konverzija_dec_bin(broj):
        suma = ''
        for i in range(16, -1, -1):
                if broj >= 2 ** i:
                        broj -= 2 ** i
                        suma += "1"
                else:
                        suma += '0'
        return suma.lstrip('0')
print(konverzija_dec_bin(broj))
