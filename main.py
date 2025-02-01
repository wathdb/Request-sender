import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import requests

global_data = {}
global_headers = {}

def on_button_click():
    global global_headers, global_data
    url = entry.get().strip()
    headers = global_headers
    data = global_data
    if var1.get() == 1:
        response = requests.post(url, json=data, headers=headers)
    elif var2.get() == 1:
        response = requests.get(url, params=data, headers=headers)
    else:
        return
    print(response.status_code)
    print(response.text)

def open_config_window():
    config_window = tk.Toplevel(root)
    config_window.title("Configuration")
    config_window.geometry("600x500")
    temp_data = {}
    temp_headers = {}
    
    def add_pair(key_entry, value_entry, listbox, temp_dict):
        key = key_entry.get().strip()
        value = value_entry.get().strip()
        if key:
            temp_dict[key] = value
            listbox.delete(0, tk.END)
            for k, v in temp_dict.items():
                listbox.insert(tk.END, f'"{k}": "{v}"')
            key_entry.delete(0, tk.END)
            value_entry.delete(0, tk.END)
    
    notebook = ttk.Notebook(config_window)
    notebook.pack(expand=True, fill='both', padx=10, pady=10)
    
    frame_data = ttk.Frame(notebook)
    notebook.add(frame_data, text="Data")
    lbl_key_data = ttk.Label(frame_data, text="Key:")
    lbl_key_data.grid(column=0, row=0, padx=5, pady=5, sticky='e')
    entry_key_data = ttk.Entry(frame_data, width=20)
    entry_key_data.grid(column=1, row=0, padx=5, pady=5)
    lbl_val_data = ttk.Label(frame_data, text="Value:")
    lbl_val_data.grid(column=2, row=0, padx=5, pady=5, sticky='e')
    entry_val_data = ttk.Entry(frame_data, width=30)
    entry_val_data.grid(column=3, row=0, padx=5, pady=5)
    btn_add_data = ttk.Button(
        frame_data, 
        text="Add",
        command=lambda: add_pair(entry_key_data, entry_val_data, listbox_data, temp_data)
    )
    btn_add_data.grid(column=4, row=0, padx=5, pady=5)
    listbox_data = tk.Listbox(frame_data, width=70, height=10)
    listbox_data.grid(column=0, row=1, columnspan=5, padx=5, pady=5)
    
    frame_headers = ttk.Frame(notebook)
    notebook.add(frame_headers, text="Headers")
    lbl_key_headers = ttk.Label(frame_headers, text="Key:")
    lbl_key_headers.grid(column=0, row=0, padx=5, pady=5, sticky='e')
    entry_key_headers = ttk.Entry(frame_headers, width=20)
    entry_key_headers.grid(column=1, row=0, padx=5, pady=5)
    lbl_val_headers = ttk.Label(frame_headers, text="Value:")
    lbl_val_headers.grid(column=2, row=0, padx=5, pady=5, sticky='e')
    entry_val_headers = ttk.Entry(frame_headers, width=30)
    entry_val_headers.grid(column=3, row=0, padx=5, pady=5)
    btn_add_headers = ttk.Button(
        frame_headers, 
        text="Add",
        command=lambda: add_pair(entry_key_headers, entry_val_headers, listbox_headers, temp_headers)
    )
    btn_add_headers.grid(column=4, row=0, padx=5, pady=5)
    listbox_headers = tk.Listbox(frame_headers, width=70, height=10)
    listbox_headers.grid(column=0, row=1, columnspan=5, padx=5, pady=5)
    
    def save_config():
        global global_data, global_headers
        global_data = temp_data.copy()
        global_headers = temp_headers.copy()
        config_window.destroy()
    
    btn_save = ttk.Button(config_window, text="Save", command=save_config)
    btn_save.pack(pady=10)

root = tk.Tk()
root.title("RSender - V1.0.0")
root.geometry("400x300")
label = ttk.Label(root, text="REQUEST ANY URL")
label.pack(pady=10)
custom_font = tkFont.Font(family="Helvetica", size=16)
label.config(font=custom_font)
entry = ttk.Entry(root, width=30)
entry.pack(pady=10)
var1 = tk.IntVar()
var2 = tk.IntVar()
checkbox1 = ttk.Checkbutton(root, text="POST", variable=var1)
checkbox1.pack(pady=0)
checkbox2 = ttk.Checkbutton(root, text="GET", variable=var2)
checkbox2.pack(pady=0)
button_send = ttk.Button(root, text="Send", command=on_button_click)
button_send.pack(pady=10)
button_config = ttk.Button(root, text="Configure Data/Headers", command=open_config_window)
button_config.pack(pady=10)
root.mainloop()
