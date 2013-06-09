from bs4 import BeautifulSoup
import lxml
import urllib
import urllib2
import os
import datetime


# create_date_range : creer une liste de date entre date 'start' et date 'fin'. Format 'aaaa-mm-jj'
# get_course_links : recuperer les liens des courses (pronos et resultats)
# get_course_links_range : recuperer les liens des courses (pronos et resultats) sur un ecart de date

def create_date_range(start, end):

  start_jour = int(start[8:10])
  start_mois = int(start[5:7])
  start_annee = int(start[:4])
  start_date = datetime.date(start_annee, start_mois, start_jour)

  end_jour = int(end[8:10])
  end_mois = int(end[5:7])
  end_annee = int(end[:4])
  end_date = datetime.date(end_annee, end_mois, end_jour)

  liste_dates = []

  for nb_day in range(0, (end_date - start_date).days +1):
	incr = start_date + datetime.timedelta(nb_day)
	if incr.day<10:
		day = '0'+str(incr.day)
	else:
		day = str(incr.day)
	if incr.month<10:
		month = '0'+str(incr.month)
	else:
		month = str(incr.month)
	annee = str(incr.year)
	liste_dates = liste_dates + [annee + "-" + month + "-" + day]
  
  return liste_dates


def get_course_links(date,pronos_file,results_file):

  urlsource = "http://www.canalturf.com/courses_liste_histo.php"
  prono_string = "pronostics"
  results_string = "resultats"

  values = {'vjour' : date[8:10],
            'vmois' : date[5:7],
            'vannee' : date[:4] }

  data = urllib.urlencode(values)

  req = urllib2.Request(urlsource, data)
  html = urllib2.urlopen(req)
  table_page = BeautifulSoup(html,"lxml")

  f_pronos = open(pronos_file, 'a')
  f_results = open(results_file, 'a')

  for table in table_page.body.findAll("table"):
	for url in table.findAll("a"):
		if url.get("href").find(prono_string) != -1 :
		  f_pronos.write(url.get("href"))
		  f_pronos.write('\n')

		elif url.get("href").find(results_string) != -1 :
		  f_results.write(url.get("href"))
		  f_results.write('\n')


  f_pronos.close()
  f_results.close()


def get_course_links_range(start,end,pronos_file,results_file):

  if os.path.isfile(pronos_file): os.remove(pronos_file)
  if os.path.isfile(results_file): os.remove(results_file)

  liste_dates = create_date_range(start, end)
  for date in liste_dates:
	get_course_links(date, pronos_file,results_file)

