import logging


class LoggerDemoConsole:
    def print_log(self):
        # create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        # add formatter to console handler
        console_handler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(console_handler)

        # logging messages
        logger.debug('debug msg')
        logger.info('info msg')
        logger.warning('warning msg')
        logger.error('error msg')
        logger.critical('critical msg')


demo = LoggerDemoConsole()
demo.print_log()