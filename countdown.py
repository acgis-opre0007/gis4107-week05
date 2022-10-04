
def get_countdown_as_text_using_for(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a for loop
    """

    for x in range(start_value,-1,-1):
      print(x)

def get_countdown_as_text_using_while(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a while loop
    """
    
    while start_value > -1:
      print(start_value)
      start_value -= 1
