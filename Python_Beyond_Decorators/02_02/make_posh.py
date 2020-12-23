def make_posh(func):
    def wrapper():
        return '+---------+\n|         |\n Fibonacci \n|         |\n+=========+'
    return wrapper
 
@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '

print(pfib())