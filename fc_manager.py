def get_feature_type(feature_code):
    if 1:
        return f'POINT'
    if 2:
        return f'POLYLINE'
    if 3:
        return f'POLYGON'
    else:
        return f'None'