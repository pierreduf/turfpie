import os
import datetime
import sys
import MySQLdb as mdb

# Macros
# get_con : creation de la connexion a la base
# create_tables : cree les tables MySQL pour stockage des donnees

def get_con():

  con = mdb.connect('localhost', 'turf_user','turfpass', 'turf');

  return con

def delete_table(table):
  try:
    con = get_con()
    cur = con.cursor()
    query = "drop table if exists "+table
    cur.execute(query)  
  except mdb.Error, e:  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)    
  finally:            
    if con:    
       con.close()

def create_table(table_name):

 if table_name == 'infos_course':
   try:
     con = get_con()
     cur = con.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS infos_course(\
	num_course VARCHAR(10), \
	nom_course VARCHAR(100), \
	reunion_course VARCHAR(20), \
	lieu_course VARCHAR(20), \
	meteo_course VARCHAR(20), \
	temp_course VARCHAR(20), \
	type_course VARCHAR(20), \
	distance_course VARCHAR(20), \
	prix_course VARCHAR(20), \
	date_course VARCHAR(20), \
	heure_course VARCHAR(25))")    
   except mdb.Error, e:  
     print "Error %d: %s" % (e.args[0],e.args[1])
     sys.exit(1)    
   finally:            
     if con:    
        con.close()

 elif table_name == 'id_chevaux':
   try:
     con = get_con()
     cur = con.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS id_chevaux(\
	num_cheval VARCHAR(10), \
	nom_cheval VARCHAR(100), \
	sexe_cheval VARCHAR(5), \
	age_cheval VARCHAR(5), \
	robe_cheval VARCHAR(20), \
	pere_cheval VARCHAR(100), \
	mere_cheval VARCHAR(100), \
        pere_mere_cheval VARCHAR(100),\
	proprio_cheval VARCHAR(100), \
	entrain_cheval VARCHAR(100), \
	elev_cheval VARCHAR(100), \
	gain_cheval VARCHAR(20),\
	perfs_cheval VARCHAR(100),\
	courus_cheval VARCHAR(5),\
	victoires_cheval VARCHAR(5),\
	places_cheval VARCHAR(20))")    
   except mdb.Error, e:  
     print "Error %d: %s" % (e.args[0],e.args[1])
     sys.exit(1)    
   finally:            
     if con:    
        con.close()

 elif table_name == 'pronos_course':
   try:
     con = get_con()
     cur = con.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS pronos_course(\
	num_course VARCHAR(10), \
	nom_cheval VARCHAR(100), \
	id_cheval VARCHAR (10), \
	num_cheval VARCHAR(10), \
	def_cheval VARCHAR(10), \
	ecurie_cheval VARCHAR(10), \
	corde_cheval VARCHAR(10), \
	oeil_cheval VARCHAR(10), \
	jockey_cheval VARCHAR(50), \
	poids_cheval VARCHAR(10), \
	dist_cheval VARCHAR(10), \
	cote10h_cheval VARCHAR(15), \
	cotepmu_cheval VARCHAR(15), \
	variation VARCHAR(15), \
	cotezeturf_cheval VARCHAR(15), \
	cotebetclic_cheval VARCHAR(20))")    
   except mdb.Error, e:  
     print "Error %d: %s" % (e.args[0],e.args[1])
     sys.exit(1)    
   finally:            
     if con:    
        con.close()

 elif table_name == 'results_course':
   try:
     con = get_con()
     cur = con.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS results_course(\
	num_course VARCHAR(10), \
        place_1 VARCHAR(5), \
        place_2 VARCHAR(5), \
        place_3 VARCHAR(5), \
        place_4 VARCHAR(5), \
        place_5 VARCHAR(5), \
        place_6 VARCHAR(5), \
        place_7 VARCHAR(5), \
        place_8 VARCHAR(5), \
        place_9 VARCHAR(5), \
        place_10 VARCHAR(5), \
        simple_gagnant VARCHAR(10), \
        simple_place VARCHAR(10), \
        tierce_ordre VARCHAR(10), \
        tierce_desordre VARCHAR(10), \
        quarte_ordre VARCHAR(10), \
        quarte_desordre VARCHAR(10), \
        quinte_ordre VARCHAR(10), \
        quinte_desordre VARCHAR(10))")    
   except mdb.Error, e:  
     print "Error %d: %s" % (e.args[0],e.args[1])
     sys.exit(1)    
   finally:            
     if con:    
        con.close()


def tosql_insert(data,cur,table_name):

  if (type(data[0]) != tuple) and (type(data[0]) != list):    
     result="'"+",".join(str(item) for item in data)+"'"
     cur.execute("""insert into %s values (%s);""",(table_name,result))	    

  else: 
     for row in data:  
         result="'"+",".join(str(item) for item in data)+"'"
         cur.execute("""insert into %s values (%s);""",(table_name,result))		

