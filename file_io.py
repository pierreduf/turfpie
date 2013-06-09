import os
import datetime
import sys

import parse_pronos

def write_infos_chevaux(pron_file,out_file)


pronos_file = open(pron_file, 'r')
infos_chevaux = open(out_file, 'w')

for line in pronos_file:
	chevaux_result = parse_pronos.parse_infos_chevaux(line)
	chevaux = chevaux_result[0]
	nb_errors = nb_errors + chevaux_result[1]
	for cheval in chevaux :
		infos_chevaux.write(";".join(str(item) for item in cheval))
		infos_chevaux.write('\n')

pronos_file.close()
infos_chevaux.close()
