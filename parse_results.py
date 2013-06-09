from bs4 import BeautifulSoup
import lxml
import urllib
import urllib2

# Macros

def parse_results(urlsource):

  nb_errors = 0
  req = urllib2.Request(urlsource)
  html = urllib2.urlopen(req)
  page = BeautifulSoup(html,"lxml")

  tr_course=page.find("table","course").find_all("tr")
  
  num_course=urlsource[urlsource.find("PMU")+15:]
  num_course=num_course[num_course.find("/")+1:num_course.find("_")]

  try:
    place_1 = tr_course[1].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_1 = ''
  try:
    place_2 = tr_course[2].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_2 = ''
  try:
    place_3 = tr_course[3].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_3 = ''
  try:
    place_4 = tr_course[4].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_4 = ''
  try:
    place_5 = tr_course[5].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_5 = ''
  try:
    place_6 = tr_course[6].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_6 = ''
  try:
    place_7 = tr_course[7].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_7 = ''
  try:
    place_8 = tr_course[8].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_8 = ''
  try:
    place_8 = tr_course[9].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1  
    place_9 = ''
  try:
    place_10 = tr_course[10].find_all("td")[1].contents[0].encode("ascii","ignore")
  except:
    nb_errors = nb_errors+1
    place_10 = ''

  block=page.find_all("div","BlockListeResultats")

  simple_gagnant = block[0].find_all("tr")[2].contents[1].string.encode("ascii","ignore")
  simple_gagnant = simple_gagnant[:len(simple_gagnant)-1]
 
  simple_place = block[0].find_all("tr")[2].contents[2].string.encode("ascii","ignore")
  simple_place = simple_place[:len(simple_place)-1]
 
  tierce_ordre = ''
  tierce_desordre = ''
  try: 
   for i in range(1,len(block)):
     if "tierc" in block[i].find_all("tr")[0].find("img").get("src"):
        tierce_ordre = block[i].find_all("tr")[1].contents[2].string.encode("ascii","ignore")
        tierce_ordre = tierce_ordre[:len(tierce_ordre)-1]

        tierce_desordre = block[i].find_all("tr")[2].contents[2].string.encode("ascii","ignore")
        tierce_desordre = tierce_desordre[:len(tierce_desordre)-1]
        break
  except:
   nb_errors = nb_errors+1

  quarte_ordre = ''
  quarte_desordre = ''
  try: 
   for i in range(1,len(block)):
     if "quart" in block[i].find_all("tr")[0].find("img").get("src"):
        quarte_ordre = block[i].find_all("tr")[1].contents[2].string.encode("ascii","ignore")
        quarte_ordre = quarte_ordre[:len(quarte_ordre)-1]

        quarte_desordre = block[i].find_all("tr")[2].contents[2].string.encode("ascii","ignore")
        quarte_desordre = quarte_desordre[:len(quarte_desordre)-1]
        break
  except:
   nb_errors = nb_errors+1
  
  quinte_ordre = ''
  quinte_desordre = ''
  try:
   for i in range(1,len(block)):
     if "quint" in block[i].find_all("tr")[0].find("img").get("src"):
        quinte_ordre = block[i].find_all("tr")[1].contents[2].string.encode("ascii","ignore")
        quinte_ordre = quinte_ordre[:len(quinte_ordre)-1]

        quinte_desordre = block[i].find_all("tr")[2].contents[2].string.encode("ascii","ignore")
        quinte_desordre = quinte_desordre[:len(quinte_desordre)-1]
        break
  except:
   nb_errors = nb_errors+1
 
  resultats = [num_course,place_1,place_2,place_3,place_4,place_5,place_6,place_7,place_8,\
               place_9,place_10,simple_gagnant,simple_place,\
               tierce_ordre,tierce_desordre,\
               quarte_ordre, quarte_desordre,\
               quinte_ordre,quinte_desordre]
     
  return (resultats,nb_errors)


