import geom_utils as gu

xmin = 1
xmax = 3
ymin = 1
ymax = 3

def test_is_point_in_box_left_outside():
    x = 0
    y = 2
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))

def test_is_point_in_box_left_edge():
    x = 1
    y = 2
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))
   
def test_is_point_in_box_above_outside():
    x = 2
    y = 4
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))
   
def test_is_point_in_box_top_edge():
    x = 2
    y = 3
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))
   
def test_is_point_in_box_right_outside():
    x = 4
    y = 2
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))
   
def test_is_point_in_box_right_edge():
    x = 3
    y = 2
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))
   
def test_is_point_in_box_below_outside():
    x = 2
    y = 0
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))
   
def test_is_point_in_box_bottom_edge():
    x = 2
    y = 1
    print("Expected: False")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))
   
def test_is_point_in_box_inside():
    x = 2
    y = 2
    print("Expected: True")
    print("Actual:" + (gu.is_point_in_box(x,y,xmin,xmax,ymin,ymax)))

test_is_point_in_box_left_outside()
test_is_point_in_box_left_edge()
test_is_point_in_box_above_outside()
test_is_point_in_box_top_edge()
test_is_point_in_box_right_outside
test_is_point_in_box_right_edge
test_is_point_in_box_below_outside()
test_is_point_in_box_bottom_edge()
test_is_point_in_box_inside()