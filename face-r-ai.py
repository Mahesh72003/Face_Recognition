import face_recognition
import cv2

# Load images and encode faces
person_1_image = face_recognition.load_image_file(r"D:\mahesh2003\mahesh intership\intership by devminds\project\project\mahesh.jpg")
person_1_encoding = face_recognition.face_encodings(person_1_image)[0]

person_2_image = face_recognition.load_image_file(r"D:\mahesh2003\mahesh intership\intership by devminds\project\project\Person_3.jpg")
person_2_encoding = face_recognition.face_encodings(person_2_image)[0]

person_3_image = face_recognition.load_image_file(r"C:\Users\91988\Desktop\WhatsApp Image 2024-07-26 at 11.06.10_9db89e2b.jpg")
person_3_encoding = face_recognition.face_encodings(person_3_image)[0]

person_4_image = face_recognition.load_image_file(r"C:\Users\91988\Desktop\WhatsApp Image 2024-07-26 at 11.07.11_c89e7f6e.jpg")
person_4_encoding = face_recognition.face_encodings(person_4_image)[0]

known_encodings = [
    person_1_encoding,
    person_2_encoding,
    person_3_encoding,
    person_4_encoding
]

known_names = [
    "Mahesh A V",
    "Bharath V",
    "lakshmiprasad v",
    "Abhishek G"
]

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    
    # Find faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Compare faces with known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Draw a rectangle around the face and label it
        top, right, bottom, left = face_recognition.face_locations(frame)[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
