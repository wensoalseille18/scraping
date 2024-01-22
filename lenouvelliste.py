import requests
from bs4 import BeautifulSoup
import csv
import os
url='https://lenouvelliste.com/'
# Chemin vers le fichier CSV
chemin_fichier_csv = 'fichier.csv'
reponse=requests.get(url)
reponse.encoding='utf-8'
if  reponse.status_code ==200:
    hml=reponse.text 
    f=open("lenouvelliste.html",'w',encoding="utf-8")
    f.write(hml)
    f.close
soup= BeautifulSoup(hml,"html5lib")
don=[]
don=soup.findAll('div',class_='lnv-featured-article-lg')
don+=soup.findAll('div',class_='lnv-featured-article-sm')
don+=soup.findAll('div',class_='lnv-recent-article')
i=1
for d in don:
    image=d.find('div',class_='img-div')
    image=image.find('img')
    if image is not None:
            image=image.get('src')
    if d.find('h1'):
        titre=d.find('h1').text
    else:
        titre='pas de titre'

    if d.find('p'):
        print(d.find('p').text)
        descption=d.find('p').text
    else:
        descption='pas de description'
    if d.find('a'):
        link=d.find('a')
        if link is not None:
            link=url+link.get('href')

    atik = {i: [titre,link,descption,image]}
    image=''
    
    if os.path.exists(chemin_fichier_csv):
        if i==1:
            with open(chemin_fichier_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
        # Créer un objet writer
                writer = csv.writer(fichier_csv)
    # Écrire les données dans le fichier CSV
                for key, values in atik.items():
                    writer.writerow([key] + values)
        else:
            with open(chemin_fichier_csv, mode='a', newline='', encoding='utf-8') as fichier_csv:
                writer = csv.writer(fichier_csv)
                for key, values in atik.items():
                    writer.writerow([key] + values)
    else:
# Ouvrir le fichier CSV en mode écriture
        with open(chemin_fichier_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
        # Créer un objet writer
            writer = csv.writer(fichier_csv)
    # Écrire les données dans le fichier CSV
            for key, values in atik.items():
                writer.writerow([key] + values)
    i+=1