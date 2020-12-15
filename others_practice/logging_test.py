import logging

logging.basicConfig(filename='testing.log', format='%(asctime)s: %(levelname)s : %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.debug('debug msg')
logging.info('info msg')
logging.warning('warning msg')
logging.error('error msg')
logging.critical('critical msg')
