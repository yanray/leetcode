"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_times = dict()
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        # logging timeout in seconds
        TIMEOUT = 10
        # the following three cases are possible
        # 1) the message has not been printed before -> true
        if message not in self.log_times:
            # create a log in the hashmap
            self.log_times.update({message: timestamp})
            return True
        
        else:
            # 2) the message has been printed before and the timer has expired -> true
            if timestamp - self.log_times[message] >= TIMEOUT:
                self.log_times.update({message: timestamp})
                return True
            # 3) the message has been printed before and timer has not expired -> false
            else:
                return False


if __name__ == '__main__':

    logger = Logger()

    print(logger.shouldPrintMessage(1, "foo"))
    print(logger.shouldPrintMessage(2, "bar"))
    print(logger.shouldPrintMessage(3, "foo"))
    print(logger.shouldPrintMessage(8, "bar"))
    print(logger.shouldPrintMessage(10, "foo"))
    print(logger.shouldPrintMessage(11, "foo"))


    
