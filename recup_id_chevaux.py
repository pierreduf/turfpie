from bs4 import BeautifulSoup
import lxml
import urllib
import urllib2
import os
import datetime


# Macros
# find_nom_cheval = retourne le nom du cheval de l'url donnee
# find_max_id = retourne le nombre total de chevaux dans la base canalturf
# get_id_chevaux = parse les infos d'identite du cheval de l'url donnee

def find_nom_cheval(urlsource):

  req = urllib2.Request(urlsource)
  html = urllib2.urlopen(req)
  page = BeautifulSoup(html,"lxml")

  nom_cheval=page.find("div","ficheinfo").find("h1").contents[0].encode("ascii","ignore")

  return nom_cheval


def find_max_id():

  fiche_vide = "Fiche du cheval "
  nb_max = 400000
  url_root = "http://www.canalturf.com/courses_fiche_cheval.php?idcheval="

  bb = 0
  bh = nb_max

  while bh != bb+1:
    url = url_root + str(bb+(bh-bb)/2)
    nom = find_nom_cheval(url)
    if nom != fiche_vide:
	bb = (bb+(bh-bb)/2)
    else:
	bh = (bb+(bh-bb)/2)

  return bb


def get_id_chevaux(mini,maxi):

  nb_errors = 0
  url_root = "http://www.canalturf.com/courses_fiche_cheval.php?idcheval="
  cheval_id_table = []

  for i in range(mini,maxi+1):
   urlsource = url_root+str(i)
   req = urllib2.Request(urlsource)
   html = urllib2.urlopen(req)
   page = BeautifulSoup(html,"lxml").find("div","ficheinfo")

   cartouche = page.find_all("div")[0]
   cart_infos = cartouche.find_all("div")[1]
   palmares = page.find("div","fiche_bloc")
   palm_infos = palmares.find("p")

   num = str(i)
   
   try:
     nom = cartouche.find("h1").contents[0].encode("ascii","ignore")
     nom = nom[nom.find("chev")+7:]
   except:
     nom = ''
     nb_errors = nb_errors+1

   try:
     sex = cart_infos.contents[0].encode("ascii","ignore")	
     sexe = sex[11:12]
     age = sex[12:]
   except:
     sexe = ''
     age = ''
     nb_errors = nb_errors+1

   try:
     robe = cart_infos.contents[2].encode("ascii","ignore")[7:]
   except:
     robe = ''
     nb_errors = nb_errors+1

   try:
     pere = cart_infos.contents[4].encode("ascii","ignore")[6:]
   except:
     pere = ''
     nb_errors = nb_errors+1

   try:
     mere = cart_infos.contents[6].encode("ascii","ignore")[6:]
   except:
     mere = ''
     nb_errors = nb_errors+1

   try:
     pere_mere = cart_infos.contents[8].encode("ascii","ignore")[13:]
   except:
     pere_mere = ''
     nb_errors = nb_errors+1

   try:
     proprio = cart_infos.contents[11].encode("ascii","ignore")[14:]
   except:
     proprio = ''
     nb_errors = nb_errors+1

   try:
     entraineur = cart_infos.contents[13].encode("ascii","ignore")[13:]
   except:
     entraineur = ''
     nb_errors = nb_errors+1

   try:
     eleveur = cart_infos.contents[15].encode("ascii","ignore")[10:]
   except:
     eleveur = ''
     nb_errors = nb_errors+1

   try:
     gain = palm_infos.contents[0].encode("ascii","ignore")[7:]
   except:
     gain = ''
     nb_errors = nb_errors+1

   try:
     perfs = palm_infos.contents[2].encode("ascii","ignore")[8:]
   except:
     perfs = ''
     nb_errors = nb_errors+1

   try:
     courus = palm_infos.contents[4].encode("ascii","ignore")[12:]
   except:
     courus = ''
     nb_errors = nb_errors+1

   try:
     victoires = palm_infos.contents[6].encode("ascii","ignore")[14:]
   except:
     victoires = ''
     nb_errors = nb_errors+1

   try:
     places = palm_infos.contents[8].encode("ascii","ignore")[10:]
   except:
     places = ''
     nb_errors = nb_errors+1

   cheval_id = [num,nom,sexe,age,robe,pere,mere,pere_mere,proprio,entraineur,eleveur,gain,perfs,\
 	       courus,victoires,places]

   cheval_id_table.append(cheval_id)

  
  return (cheval_id_table,nb_errors)


