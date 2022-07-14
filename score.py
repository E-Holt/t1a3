keep_adding_points = 0
def point_counter(total_points):
    global keep_adding_points
    keep_adding_points = keep_adding_points + total_points
    print("Your total points are", keep_adding_points,"!")