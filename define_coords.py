import cv2

# Mouse callback function to capture the click event
def click_event(event, x, y, flags, params):
    # Check if the event is a left mouse button click
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print the coordinates of the point
        print(f"Clicked at: ({x}, {y})")
        # Optionally, you can draw a small circle at the clicked point
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow('Image', img)

# Load the image
img = cv2.imread('abc.jpg')

# Create a window to display the image
cv2.imshow('Image', img)

# Set the mouse callback function to capture the click events
cv2.setMouseCallback('Image', click_event)

# Wait for a key press indefinitely or until a key is pressed
cv2.waitKey(0)

# Destroy all the windows after the key press
cv2.destroyAllWindows()
