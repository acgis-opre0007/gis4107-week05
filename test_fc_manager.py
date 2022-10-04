import fc_manager as FC

test_get_feature_type<POINT>:
    feature_code = 1
    expected: 'POINT'
    actual: FC.get_feature_type(1)
    

test_get_feature_type<POLYLINE>:
    expected: 'POLYLINE'
    actual: FC.get_feature_type(2)

test_get_feature_type<POLYGON>:
    expected: 'POLYGON'
    actual: FC.get_feature_type(3)

test_get_feature_type<NONE>
    expected: 'none'
    actual: FC.get_feature_type(4)