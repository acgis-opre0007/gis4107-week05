def is_point_in_box(x,y,xmin,xmax,ymin,ymax):
    if (x > xmin) and (x < xmax) and (y > ymin) and (y < ymax):
        return("True")
    else:
        return("False")