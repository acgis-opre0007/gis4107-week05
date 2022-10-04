import modvar as mv

def test_cond1():
    var = 1
    print(5)
    print(mv.mod_myvar(var))

def test_cond2():
    var = 3
    print(2.0)
    print(mv.mod_myvar(var))

def test_cond3():
    var = 2
    print(4)
    print(mv.mod_myvar(var))

def test_cond4():
    var = 12
    print(10)
    print(mv.mod_myvar(var))

test_cond1()
test_cond2()
test_cond3()
test_cond4()
