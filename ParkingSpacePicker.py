import cv2
import pickle

width, height = 107, 48

# Try to load existing positions
try:
    with open("CarParkPos.pkl", "rb") as f:
        poslist = pickle.load(f)
except FileNotFoundError:
    poslist = []  # Initialize empty if file does not exist

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(poslist):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                poslist.pop(i)
                break

    # Save updated positions
    with open("CarParkPos.pkl", "wb") as f:
        pickle.dump(poslist, f)

while True:
    img = cv2.imread('carParkImg.png')
    if img is None:
        print("Error: 'carParkImg.png' not found.")
        break

    for pos in poslist:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing 'Esc'
        break

cv2.destroyAllWindows()

