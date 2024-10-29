## The sys module in Python provides access to functions and variables that interact closely with the Python interpreter. 
# It’s commonly used for interacting with the runtime environment, managing input/output streams,
#  handling command-line arguments, and modifying the import path.
import sys
import logging
## error_detail will be available in sys module which is imported
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    ## refer to this link to understand the below line of code: https://docs.python.org/3/tutorial/errors.html
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_details)
    
    def __str__(self):
        return self.error_message

## to check if custom exception is working
# if __name__=='__main__':
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e,sys)

    



