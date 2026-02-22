import sqlite3
import cv2

def view_users():
    conn = sqlite3.connect("database/atm_users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT account_number, name, image_path FROM users")
    rows = cursor.fetchall()
    if rows:
        print("Registered Users:")
        for row in rows:
            account_number = row[0]
            name = row[1]
            image_path = row[2]
            print(f"Account Number: {account_number}, Name: {name}")

            if image_path and cv2.os.path.exists(image_path):
                image = cv2.imread(image_path)
                cv2.imshow(f"User: {name} (Account: {account_number})", image)
                print(f"Displaying image for {name}")
                cv2.waitKey(0)  
                cv2.destroyAllWindows()
            else:
                print(f"No image found for user {name}")
    else:
        print("No users found.")

    conn.close()


if __name__ == "__main__":
    view_users()
