def mod_sequence(seq,skip_index=None,truncate_index=None):
    """
    Given a string, returns a version that has been truncated and had some character omitted.
    seq -- initial string
    skip_index -- the position of the character to be omitted
    truncate_index -- the position before which to truncate the string; ignored when equal to or greater
        than initial string length
    """

    seq_length = len(seq)
    result = ''
    if truncate_index == None or truncate_index >= (seq_length):
        start_value = 0
    else:
        start_value = truncate_index

    for x in range(start_value,seq_length):
        if x == skip_index:
            continue
        else:
            result += seq[x]
    
    return result

print(mod_sequence("ABCD",None,3))