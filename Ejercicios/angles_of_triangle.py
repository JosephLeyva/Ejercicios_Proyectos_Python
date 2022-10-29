'''
EXERCISE: Write a metjpd that takes as input two integers representing two angles of a triangle,
and computes the third angle
'''


def determining_3rd_angle_triangle(first_angle, second_angle):
    total = 180
    return total - first_angle - second_angle


print(determining_3rd_angle_triangle(60, 80))
