
def get_countdown_as_text_using_for(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a for loop
    """
    result = ''
    for x in range(start_value,-1,-1):
       result += f'{x} '
    return result

def get_countdown_as_text_using_while(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0 using a while loop
    """
    result = ''
    while start_value > -1:
      result += f'{start_value} '
      start_value -= 1
    return result

print(get_countdown_as_text_using_for())
print(get_countdown_as_text_using_while())