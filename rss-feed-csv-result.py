import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('result.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Judul", "Tanggal", "Link"])

keyword = input("Masukkan Keyword Anda: ")

def liputan6(keyword):
    url = requests.get('https://feed.liputan6.com/rss')
    s = BeautifulSoup(url.text, features="xml")
    item = s.find_all('item')
    for i in item:
        title = i.title.text
        if keyword in title:
            #cari = i.find('description').text
            link = i.find('link').text
            date = i.find('pubDate').text
            #cari1 = cari.split('>')[10]
            print(title)
            print(link)
            #print(cari1)
            print(date, "\n")
            csv_writer.writerow([title, date, link])

def detik(keyword):
    url = requests.get('http://rss.detik.com/index.php/detikcom')
    s = BeautifulSoup(url.text, features="xml")
    isi = s.find_all('item')
    for i in isi:
        title = i.title.text
        if keyword in title:
            cari = i.find('description').text
            link = i.find('link').text
            date = i.find('pubDate').text
            isi = cari.split('>')[1]
            print(title)
            print(link)
            print(isi)
            print(date, "\n")
            csv_writer.writerow([title, date,isi, link])


def suara(keyword):
    link = requests.get('https://www.suara.com/rss')
    s = BeautifulSoup(link.text, features='xml')
    isi = s.find_all('item')
    for i in isi:
        title = i.title.text
        if keyword in title:
            cari = i.find('description').text
            link = i.find('link').text
            date = i.find('pubDate').text
            isi = cari.split('\t')[8]
            print(title)
            print(link)
            print(isi)
            print(date, "\n")
            csv_writer.writerow([title, date, isi, link])

def okezone(keyword):
    link = requests.get('http://sindikasi.okezone.com/index.php/okezone/RSS2.0')
    s = BeautifulSoup(link.text, features='xml')
    isi = s.find_all('item')
    for i in isi:
        title = i.title.text
        if keyword in title:
            link = i.find('link').text
            if "://news" in link:
                isi = requests.get(link)
                bs = BeautifulSoup(isi.text, features="html.parser")
                konten = bs.find('p').text
                t = bs.find('div', class_="reporter")
                date = t.find('b').text
                print(title)
                print(link)
                split_konten = konten.split("\n")
                hasil = split_konten[0].strip()
                print(date)
                print(hasil + "\n")
                csv_writer.writerow([title, date,isi, link])

def portalAntara(keyword):
    link = requests.get('https://www.antaranews.com/rss/terkini')
    s = BeautifulSoup(link.text, features='xml')
    isi = s.find_all('item')
    for i in isi:
        title = i.title.text
        if keyword in title:
            link = i.find('link').text
            date = i.find('pubDate').text
            get = requests.get(link)
            s = BeautifulSoup(get.text, features='html.parser')
            cari = s.find('div', class_="post-content clearfix").text
            jjk = cari.split("\n")
            bbb = jjk[1].strip()
            ccc = jjk[3].strip()
            isi = bbb + ccc
            print(title)
            print(isi)
            print(link)
            print(date, "\n")
            csv_writer.writerow([title, date, isi, link])
    csv_file.close()
liputan6(keyword)
detik(keyword)
suara(keyword)
okezone(keyword)
portalAntara(keyword)