if __name__ == '__main__':
	print('Lütfen Adınızı Giriniz')
	name = input()
	print('Lütfen Soyadınızı Giriniz')
	soyad = input()
	print('Lütfen Doğum Yılınızı Giriniz')
	dogum_yili = input()

	musteri = []
	musteri.append(name)
	musteri.append(soyad)
	musteri.append(dogum_yili)

	for i in range(len(musteri)):
		print(musteri[i])
