# log_decorator
Managing logs effectively is crucial for debugging and monitoring applications. Python provides the logging module for this purpose, and you can use decorators to create a custom log management system. Here's an example of a Python decorator for logging:

```
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
        
        # Log the result, if applicable
        logging.info(f'Function result: {result}')
        
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
result1 = add(5, 3)
result2 = subtract(10, 4)
```

In this example:

We configure the logging module to log messages to a file named 'app.log' with a minimum logging level of INFO. We also define a custom log message format.

We create a decorator function log_function_call. This decorator logs the function name before calling the original function and logs the result afterward.

The wrapper function within the decorator captures any arguments and keyword arguments passed to the original function, calls the original function, logs the function name and result, and returns the result.

We apply the @log_function_call decorator to the add and subtract functions.

When we call add(5, 3) and subtract(10, 4), the decorator logs information about these function calls and their results.

This is a basic example of using a Python decorator for logging function calls. You can customize it further to suit your specific logging requirements, such as adding timestamps, log levels, or handling exceptions.
