Face Recognition ATM System
Overview

Face Recognition ATM is a Python-based application that simulates secure ATM authentication using facial recognition. The system uses OpenCV for webcam access, DeepFace for face embedding and recognition, and SQLite for storing user data.

Users can register their face, authenticate using real-time recognition, and perform basic ATM operations such as balance enquiry and withdrawal.

Features

User registration with face capture

Real-time face recognition using webcam

SQLite database integration

Secure account identification

Basic ATM operations:

Check balance

Withdraw money

Add money

Stored face embeddings for matching

Account-based image storage

Technologies Used

Python 3.x

OpenCV

DeepFace

face_recognition (in some modules)

NumPy

SQLite3

Project Structure
├── account_interface.py
├── face.py
├── real_time.py
├── setup_database.py
├── user_registration.py
├── utils.py
├── view_users.py
├── database/
├── captured_images/
└── README.md
Installation Guide
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/face-recognition-atm.git
cd face-recognition-atm

Replace YOUR_USERNAME with your GitHub username.

2. Create Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Required Dependencies

Install required libraries:

pip install opencv-python deepface face_recognition numpy

If DeepFace gives errors, ensure you also install:

pip install tensorflow
4. Ensure Folder Structure

Make sure the following folders exist:

captured_images/

database/

If not, create them manually:

mkdir captured_images
mkdir database
Database Setup

The system automatically creates the SQLite database when a user is registered.

Database file location:

database/atm_users.db

If needed, run:

python setup_database.py
How to Run the Project
Option 1: Register a New User
python user_registration.py

Follow on-screen instructions:

Enter name

Enter account number

Press SPACE to capture face

Option 2: Real-Time Face Recognition
python real_time.py

The system will:

Load registered face embeddings

Start webcam

Match detected faces

Option 3: ATM Interface
python face.py

Choose:

Register

Login

If authentication succeeds, ATM options will appear.

Important Notes

Webcam access is required.

Good lighting improves recognition accuracy.

Do not upload captured_images/ or .db files to GitHub.

Add a .gitignore file:

database/
captured_images/
*.db
__pycache__/
Known Issues

Face recognition accuracy depends on lighting and camera quality.

Embedding threshold may require tuning.

Some modules use different face recognition libraries and may require alignment.

Future Improvements

Improve matching accuracy with better models

Encrypt database storage

Add transaction history

Build GUI instead of terminal interface

Deploy as a desktop application
