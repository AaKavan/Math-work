# imports
import tkinter as tk
from tkinter import messagebox
import sympy as sp


# Function to take matrix from user input
def parse_matrix(entry):
    try:
        text = entry.get("1.0", tk.END).strip()
        rows = text.split("\n")
        matrix = [row.split() for row in rows if row.strip()]
        sympy_matrix = sp.Matrix([[sp.sympify(val) for val in row] for row in matrix])
        return sympy_matrix
    except Exception:
        messagebox.showerror("Error", "Invalid matrix input. Please enter numbers or symbols separated by spaces.")
        return None


# Function to calculate commutator [A,B]= AB - BA
def calculate_commutator():
    A = parse_matrix(entry_A)
    B = parse_matrix(entry_B)
    if A is None or B is None:
        return
    if A.shape != B.shape:
        messagebox.showerror("Error", "Matrices must have the same shape.")
        return
    try:
        comm = A * B - B * A
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, str(comm))
    except Exception as e:
        messagebox.showerror("Error", f"Calculation failed: {e}")


# Function to calculate the conjugate: A_new = P^-1AP
def calculate_conjugate():
    A = parse_matrix(entry_A)
    P = parse_matrix(entry_P)
    if A is None or P is None:
        return
    if A.shape[0] != A.shape[1] or P.shape[0] != P.shape[1] or A.shape != P.shape:
        messagebox.showerror("Error", "A and P must be square matrices of the same size.")
        return
    try:
        P_inv = P.inv()
        conj = P_inv * A * P
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, str(conj))
    except Exception as e:
        messagebox.showerror("Error", f"Calculation failed: {e}")

# GUI setup
root = tk.Tk()
root.title("Matrix Calculator (Numeric + Symbolic)")

label_A = tk.Label(root, text="Matrix A (rows separated by newlines, numbers/symbols by spaces):")
label_A.pack()
entry_A = tk.Text(root, height=5, width=40)
entry_A.pack()

label_B = tk.Label(root, text="Matrix B (rows separated by newlines, numbers/symbols by spaces):")
label_B.pack()
entry_B = tk.Text(root, height=5, width=40)
entry_B.pack()

label_P = tk.Label(root, text="Matrix P (for conjugation P^-1 A P):")
label_P.pack()
entry_P = tk.Text(root, height=5, width=40)
entry_P.pack()

calculate_btn = tk.Button(root, text="Calculate [A, B] = AB - BA", command=calculate_commutator)
calculate_btn.pack(pady=5)

conjugate_btn = tk.Button(root, text="Calculate Conjugate P^-1 A P", command=calculate_conjugate)
conjugate_btn.pack(pady=5)

result_label = tk.Label(root, text="Result:")
result_label.pack()
result_text = tk.Text(root, height=5, width=40)
result_text.pack()

root.mainloop()
