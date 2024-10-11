import cv2
from work_with_db import WorkWithDB

db = WorkWithDB()


# Function to get the color at the given point (x, y)
def get_color_at_point(img, x, y):
    # Get the BGR color at the given (x, y) point
    b, g, r = img[y, x]
    return b, g, r


# Load the image
img = cv2.imread('xyz.jpg')
# img = cv2.imread('abc.jpg')


all_coords = db.get_all_coords()

for coord in all_coords:
    color_a = get_color_at_point(img, coord[1], coord[2])
    color_b = get_color_at_point(img, coord[3], coord[4])
    color_c = get_color_at_point(img, coord[5], coord[5])
    color_d = get_color_at_point(img, coord[7], coord[8])

    if color_a[0] < 100 and color_a[1] < 100 and color_a[2] < 100:
        print(f"{coord[0]} ==> A")
    elif color_b[0] < 100 and color_b[1] < 100 and color_b[2] < 100:
        print(f"{coord[0]} ==> B")
    elif color_c[0] < 100 and color_c[1] < 100 and color_c[2] < 100:
        print(f"{coord[0]} ==> C")
    elif color_d[0] < 100 and color_d[1] < 100 and color_d[2] < 100:
        print(f"{coord[0]} ==> D")
    else:
        sums = [sum(color_a), sum(color_b), sum(color_c), sum(color_d)]

        ans = min(sums)

        if ans == sums[0]:
            print(f"{coord[0]} ==> A")
        elif ans == sums[1]:
            print(f"{coord[0]} ==> B")
        elif ans == sums[2]:
            print(f"{coord[0]} ==> C")
        elif ans == sums[3]:
            print(f"{coord[0]} ==> D")
        else:
            print("\nERROR!")
            print(coord)
            print(f"{color_a}\t|\t{color_b}\t|\t{color_c}\t|\t{color_d}")
            print(f"{sum(color_a)}\t|\t{sum(color_b)}\t|\t{sum(color_c)}\t|\t{sum(color_d)}\n")

    # sums = [sum(color_a), sum(color_b), sum(color_c), sum(color_d)]
    #
    # ans = min(sums)
    #
    # if ans == sums[0]:
    #     print(f"{coord[0]} ==> A")
    # elif ans == sums[1]:
    #     print(f"{coord[0]} ==> B")
    # elif ans == sums[2]:
    #     print(f"{coord[0]} ==> C")
    # elif ans == sums[3]:
    #     print(f"{coord[0]} ==> D")
    # else:
    #     print("\nERROR!")
    #     print(coord)
    #     print(f"{color_a}\t|\t{color_b}\t|\t{color_c}\t|\t{color_d}")
    #     print(f"{sum(color_a)}\t|\t{sum(color_b)}\t|\t{sum(color_c)}\t|\t{sum(color_d)}\n")


# # Check if the point is within the image dimensions
# if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
#     # Get the color at the specified point
#     b, g, r = get_color_at_point(img, x, y)
#     print(f"Color at point ({x}, {y}) -> B: {b}, G: {g}, R: {r}")
# else:
#     print(f"Point ({x}, {y}) is outside the image bounds")


