# T051
# Date: 12/04/2022
# Version: 1.0
# Active members
# Leena Ford 101229281 
# Isabella Fotia 101228368 
# Umayer Joarder 101227396 
# Espen Swift 101232582 

def check_equal(description: str, outcome, expected) -> bool:
    """
    Returns the results of a test. If the test passes, "PASSED" is displayed. Otherwise, "FAILED" is displayed with the details of the output. 
    
    "description" describes the function call of the function we are testing.
    
    The actual value returned from the function that we're testing is the 'outcome' (actual) 
    and the 'expected' value is what we predict the function should return. 
    
    Preconditions: both the parameters should be the same type. This function should 
    not be used to evaluate whether or not floats/lists of floats/tuples of floats are equal. 
    
    Examples 
    >>> check_equal('A working function that returns the sum of x and y if x = 9 and y = 10', sum_function(9,10), 19)
    A working function that returns the sum of x and y if x = 9 and y = 10 PASSED
    
    >>> check_equal('A non-working function that returns the sum of x and y if x = 9 and y = 10', sum_function(9,10), 19)
    A non-working function that returns the sum of x and y if x = 9 and y = 10 FAILED: expected 19, got # 
    
    """
   
    
    outcome_type = type(outcome)
    expected_type = type(expected)
    
    if outcome_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return False
    
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return False
    
    else:
        print("{0} PASSED".format(description))
        return True
        
    print("------")
