import cv2
from work_with_db import WorkWithDB

db = WorkWithDB()

coords = [0, 0, 0, 0, 0, 0, 0, 0]
i = 0

# Mouse callback function to capture the click event
def click_event(event, x, y, flags, params):
    # Check if the event is a left mouse button click
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the color (BGR) at the clicked point
        b, g, r = img[y, x]

        global coords, i
        if i < len(coords) - 1:
            coords[i], coords[i+1] = x, y
            i += 2
        else:
            print(coords)
            # print(db.insert_coords(coords))
            coords[0], coords[1] = x, y
            i = 2

        # Print the coordinates and the color of the point
        print(f"Clicked at: ({x}, {y}), Color: (B: {b}, G: {g}, R: {r})")

        # Optionally, draw a small circle at the clicked point and display it
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Green circle
        cv2.imshow('Image', img)


# Load the image
img = cv2.imread('abc.jpg')

# Create a window to display the image
cv2.imshow('Image', img)

# Set the mouse callback function to capture click events
cv2.setMouseCallback('Image', click_event)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Destroy all windows after the key press
cv2.destroyAllWindows()
