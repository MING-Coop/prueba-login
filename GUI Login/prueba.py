import tkinter as tk
from tkinter import messagebox

# Función para verificar el inicio de sesión
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Validar las credenciales (en este ejemplo son predeterminadas)
    if username == "admin" and password == "12345":
        messagebox.showinfo("Login", "Login exitoso")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear la ventana principal
root = tk.Tk()
root.title("Login")
root.geometry("300x150")

# Crear widgets de la interfaz
label_username = tk.Label(root, text="Usuario")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Contraseña")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=10)

# Iniciar la aplicación
root.mainloop()