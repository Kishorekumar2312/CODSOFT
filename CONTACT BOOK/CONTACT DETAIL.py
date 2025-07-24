import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    contact = {
        "store": store_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }
    contacts.append(contact)
    messagebox.showinfo("Success", "Contact added!")
    clear_entries()
    refresh_list()

def clear_entries():
    store_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def refresh_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['store']} - {contact['phone']}")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        del contacts[selected[0]]
        messagebox.showinfo("Deleted", "Contact removed.")
        refresh_list()

# GUI layout
root = tk.Tk()
root.title("Contact Manager")

tk.Label(root, text="Store Name").grid(row=0, column=0)
tk.Label(root, text="Phone").grid(row=1, column=0)
tk.Label(root, text="Email").grid(row=2, column=0)
tk.Label(root, text="Address").grid(row=3, column=0)

store_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

store_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=1)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=5, columnspan=2)

refresh_list()

root.mainloop()