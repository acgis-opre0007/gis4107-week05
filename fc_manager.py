def get_feature_type(feature_code):
    if feature_code == 1:
        return f'POINT'
    if feature_code == 2:
        return f'POLYLINE'
    if feature_code == 3:
        return f'POLYGON'
    else:
        return f'None'
