import sys, logging, os

try:
    os.chdir('/tmpp2')
except FileNotFoundError:
    logging.error('Fichier non trouvé', exc_info=sys.exc_info())

