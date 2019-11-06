import logging

logger = logging.getLogger(__name__)
# Ne fonctionne pas :
#logger.setLevel(logging.INFO)
# A la place, utiliser une fois dans le 'main' :
logging.basicConfig(level=logging.INFO)

def f(a: str):
    logger.warning('Doing something in f')
    print(a)

def g(x: int, y: int):
    z = 2*x + y
    logger.info('Calculating in g...')
    f('The answer is: {}'.format(z))

logger.info('Starting')
g(42, 12)
logger.info('Exiting..')
