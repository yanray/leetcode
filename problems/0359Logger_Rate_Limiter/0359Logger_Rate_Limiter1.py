"""

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.log_dict:
            self.log_dict[message] = timestamp
            return True
        else:
            if timestamp - self.log_dict[message] >= 10:
                self.log_dict[message] = timestamp
                return True
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


    
