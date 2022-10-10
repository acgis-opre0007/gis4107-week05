def mod_sequence(seq,skip_index=None,truncate_index=None):
    """
    Given a string, returns a version that has been truncated and had some character omitted.
    seq -- initial string
    skip_index -- the position of the character to be omitted
    truncate_index -- the position at which to truncate the string; ignored when equal to or greater
        than initial string length
    """

    result = ''
    if truncate_index == None or truncate_index >= len(seq):
        end_value = len(seq)
    else:
        end_value = truncate_index

    for x in range(end_value):
        if x == skip_index:
            continue
        else:
            result += seq[x]
    
    return result

#print(mod_sequence("ABCD"))