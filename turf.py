import os
import datetime
import sys

import get_links
import parse_pronos
import parse_infos_course
import recup_id_chevaux
import parse_results
import tosql
import tofile

out_folder = "output/"

def prompt():
  choice = "0"	
  while 1:
    print """Choix recuperation donnees :
	    1. Infos courses
	    2. Identites chevaux
            3. Pronostics courses
            4. Resultats courses
            5. Effacer tables
          """
    choice = raw_input(">>> ")
    if (choice != "1") and (choice != "2") and (choice != "3") and (choice != "4")\
       and (choice != "5"):
	continue
    else:
	break        
  return choice


choice=prompt()

# RECUPERER INFOS COURSES

if choice == "1":
    debut = raw_input("> Date debut (aaaa-mm-jj) : ")
    fin = raw_input("> Date fin (aaaa-mm-jj) : ")

    mode = raw_input(">> Mode (SQL/FIL) : ") 

    try:
      get_links.get_course_links_range(\
	debut,\
	fin,\
	out_folder+'pronos_urls',\
	out_folder+'results_url')
    except:
      print("Mauvais format de date !")
      sys.exit(1)

    if mode == "SQL":
     pronos_file = open(out_folder+'pronos_urls', 'r')
     tosql.create_table('infos_course')
     con=tosql.get_con()

     for line in pronos_file:
         detail_course = parse_infos_course.parse_infos_course(line)
         tosql.tosql_insert(detail_course,con.cursor(),'infos_course')
     con.commit()

     if con:
        con.close()
     if pronos_file:
        pronos_file.close()
     print("OK !")

    elif mode == "FIL":
     pronos_file = open(out_folder+'pronos_urls', 'r')
     
     os.system("rm "+out_folder+"infos_course")
          
     for line in pronos_file:
         detail_course = parse_infos_course.parse_infos_course(line)
         tofile.tofile_write(detail_course,out_folder+'infos_course')
    
     if pronos_file:
        pronos_file.close()
     print("OK !")


    else:
	print ("Mauvais format !")


# RECUPERER INFOS CHEVAUX

elif choice == "2":
    mini = 107
    maxi = recup_id_chevaux.find_max_id()

    mini_user = raw_input("> Mini (defaut 107) : ")
    if (mini_user != "") and (int(mini_user) > 107):
       mini = int(mini_user)

    maxi_user = raw_input("> Maxi (defaut "+str(maxi)+") : ")
    if (maxi_user != "") and (int(maxi_user) < maxi):
       maxi = int(maxi_user)

    tosql.create_table('id_chevaux')
    con=tosql.get_con()
    chevaux = recup_id_chevaux.get_id_chevaux(mini,maxi)
    tosql.tosql_insert(chevaux[0],con.cursor(),'id_chevaux')
    con.commit()
    if con:
       con.close()
    print ("OK !")
    

elif choice == "3":

    debut = raw_input("> Date debut (aaaa-mm-jj) : ")
    fin = raw_input("> Date fin (aaaa-mm-jj) : ")
    try:
      get_links.get_course_links_range(\
	debut,\
	fin,\
	out_folder+'pronos_urls',\
	out_folder+'results_url')
    except:
      print("Mauvais format de date !")
      sys.exit(1)

    pronos_file = open(out_folder+'pronos_urls', 'r')
    tosql.create_table('pronos_course')
    con=tosql.get_con()

    for line in pronos_file:
        pronos_course = parse_pronos.parse_infos_chevaux(line)
        tosql.tosql_insert(pronos_course[0],con.cursor(),'pronos_course')
    con.commit()

    if con:
       con.close()
    if pronos_file:
       pronos_file.close()
    print("OK !")


elif choice == "4":

    debut = raw_input("> Date debut (aaaa-mm-jj) : ")
    fin = raw_input("> Date fin (aaaa-mm-jj) : ")
    try:
      get_links.get_course_links_range(\
	debut,\
	fin,\
	out_folder+'pronos_urls',\
	out_folder+'results_url')
    except:
      print("Mauvais format de date !")
      sys.exit(1)

    results_file = open(out_folder+'results_url', 'r')
    tosql.create_table('results_course')
    con=tosql.get_con()

    for line in results_file:
        resultats = parse_results.parse_results(line)
        tosql.tosql_insert(resultats[0],con.cursor(),'results_course')
    con.commit()

    if con:
       con.close()
    if results_file:
       results_file.close()
    print("OK !")


elif choice == "5":
   tosql.delete_table("infos_course")
   tosql.delete_table("id_chevaux")
   tosql.delete_table("pronos_course")
   tosql.delete_table("results_course")
   print("OK !")
