from deepface import DeepFace
import cv2
import os
import numpy as np
def load_registered_faces(captured_dir):
    registered_faces = {}
    for filename in os.listdir(captured_dir):
        if filename.endswith(".jpg"):
            path = os.path.join(captured_dir, filename)
            try:
                embedding_result = DeepFace.represent(
                    img_path=path, model_name="OpenFace", enforce_detection=False
                )
                
                account_number = filename.split(".")[0]  
                registered_faces[account_number] = embedding_result[0]["embedding"]
            except Exception as e:
                print(f"Could not process {path}: {e}")
    return registered_faces

def match_face(face_embedding, registered_faces, threshold=0.5):
    for account_number, embedding in registered_faces.items():
        try:
            face_embedding = np.array(face_embedding)
            embedding = np.array(embedding)

            
            distance = np.linalg.norm(face_embedding - embedding)
            if distance < threshold:  
                return account_number
        except Exception as e:
            print(f"Error comparing embeddings: {e}")
    return None

def recognize_faces_in_realtime(registered_faces):
    # Start webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot access webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

      
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_img = frame[y:y + h, x:x + w]
            try:
                face_embedding_result = DeepFace.represent(
                    img_path=face_img,
                    model_name="OpenFace",
                    enforce_detection=False,
                )
                face_embedding = face_embedding_result[0]["embedding"]

                matched_account = match_face(face_embedding, registered_faces)
                if matched_account:
                    cv2.putText(
                        frame,
                        f"User: {matched_account}",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )
                else:
                    cv2.putText(
                        frame,
                        "Unknown",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 0, 255),
                        2,
                    )
            except Exception as e:
                print(f"Error processing detected face: {e}")

        # Display the webcam feed
        cv2.imshow("Face Recognition Stream", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

captured_images_dir = "captured_images"
print("Loading registered user embeddings...")
registered_faces = load_registered_faces(captured_images_dir)
print(f"Loaded embeddings for {len(registered_faces)} registered users.")

recognize_faces_in_realtime(registered_faces)
