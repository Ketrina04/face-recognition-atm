Face Recognition ATM System
Overview

Face Recognition ATM System is a biometric authentication application built in Python that replaces traditional PIN-based ATM verification with real-time facial recognition. The system captures a user’s face through a webcam, generates facial embeddings using a deep learning model, and authenticates identity by comparing live embeddings against stored records in a SQLite database.

This project demonstrates the integration of computer vision, deep learning-based feature extraction, database management, and secure authentication logic into a cohesive real-time system.

Problem Context

Conventional ATM systems rely on PIN-based authentication, which can be compromised through shoulder surfing, skimming, or credential theft. This project explores biometric authentication as a more secure and user-friendly alternative by implementing facial recognition as the primary verification mechanism.

Key Features

• Real-time face detection using OpenCV
• Facial embedding generation using DeepFace (OpenFace model)
• Euclidean distance-based similarity comparison
• Persistent user storage using SQLite
• Modular and structured Python implementation
• Webcam-based real-time processing pipeline
• ATM simulation with balance enquiry, withdrawal, and deposit

System Workflow

User Registration Phase
The user enters name and account number. The system captures a facial image using the webcam, extracts a facial embedding, and stores account details along with the image path in the SQLite database.

Authentication Phase
During login, the webcam captures a live frame. The face is detected and converted into a numerical embedding. This embedding is compared against stored embeddings using vector distance calculations. If the similarity threshold is satisfied, the user is authenticated.

ATM Operations Phase
After successful authentication, the user can check balance, withdraw funds, or add money through a terminal-based interface.

Technology Stack

Programming Language: Python 3.x
Computer Vision: OpenCV
Face Recognition: DeepFace, face_recognition
Numerical Computation: NumPy
Database: SQLite3

Project Structure

The project contains separate modules for user registration, real-time recognition, ATM operations, database setup, utility functions, and user viewing. It follows a modular structure to separate authentication logic, recognition logic, and database handling for maintainability and clarity.

Installation and Setup

First, clone the repository by running: git clone https://github.com/YOUR_USERNAME/face-recognition-atm.git
 and then navigate into the project directory using cd face-recognition-atm.

Create a virtual environment using python -m venv venv. Activate it on Windows using venv\Scripts\activate or on Mac/Linux using source venv/bin/activate.

Install required dependencies using pip install opencv-python deepface face_recognition numpy tensorflow.

Ensure that two folders exist inside the project directory: captured_images and database. If they do not exist, create them manually.

The SQLite database will be created automatically during user registration.

Running the Application

To register a new user, run python user_registration.py and follow the instructions to capture the face image.

To start real-time recognition, run python real_time.py.

To launch the ATM login interface, run python face.py and choose the appropriate option for registration or login.

Security Considerations

Authentication is based on biometric embeddings rather than passwords. Identity verification is performed using numerical vector similarity comparison. User data is stored locally in a SQLite database.

However, the current implementation does not include database encryption or liveness detection mechanisms.

Limitations

Recognition accuracy depends on lighting conditions and camera quality.
The system does not implement anti-spoofing or liveness detection.
The interface is terminal-based rather than graphical.
Database encryption is not implemented.

Future Enhancements

• Add liveness detection to prevent spoofing attacks
• Implement encrypted database storage
• Develop a GUI using Tkinter or PyQt
• Add transaction history logging
• Improve model accuracy and threshold tuning
• Package as a standalone desktop application

Placement Relevance

This project demonstrates practical understanding of computer vision pipelines, facial embedding representation, real-time video processing, database integration, modular software design, and applied AI system development. It reflects the ability to design and implement an end-to-end biometric authentication system rather than isolated algorithmic components.
