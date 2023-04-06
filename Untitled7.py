#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password = "")

print(conn)

conn.close()


# In[ ]:


import mysql.connector

dataBase=mysql.connector.connect(host = "localhost", user = "root", password = "")

cursorObj=dataBase.cursor()

cursorObj.execute("CREATE DATABASE D3_TI_2023")


# In[12]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "", 
    database="D3_TI_2023"
)

cursorObj = dataBase.cursor()

mhsRecord = """CREATE TABLE mahasiswa(
                NIM VARCHAR(10)NOT NULL PRIMARY KEY, 
                NAMA VARCHAR(30) NOT NULL, 
                ALAMAT VARCHAR(255), 
                MKM VARCHAR(10) NOT NULL)"""

cursorObj.execute(mhsRecord)

dataBase.close()


# In[13]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "", 
    database="D3_TI_2023"
)

cursorObj = dataBase.cursor()

dosenRecord = """CREATE TABLE dosen(
                NIP VARCHAR(20)NOT NULL PRIMARY KEY, 
                NAMA VARCHAR(50) NOT NULL, 
                MKD VARCHAR(50) NOT NULL)"""

cursorObj.execute(dosenRecord)

dataBase.close()


# In[14]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "", 
    database="D3_TI_2023"
)

cursorObj = dataBase.cursor()

mkRecord = """CREATE TABLE matkul(
            kodeMK VARCHAR(10)NOT NULL PRIMARY KEY, 
            namaMK VARCHAR(50) NOT NULL, 
            WAKTU DATE, 
            RUANG VARCHAR(10))"""

cursorObj.execute(mkRecord)

dataBase.close()


# In[15]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = "root", 
    password = "", 
    database="D3_TI_2023"
)

cursorObj=dataBase.cursor()

sql="INSERT INTO mahasiswa(NIM, NAMA, ALAMAT, MKM) VALUES(%s,%s,%s,%s)"
val = [("V3922001","Audy","Ngawi","Praktik Pemrograman Python"),
("V3922002","Layla","Sragen","Praktik Basis Data"),
("V3922003","Nayomi","Karanganyar","Kewirausahaan"),
("V3922004","Nara","Surakarta","Praktik Mikrokontroller"),
("V3922005","Rachma","Boyolali","Statistika dan Probabilitas")]

cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[16]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = "root", 
    password = "", 
    database="D3_TI_2023"
)

cursorObj=dataBase.cursor()

sql="INSERT INTO Dosen(NIP, NAMA, MKD) VALUES(%s,%s,%s)"
val = [("202301","Bhakti","Praktik Pemrograman Python"),
("20232","Kusuma","Statistika dan Probabilitas"),
("20233","Bintang","Praktik Mikrokontroller"),
("20234","Aura","Kewirausahaan"),
("20235","Afifah","Praktik Basis Data")]

cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[18]:


import mysql.connector


dataBase = mysql.connector.connect(host = 'localhost', 
                                   user = "root", 
                                   password = "", 
                                   database="D3_TI_2023")

cursorObj=dataBase.cursor()


sql="INSERT INTO matkul(kodeMK, namaMK, WAKTU, RUANG) VALUES(%s,%s,%s,%s)"
val = [("2301","Praktik Pemrograman Python","14-1-2023","Labkom 1"),
       ("2302","Statistika dan Probabilitas","15-1-2023","Ruang Virtual"),
       ("2303","Praktik Basis Data","1-2-2023","Ruang Mikro"),
       ("2304","Kewirausahaan","31-1-2023","Labkom 3"),
       ("2305","Praktik Mikrokontroller","16-2-2023","Labkom 2")]


cursorObj.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[19]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = "root", 
    password = "", 
    database="D3_TI_2023") 

cursorObj = dataBase.cursor()

sql = "SELECT NAMA, MKD FROM dosen"

cursorObj.execute (sql)

myresult = cursorObj.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[ ]:




