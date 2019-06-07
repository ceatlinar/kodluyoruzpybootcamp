
def check_isdigit(info_length, mystr):
	if mystr.isdigit() and len(mystr) == info_length:
		return True
	else:
		return False

def get_correct_info(info_length, mystr):
	correct_info = False
	while not correct_info:
		print(mystr)
		giris_verisi = input()
		if check_isdigit(info_length, giris_verisi):
			correct_info = True
	return giris_verisi

def print_customer_info(musteri):
	print('Musteri Bilgileri')
	for key, value in musteri.items():
		print(key,value)


if __name__ == '__main__':
	musteri = {}
	print('İsminizi Giriniz')
	musteri['isim'] = input()
	print('Soyisminizi Giriniz')
	musteri['soyisim'] = input()
	musteri['dogum_yili'] = get_correct_info(4, 'Doğum Yılınızı Giriniz')
	print('TC kimlik Numaranızı Girmek İsterseniz 1 İstemezseniz 2 Tuşuna Basınız')
	if int(input()) == 1:
		musteri['TC'] = get_correct_info(11,'11 Haneli TC Kimlik Numaranızı Giriniz')
	
	print_customer_info(musteri)
