import cv2

# Try to read the image
img = cv2.imread("./tryy.png")

# Check if the image was successfully loaded
if img is None:
    print("Error: Could not open or find the image.")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    lowerbody_cascade = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
    
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=2)
    lowerbodies = lowerbody_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=1)
    
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
        
    for x, y, w, h in lowerbodies:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
    cv2.imshow("Gray", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
