#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib


metin = input("Hash değerini hesaplamak istediğiniz metni girin: ")


print("Kullanabileceğiniz hash algoritmaları: SHA1, SHA256, SHA512, MD5")
algoritma = input("Kullanmak istediğiniz hash algoritmasını girin: ").upper()


if algoritma == "SHA1":
    hash_degeri = hashlib.sha1(metin.encode()).hexdigest()
elif algoritma == "SHA256":
    hash_degeri = hashlib.sha256(metin.encode()).hexdigest()
elif algoritma == "SHA512":
    hash_degeri = hashlib.sha512(metin.encode()).hexdigest()
elif algoritma == "MD5":
    hash_degeri = hashlib.md5(metin.encode()).hexdigest()
else:
    print("Geçersiz hash algoritması!")
    exit()


print(f"\nMetnin hash değeri ({algoritma}): {hash_degeri}")


# In[ ]:




