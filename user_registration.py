import cv2
import os
from deepface import DeepFace
from utils import add_user  # Assuming add_user is correctly imported
import re

# Ensure captured_images directory exists
os.makedirs("captured_images", exist_ok=True)

def user_registration():
    name = input("Enter your full name: ")
    account_number = input("Enter your account number: ")

    print("\nPlease ensure your face is visible and press SPACE to capture your face...")

    cap = cv2.VideoCapture(0)

    # Check if webcam is successfully opened
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    max_attempts = 10
    attempts = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            attempts += 1
            if attempts >= max_attempts:
                print("Error: Could not capture frame from webcam.")
                break
            continue

        cv2.imshow("Press SPACE to register your face or press 'q' to cancel", frame)

        key = cv2.waitKey(10) & 0xFF  # Changed waitKey to 10 for better responsiveness
        if key == ord(' '):  # SPACE key pressed
            # Sanitize account number for filename
            account_number_safe = re.sub(r'[^a-zA-Z0-9]', '_', account_number)
            image_path = f"captured_images/{account_number_safe}.jpg"
            cv2.imwrite(image_path, frame)
            print("\nFace image captured successfully.")

            # Use DeepFace to extract faces from the captured image
            try:
                # Extract face(s) from the image (returns a list of faces)
                faces = DeepFace.extract_faces(img_path=image_path, detector_backend='opencv')
                
                # Check if any face was extracted
                if faces:
                    print("Face extracted successfully.")
                else:
                    print("No faces detected in the image.")
            except Exception as e:
                print(f"Error during face extraction: {e}")

            try:
                add_user(name, account_number, image_path)
                print("\nUser registration completed successfully!")
            except Exception as e:
                print(f"Error during user registration: {e}")

            break  # Exit the loop once user registration is completed

        elif key == ord('q'):  # 'q' key pressed
            print("\nRegistration canceled.")
            break

    # Ensure cleanup even in case of errors
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    user_registration()
