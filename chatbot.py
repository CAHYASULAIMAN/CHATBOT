#studi kasus chatbot 

# chatbot yang berguna untuk melayani penjualan olahan hasil kelapa sawit 
import string 

#data base
harga_aren = 750
harga_gjawa = 600
harga_arenblok = 800
#nama bot
chatbot_name = "coco" + "bot"

print (f"Hallo , Saya adalah {chatbot_name}")
print (f"Saya akan memandu anda pada layanan ini\nsilahkan tanyakan pertanyaan anda ?")

while (True):
    user_massage= input("kamu : ").lower().strip(string.punctuation+string.whitespace)
    print (chatbot_name + ":", end=' ')

    if user_massage == "quit" or user_massage == "selesai":
        print ("sampai ketemu lagi, terimakasih atas kunjungganya", end='' )
        break

# blok bagian awal keluhan atau pertanyaan
    if user_massage == "hallo" or "hi" in user_massage:
        print ('hallo, ada yang bisa coco bantu', end='' )
    elif "tanya" in user_massage :
        print ("hallo , ada yang bisa coco bantu", end='')
    

# Blok bertanya produk
    elif "apa" in user_massage and "produk" in user_massage:
        print ('produknya ada 3 jenis, yaitu :')
        print ('1. Gula Aren')
        print ('2. Gula Jawa')
        print ('3. Gula Aren Blok')
        print ('silahkan masukan nomer produk untuk mendapat penjelasan detail', end='' )
    elif user_massage == "1" :
        print (' Gula aren merupakan produk unggulan kami produk tersebut merupakan hasil olahan dari bahan alami dengan proses yang teliti dan ketat')
        print ('kami menghadirkan produk Gula aren Tersebut dengan menjaga kualitas dan kehigenisan', end='' )
    
    elif user_massage == "2" :
        print (' Gula Jawa merupakan produk unggulan kamiproduk tersebut merupakan hasil olahan dari bahan alami tebu dengan proses yang teliti dan ketat')
        print ('kami menghadirkan produk Gula Jawa Tersebut dengan menjaga kualitas dan kehigenisan', end='' )
    
    elif user_massage == "3" :
        print (' Gula Aren Blok merupakan produk unggulan kamiproduk tersebut merupakan hasil olahan dari bahan alami dengan proses yang teliti dan ketat')
        print ('kami menghadirkan produk Gula Aren Blok Tersebut kita bentuk blok agar mudah pada saat import dan pemindahan logistik')
        print ('kami menghadirkan produk Gula Aren Blok Tersebut dengan menjaga kualitas dan kehigenisan', end='' )

# Blok bertanya harga
    elif  "harga" in user_massage and 'aren' in user_massage :
        print (f"harga gula aren adalah {str(harga_aren)}\ biji", end='') #harga gula aren
    elif  "harga" in user_massage and 'jawa' in user_massage :
        print (f"harga gula aren adalah {str(harga_gjawa)}\ biji", end='') #harga gula jawa
    elif  "harga" in user_massage and 'blok' in user_massage :
        print (f"harga gula aren adalah {str(harga_arenblok)}\ biji", end='') #harga gula aren blok
    

# Blok alamat pengiriman
    elif "alamat" in user_massage:
        print ("kami bisa mengirimkan barang hingga seluruh indonesia")
        print ("bahkan kami mampu mengirimkan barang hingga ke luar negeri", end='')
    elif 'luar negeri'in user_massage :
        print ("diluar negeri kami sudah siap untuk mengirimkan berbagai negara seperti amerika, china, jepang, korea, arab, inggris.", end='')

# Blok jasa eksport yang di gunakan        
    elif "jasa" in user_massage and "ekspor" in user_massage :
        print ('kami mengunakan jasa eksport dari perushaan seperti ')
        print ("1. esportjava")
        print ("2. gemilang export")
        print ("3. lintas jaya indo")
        print ("4. LIC", end='')


#blok penutup 
    elif "terimakasih" in user_massage :
        print ("sama sama, kami juga senang dapat membantu anda")
        print ('mohon ketik "quit atau selesai" untuk keluar dari fitur ini', end='')
    elif "saya " in user_massage and "akhiri" in user_massage :
        print ("sama sama, kami juga senang dapat membantu anda")
        print ('mohon ketik "quit atau selesai" untuk keluar dari fitur ini', end='')
    elif "terimakasih" in user_massage and "kerjasama" in user_massage:
        print ("sama sama, kami juga senang dapat membantu anda")
        print ('"mohon ketik "quit atau selesai" untuk keluar dari fitur ini"', end='')

    else :
        print ('mohon memasukan pertanyaan dengan menyertakan kata kunci "tanya,nama produk,harga,masalah" dalam pertanyaan agar cocobot merespon, Terimakasih.', end='' )
    print()elapa 

