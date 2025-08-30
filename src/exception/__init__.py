import os 
import sys

def error_message_detail(error,error_detail):
    try:
        _,_, exc_tb =error_detail.exc_info()

        if exc_tb is None:
            return f"Error: {str(error)}"
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        line_number = exc_tb.tb_lineno
        function_name = exc_tb.tb_frame.f_code.co_name
        error_message = f"Error occurred in file: {file_name}, line: {line_number}, function: {function_name}"
        return error_message
    except Exception as e:
        return f"error: {str(e)}"

class ForestException(Exception):
    def __init__(self, error_message,error_detail=sys):
        super().__init__(error_message)
        self.error_detail = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_detail