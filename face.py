import face_recognition
import cv2
import numpy as np
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('atm_users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, face_encoding BLOB)')
    conn.commit()
    conn.close()

# Function to register a face
def register_face(name):
    video_capture = cv2.VideoCapture(0)
    print("Press 'q' after positioning your face...")

    while True:
        ret, frame = video_capture.read()
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            face_locations = face_recognition.face_locations(frame)
            if face_locations:
                face_encodings = face_recognition.face_encodings(frame, face_locations)
                face_encoding = face_encodings[0]

                conn = sqlite3.connect('atm_users.db')
                c = conn.cursor()
                c.execute('INSERT INTO users (name, face_encoding) VALUES (?, ?)', (name, face_encoding.tobytes()))
                conn.commit()
                conn.close()

                print(f"Face registered for {name}.")
                break
            else:
                print("No face detected. Please try again.")

    video_capture.release()
    cv2.destroyAllWindows()

# Function to authenticate a face
def authenticate_face():
    conn = sqlite3.connect('atm_users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()

    video_capture = cv2.VideoCapture(0)
    print("Look at the camera to authenticate...")

    while True:
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            for user in users:
                name, db_face_encoding = user
                db_face_encoding = np.frombuffer(db_face_encoding, dtype=np.float64)

                match = face_recognition.compare_faces([db_face_encoding], face_encoding)
                if match[0]:
                    print(f"Authentication successful! Welcome {name}.")
                    video_capture.release()
                    cv2.destroyAllWindows()
                    return name

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    print("Authentication failed!")
    return None

# ATM operations
def atm_operations(name):
    user_data = {'John': 1000, 'Doe': 1500}  # Replace with database integration

    print(f"Welcome {name}!")
    while True:
        print("\n1. Check Balance\n2. Withdraw Cash\n3. Add Money\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Your balance is: ${user_data.get(name, 0)}")
        elif choice == '2':
            amount = int(input("Enter withdrawal amount: "))
            if amount <= user_data.get(name, 0):
                user_data[name] -= amount
                print(f"Withdrawal successful. Remaining balance: ${user_data[name]}")
            else:
                print("Insufficient balance.")
        elif choice == '3':
            amount = int(input("Enter amount to add: "))
            if name in user_data:
                user_data[name] += amount
            else:
                user_data[name] = amount
            print(f"Money added successfully. New balance: ${user_data[name]}")
        elif choice == '4':
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Try again.")

# Main function
def main():
    setup_database()
    print("Welcome to Face Recognition ATM!")
    print("1. Register\n2. Login")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter your name: ")
        register_face(name)
    elif choice == '2':
        user_name = authenticate_face()
        if user_name:
            atm_operations(user_name)
    else:
        print("Invalid option.")

if _name_ == "_main_":
    main()