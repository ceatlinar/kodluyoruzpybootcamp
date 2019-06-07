
def calculate_factorial(sayi):
	if sayi == 0:
		return 1
	else:
		return sayi * calculate_factorial(sayi-1)


if __name__ == '__main__':
	
	print('Faktöriyeli Alınacak Sayıyı Giriniz')
	
	sayi = int(input())
	
	if sayi < 0:
		print('Negatif Sayılar İçin Faktöriyel Hesaplanamaz')
	elif sayi == 0 or sayi == 1:
		print('Sayının Faktöriyeli {sayi}'.format(sayi = sayi))
	else:
		sonuc = calculate_factorial(sayi)
		print('Sayının Faktöriyeli {sayi}'.format(sayi = sonuc))
