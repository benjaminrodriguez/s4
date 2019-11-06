import logging

FORMAT = '%(asctime)s %(clientip)s %(user)s %(message)s'
logging.basicConfig(format=FORMAT)

d = {
    'clientip': '192.168.0.1',
    'user': 'toto'
}

# Crée un logger ou récupère le logger 'tcpserver' s'il a déjà été crée
logger = logging.getLogger('tcpserver')

logger.warning('Protocol problem: %s','connection reset' , extra=d)
