import logging
import logging.config


class LoggerDemoConf:
    def test_log(self):
        # create logger
        logging.config.fileConfig('logging.conf')
        loggger = logging.getLogger(LoggerDemoConf.__name__)

        # logging messages
        loggger.debug('debug msg')
        loggger.info('info msg')
        loggger.warning('warning msg')
        loggger.error('error msg')
        loggger.critical('critical msg')


demo = LoggerDemoConf()
demo.test_log()