import countdown as c

def test_countdown_for_10():
    """Tests for loop in countdown.py with default value; i.e. no argument."""
    c.get_countdown_as_text_using_for()

def test_countdown_for_5():
    """Tests for loop in countdown.py with starting value of 5."""
    count_from = 5
    c.get_countdown_as_text_using_for(count_from)

def test_countdown_while_10():
    """Tests for while in countdown.py with default value; i.e. no argument."""
    c.get_countdown_as_text_using_while()

def test_countdown_while_5():
    """Tests for while in countdown.py with starting value of 5."""
    count_from = 5
    c.get_countdown_as_text_using_while(count_from)

test_countdown_for_10()
test_countdown_for_5()
test_countdown_while_10()
test_countdown_while_5()