import string 

#data base
harga_aren = 750
harga_gjawa = 600
harga_arenblok = 800
#nama bot
chatbot_name = "coco" + "bot"

print (f"Hallo , Saya adalah {chatbot_name}")
print (f"Saya akan memandu anda pada layanan ini\nsilahkan tanyakan pertanyaan anda ?")

while (True):
    user_massage= input("kamu : ").lower().strip(string.punctuation+string.whitespace)
    print (chatbot_name + ":", end=' ')

    if user_massage == "quit" or user_massage == "selesai":
        print ("sampai ketemu lagi, terimakasih atas kunjungganya", end='' )
        break

# blok bagian awal keluhan atau pertanyaan
    if user_massage == "hallo" or "hi" in user_massage:
        print ('hallo, ada yang bisa coco bantu', end='' )
    elif "tanya" in user_massage :
        print ("hallo , ada yang bisa coco bantu", end='')
    

# Blok bertanya produk
    elif "apa" in user_massage and "produk" in user_massage:
        print ('produknya ada 3 jenis, yaitu :')
        print ('1. Gula Aren')
        print ('2. Gula Jawa')
        print ('3. Gula Aren Blok')
        print ('silahkan masukan nomer produk untuk mendapat penjelasan detail', end='' )
    elif user_massage == "1" :
        print (' Gula aren merupakan produk unggulan kami produk tersebut merupakan hasil olahan dari bahan alami dengan proses yang teliti dan ketat')
        print ('kami menghadirkan produk Gula aren Tersebut dengan menjaga kualitas dan kehigenisan', end='' )
    
    elif user_massage == "2" :
        print (' Gula Jawa merupakan produk unggulan kamiproduk tersebut merupakan hasil olahan dari bahan alami tebu dengan proses yang teliti dan ketat')
        print ('kami menghadirkan produk Gula Jawa Tersebut dengan menjaga kualitas dan kehigenisan', end='' )
    
    elif user_massage == "3" :
        print (' Gula Aren Blok merupakan produk unggulan kamiproduk tersebut merupakan hasil olahan dari bahan alami dengan proses yang teliti dan ketat')
        print ('kami menghadirkan produk Gula Aren Blok Tersebut kita bentuk blok agar mudah pada saat import dan pemindahan logistik')
        print ('kami menghadirkan produk Gula Aren Blok Tersebut dengan menjaga kualitas dan kehigenisan', end='' )

# Blok bertanya harga
    elif  "harga" in user_massage and 'aren' in user_massage :
        print (f"harga gula aren adalah {str(harga_aren)}\ biji", end='') #harga gula aren
    elif  "harga" in user_massage and 'jawa' in user_massage :
        print (f"harga gula aren adalah {str(harga_gjawa)}\ biji", end='') #harga gula jawa
    elif  "harga" in user_massage and 'blok' in user_massage :
        print (f"harga gula aren adalah {str(harga_arenblok)}\ biji", end='') #harga gula aren blok
    

# Blok alamat pengiriman
    elif "alamat" in user_massage:
        print ("kami bisa mengirimkan barang hingga seluruh indonesia")
        print ("bahkan kami mampu mengirimkan barang hingga ke luar negeri", end='')
    elif 'luar negeri'in user_massage :
        print ("diluar negeri kami sudah siap untuk mengirimkan berbagai negara seperti amerika, china, jepang, korea, arab, inggris.", end='')

# Blok jasa eksport yang di gunakan        
    elif "jasa" in user_massage and "ekspor" in user_massage :
        print ('kami mengunakan jasa eksport dari perushaan seperti ')
        print ("1. esportjava")
        print ("2. gemilang export")
        print ("3. lintas jaya indo")
        print ("4. LIC", end='')


#blok penutup 
    elif "terimakasih" in user_massage :
        print ("sama sama, kami juga senang dapat membantu anda")
        print ('mohon ketik "quit atau selesai" untuk keluar dari fitur ini', end='')
    elif "saya " in user_massage and "akhiri" in user_massage :
        print ("sama sama, kami juga senang dapat membantu anda")
        print ('mohon ketik "quit atau selesai" untuk keluar dari fitur ini', end='')
    elif "terimakasih" in user_massage and "kerjasama" in user_massage:
        print ("sama sama, kami juga senang dapat membantu anda")
        print ('"mohon ketik "quit atau selesai" untuk keluar dari fitur ini"', end='')

    else :
        print ('mohon memasukan pertanyaan dengan menyertakan kata kunci "tanya,nama produk,harga,masalah" dalam pertanyaan agar cocobot merespon, Terimakasih.', end='' )
    print()
