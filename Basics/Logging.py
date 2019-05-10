# Logging in python

import logging

logging.basicConfig(filename = 'programLogs.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')   # Define type of logs to be printed (info,debug,error etc)
logging.info('INFO -- Start of program')
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program\n')
logging.info('INFO -- End of program\n')
