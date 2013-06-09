
def dict_meteo():

  meteo_list = open('meteo_list','r')
  meteo_dico = {}

  for line in meteo_list:

               meteo_dico[line[:line.find(",")]] = line[line.find(",")+1:len(line)-1]

  meteo_list.close()
  
  return meteo_dico

test = dict_meteo()
