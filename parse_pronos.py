from bs4 import BeautifulSoup
import lxml
import urllib
import urllib2
import os
import datetime
import sys
import sanitize

# Macros
# parse_infos_chevaux : parse les infos de la course pour une adresse donnee. Renvoie une liste
# find_index : trouve l'index dans une liste de la chaine contenant 'nom', renvoi -1 sinon


def find_index(liste,nom):
  index=-1
  for ind in range(0,len(liste)):
	if liste[ind].find(nom) != -1:
	   index=ind
	   break	
  return int(index)

def parse_infos_chevaux(urlsource):

  nb_errors = 0
  req = urllib2.Request(urlsource)
  html = urllib2.urlopen(req)
  pronos_page = BeautifulSoup(html,"lxml")

  table_chevaux = pronos_page.find("table", "course").find_all("tbody")[1].find_all("tr")
  
  label = pronos_page.find("table", "course").find_all("tbody")[0].find_all("td")
  for i in range(0,len(label)):
	label[i] = str(label[i].contents)

  result_cheval = []
  

  for cheval in table_chevaux:
   
     sstable = cheval.find_all("td")

     num_course = urlsource[urlsource.rfind("/")+1:]
     num_course = num_course[:num_course.find("_")]

     if sstable[0].string == "NP":
	result_cheval.append([num_course,sstable[1].string,\
	'',"NP",'','','','','','','','','','','',''])
	continue

     nom_cheval = sanitize.s(cheval.find("strong").contents[0].encode("ascii","ignore"))

     id_cheval = cheval.find("a","fiche").get("href")
     id_cheval = id_cheval[id_cheval.find("idcheval")+9:]
     id_cheval = id_cheval[:id_cheval.find("&")]     

     num_cheval = sstable[0].string.encode("ascii","ignore")
      
     ind = find_index(label,"Def")
     try:
	def_cheval = sstable[ind].contents[0].encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	def_cheval = ''

     ind = find_index(label,"Ec")
     try:
	ecurie_cheval = sstable[ind].contents[0].encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	ecurie_cheval = ''

     ind = find_index(label,"Corde")
     try:
	corde_cheval = sstable[ind].contents[0].encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	corde_cheval = ''

     ind = find_index(label,"Oeil")
     try:
	oeil_cheval = sstable[ind].contents[0].encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	oeil_cheval = ''

     ind = find_index(label,"Entrai")
     try:
    	jockey_cheval = sanitize.s(sstable[ind].find_all("a")[0].contents[1].encode("ascii","ignore"))
     except:
	nb_errors = nb_errors+1
	jockey_cheval = ''
    
     ind = find_index(label,"Poids")
     try:
	poids_cheval = sstable[ind].contents[0].encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	poids_cheval = ''

     ind = find_index(label,"Dist")
     try:
	dist_cheval = sstable[ind].contents[0].encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	dist_cheval = ''

     ind = find_index(label,"10h")
     try:
	cote10h_cheval = sstable[ind].contents[0].string.encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	cote10h_cheval = ''
     try:
     	cotepmu_cheval = sstable[ind+1].find("strong").contents[0].string.encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	cotepmu_cheval = ''
     try:
	variation = sstable[ind+2].contents[0].string.encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	variation = ''
     try:
    	cotezeturf_cheval = sstable[ind+3].find("strong").contents[0].string.encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	cotezeturf_cheval = ''
     try:
      	cotebetclic_cheval = sstable[ind+4].find("strong").contents[0].string.encode("ascii","ignore")
     except:
	nb_errors = nb_errors+1
	cotebetclic_cheval = ''


     cheval_infos = [num_course, nom_cheval, id_cheval, num_cheval,\
	            def_cheval,ecurie_cheval, corde_cheval,oeil_cheval,jockey_cheval,\
                    poids_cheval,dist_cheval,cote10h_cheval,cotepmu_cheval,variation,\
                    cotezeturf_cheval,cotebetclic_cheval]


     result_cheval.append(cheval_infos)

  
  return (result_cheval,nb_errors)



