import os

#İstiklal Marşını tek bir string içerisine aktaran fonksiyon
def get_istiklal_marsi():
    #İstiklal Marşını tek bir String içerisinde tutabilmek için Python triple quote kullanıyoruz.
    istiklal_marsi = '''Korkma, sönmez bu şafaklarda yüzen al sancak;
                        Sönmeden yurdumun üstünde tüten en son ocak.
                        O benim milletimin yıldızıdır, parlayacak;
                        O benimdir, o benim milletimindir ancak.

                        Çatma, kurban olayım, çehreni ey nazlı hilal!
                        Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
                        Sana olmaz dökülen kanlarımız sonra helal...
                        Hakkıdır, hakk'a tapan, milletimin istiklal!

                        Ben ezelden beridir hür yaşadım, hür yaşarım.
                        Hangi çılgın bana zincir vuracakmış? Şaşarım!
                        Kükremiş sel gibiyim, bendimi çiğner, aşarım.
                        Yırtarım dağları, enginlere sığmam, taşarım.

                        Garbın afakını sarmışsa çelik zırhlı duvar,
                        Benim iman dolu göğsüm gibi serhaddim var.
                        Ulusun, korkma! Nasıl böyle bir imanı boğar,
                        'Medeniyet!' dediğin tek dişi kalmış canavar?

                        Arkadaş! Yurduma alçakları uğratma, sakın.
                        Siper et gövdeni, dursun bu hayasızca akın.
                        Doğacaktır sana va'dettigi günler hakk'ın...
                        Kim bilir, belki yarın, belki yarından da yakın.

                        Bastığın yerleri 'toprak!' diyerek geçme, tanı:
                        Düşün altında binlerce kefensiz yatanı.
                        Sen şehit oğlusun, incitme, yazıktır, atanı:
                        Verme, dünyaları alsan da, bu cennet vatanı.

                        Kim bu cennet vatanın uğruna olmaz ki feda?
                        Şuheda fışkıracak toprağı sıksan, şuheda!
                        Canı, cananı, bütün varımı alsın da hüda,
                        Etmesin tek vatanımdan beni dünyada cüda.

                        Ruhumun senden, ilahi, şudur ancak emeli:
                        Değmesin mabedimin göğsüne namahrem eli.
                        Bu ezanlar-ki şahadetleri dinin temeli,
                        Ebedi yurdumun üstünde benim inlemeli.

                        O zaman vecd ile bin secde eder -varsa- taşım,
                        Her cerihamdan, ilahi, boşanıp kanlı yaşım,
                        Fışkırır ruh-i mücerred gibi yerden na'şım;
                        O zaman yükselerek arsa değer belki başım.

                        Dalgalan sen de şafaklar gibi ey şanlı hilal!
                        Olsun artık dökülen kanlarımın hepsi helal.
                        Ebediyen sana yok, ırkıma yok izmihlal:
                        Hakkıdır, hür yaşamış, bayrağımın hürriyet;
                        Hakkıdır, hakk'a tapan, milletimin istiklal! '''

    return istiklal_marsi


#İstiklal Marşının dictionary içerisine atıldığı metod
def get_istiklal_marsi_in_dict(cumleler):
    # dictionary tanımlanıyor ve cumleler içerisinden ilk 9 kıta için 4 satır alınıp 5. boş satır atlanıyor
    misralar = {}
    j = 1
    for i in range(0,45,5):
        misra = cumleler[i] +'\n'+ cumleler[i+1] +'\n'+ cumleler[i+2] +'\n'+ cumleler[i+3]
        misralar[j] = misra
        j += 1

    #İstiklal Marşının son mısrası 5 satır olduğu için bu mısra döngü dışında alınıyor
    i = i+5
    misralar[j] = cumleler[i] +'\n'+ cumleler[i+1] +'\n'+ cumleler[i+2] +'\n'+ cumleler[i+3] +'\n'+ cumleler[i+4]

    return misralar

#main fonksiyon
if __name__ == "__main__":
    
    #İstiklal Marşı istiklal_marsi isimli string içerisine atılıyor.
    istiklal_marsi = get_istiklal_marsi()
    
    #istiklal marşının tüm satırları splitlines metodu ile alınıyor
    cumleler = istiklal_marsi.splitlines()
    
    #Mısraların tutulacağı misralar isimli dictionary get_istiklal_marsi_in_dict metodu ile oluşturuluyor
    misralar = get_istiklal_marsi_in_dict(cumleler)

    '''Kullanıcı girdisi giris isimli değişkende tutuluyor. Tutulan bu değişken bir sayı değil ise veya 1-10 arası bir sayı
       değilse kullanıcıya uyarı veriliyor. Aksi durumda kullanıcının girdiği sayıya denk gelen mısra ekrana yazdırılıyor'''
    giris = 0
    while giris != 'x':
        print('\nİstiklal Marsinin Görmek İstediğiniz Numarasını Giriniz\nÇıkmak İçin Klavyeden X e Basınız ')
        giris = input()
        if giris.isdigit():
            giris = int(giris)
            if 1 <= giris <= 10:
                os.system('clear')
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Mısra', giris)
                print(misralar[giris])
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('İstiklal Marşı 10 Mısradan Oluşmaktadır.\nLütfen 1-10 Arasi Bir Sayı Giriniz')
        elif giris == 'x':
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Lütfen 1-10 Arasi Bir Sayi Giriniz')
