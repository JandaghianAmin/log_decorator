import logging

# Configure the logging module
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Decorator function for logging
def log_function_call(func):
    def wrapper(*args, **kwargs):
        # Log the function call
        logging.info(f'Calling function: {func.__name__}')
        
        # Call the original function and capture its return value
        result = func(*args, **kwargs)
        
        ar = ''
        for i in args:
            ar = ar + str(i) + ' '
        # Log the result, if applicable
        logging.info(f'Function args is:{ar} and result: {result}')
        
        return result
    
    return wrapper

# Usage of the decorator
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def subtract(a, b):
    return a - b

# Test the decorated functions
result1 = add(8, 6)
result2 = subtract(9, 3)
