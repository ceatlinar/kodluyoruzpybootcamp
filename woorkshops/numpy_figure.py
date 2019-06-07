import numpy as np 
import matplotlib.pyplot as plt


def create_siyahbeyaz():
	return np.full((20,20),0)


def create_siyahbeyaz_cerceveli():
	siyahbeyaz_cerceveli = np.full((20,20),1)
	myarray = [0,1,18,19]

	for i in range(len(myarray)):
		siyahbeyaz_cerceveli[myarray[i]] = 0
		siyahbeyaz_cerceveli[:,myarray[i]] = 0

	return siyahbeyaz_cerceveli


def create_siyahbeyaz_cerceveli_kosegen():
	siyahbeyaz_cerceveli_kosegen = create_siyahbeyaz_cerceveli()
	for i in range(20):
		siyahbeyaz_cerceveli_kosegen[i][i] = 0

	return siyahbeyaz_cerceveli_kosegen


if __name__  == '__main__':
	siyahbeyaz = create_siyahbeyaz()
	siyahbeyaz_cerceveli = create_siyahbeyaz_cerceveli()
	siyahbeyaz_cerceveli_kosegen = create_siyahbeyaz_cerceveli_kosegen()

	plt.figure()
	plt.subplot(1,3,1)
	plt.imshow(siyahbeyaz, 'gray', interpolation='none')
	plt.subplot(1,3,2)
	plt.imshow(siyahbeyaz_cerceveli, 'gray', interpolation='none')
	plt.subplot(1,3,3)
	plt.imshow(siyahbeyaz_cerceveli_kosegen, 'gray', interpolation='none')
	plt.show()

