import fc_manager as FC

def test_get_feature_type_1():
    feature_code = 1
    expected = 'POINT'
    actual = FC.get_feature_type(feature_code)
    print (actual)
    assert actual == expected 

def test_get_feature_type_2():
    feature_code = 2
    expected = 'POLYLINE'
    actual = FC.get_feature_type(feature_code)
    print (actual)
    assert actual == expected 

def test_get_feature_type_3():
    feature_code = 3
    expected = 'POLYGON'
    actual = FC.get_feature_type(feature_code)
    print (actual)
    assert actual == expected  

def test_get_feature_type_0():
    feature_code = 0
    expected = 'None'
    actual = FC.get_feature_type(feature_code)
    print (actual)
    assert actual == expected  

test_get_feature_type_1()
test_get_feature_type_2()
test_get_feature_type_3()
test_get_feature_type_0()