def bears(n: int) -> bool:
    """
    Docstring for bears: Given a random number, n, Try to get the number to 42
    
    :param n: Description
    :type n: int
    :return: Description
    :rtype: bool
    """
    #Base Cases
    if n == 42: 
        return True
    if n < 42: 
       return False 

    #rest
    if n % 5 == 0:
        if bears(n-42):
            return True 
    if n%2 == 0:
        if bears(n//2):
            return True
        
    if n%3 == 0 or n % 4 == 0 and n >= 10: 
        digits = n % 100
        tens = digits // 10
        ones = digits % 10 
        product = (ones*tens)
        if product > 0:
            if bears(n - product):  
                return True 
        


    return False 