# create folders for output files generated during the de novo hybrid assembly pipeline

import os

configfile = open('config.yaml', 'r').read()
liste = configfile.split('\n')
for elem in liste[:]:
    if elem == '' or elem[0] == '#' or elem[0:3] == 'ref':
        liste.remove(elem)

if liste[0][:5] == 'path:':
    path = liste[0][7:len(liste[0]) - 1]
    if os.path.exists(path) == False:
        os.mkdir(path)
    liste.pop(0)
else:
    path = os.getcwd()
os.mkdir(path + '/raw_data')
os.mkdir(path + '/annotation')
os.mkdir(path + '/ideel')
for i in range(len(liste)):
    parameter = liste[i].split(': ', 1)
    details = parameter[1]
    parameter = parameter[0]
    details = details.split(', ')
    details[0] = details[0][1:len(details[0])]
    details[len(details) - 1] = details[len(details) - 1][0:len(details[len(details) - 1]) - 1]
    if parameter == 'strains':
        strains = details
    if parameter == 'preprocessing_short':
        os.mkdir(path + '/preprocessing')
        os.mkdir(path + '/preprocessing/illumina/')
        preprocessing_short = details
    if parameter == 'demultiplexing':
        demultiplexing = details
    if parameter == 'assembly':
        os.mkdir(path + '/' + parameter)
        assembly = details
    if parameter == 'postprocessing':
        os.mkdir(path + '/' + parameter)
        postprocessing = details
    if parameter == 'quality':
        os.mkdir(path + '/' + parameter)
        quality = details
for elem in strains[:]:
    if elem[0:6] == 'strain':
        strains.remove(elem)
    else:
        strains[strains.index(elem)] = elem.split(': ')[0]
for preprocesser in preprocessing_short:
    os.mkdir(path + '/preprocessing/illumina/' + preprocesser)
for demultiplexer in demultiplexing:
    os.mkdir(path + '/preprocessing/' + demultiplexer)
    for bacteria in strains:
        for assembler in assembly:
            os.mkdir(path + '/assembly' + '/' + bacteria + '_' + demultiplexer + '_' + assembler)
            os.mkdir(path + '/postprocessing' + '/' + bacteria + '_' + demultiplexer + '_' + assembler)
            os.mkdir(path + '/annotation' + '/' + bacteria + '_' + demultiplexer + '_' + assembler)
for check in quality:
    os.mkdir(path + '/quality' + '/' + check)
    if check != 'quast':
        for bacteria in strains:
            os.mkdir(path + '/quality' + '/' + check + '/' + bacteria)
