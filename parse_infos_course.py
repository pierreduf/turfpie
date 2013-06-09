from bs4 import BeautifulSoup
import lxml
import urllib
import urllib2
import os
import datetime
import sys

import meteo

meteo_dico = meteo.dict_meteo()


# Macros
#parse_infos_course : parse les infos de la course pour une adresse donnee. Renvoie une liste


def parse_infos_course(urlsource):

  req = urllib2.Request(urlsource)
  html = urllib2.urlopen(req)
  pronos_page = BeautifulSoup(html,"lxml")

  boite_entete = pronos_page.find_all("div","boite4rond")[0]

  num_course=urlsource[urlsource.find("PMU")+15:]
  num_course=num_course[num_course.find("/")+1:num_course.find("_")]

  nom_course = boite_entete.find_all("h1")[0].contents[0]
  nom_course = nom_course[:nom_course.find(' - ')]

  reunion_course = boite_entete.find_all("h3")[0].contents[0]
  reunion_course = reunion_course[reunion_course.rfind('union')+6:]

  lieu_course = boite_entete.find_all("h3")[0].contents[0]
  lieu_course = lieu_course[:lieu_course.find(' | ')]
  lieu_course = lieu_course[lieu_course.find(' - ')+3:]

  meteo_course = boite_entete.find_all("div","boite4rond")[0].find_all("img")
  if not meteo_course:
	meteo_course = ''
  else:
	meteo_course = meteo_course[0].get("src")
  	meteo_course = meteo_course[meteo_course.rfind('/')+1:]
  	meteo_course = meteo_dico[meteo_course]

  temp_course = str(boite_entete.find("h4"))
  if temp_course == 'None':
	temp_course = ''
  else :
  	temp_course = temp_course[temp_course.find(">")+1:temp_course.find("\xc2")] + ' - ' + temp_course[temp_course.rfind("/>")+2:temp_course.rfind("\xc2")]

  type_course = boite_entete.find_all("p")[0].contents[0]
  type_course = type_course[:type_course.find(' - ')]

  distance_course = boite_entete.find_all("p")[0].contents[0]
  distance_course = distance_course[:distance_course.find('m - ')]
  distance_course = distance_course[distance_course.find(' - ')+3:]

  prix_course = boite_entete.find_all("p")[0].contents[0]
  prix_course = prix_course[prix_course.rfind(' - ')+3:]
  prix_course = prix_course[:prix_course.find('&')]

  date_course = urlsource[urlsource.find("prono")+15:urlsource.find("prono")+25]

  heure_course = boite_entete.find_all("h3")[0].contents[0]
  heure_course = heure_course[:heure_course.find(' - ')]

  return [num_course,nom_course, reunion_course,lieu_course, meteo_course, temp_course,type_course, distance_course,prix_course, date_course,heure_course]

