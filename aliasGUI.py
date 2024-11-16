import tkinter as tk
from tkinter import messagebox, ttk
import os
from ttkthemes import ThemedTk
import webbrowser

# Temalı pencere oluşturma
root = ThemedTk(theme="aqua")
root.title("Pardus Alias Yönetici")
root.geometry("600x500")
root.resizable(False, False)  # Formun boyutlarını sabitleme

# Başlık etiketi
title_label = tk.Label(root, text="Pardus Alias Yönetici", font=("Courier", 20, "bold"), bg="#f7f7f7", relief="ridge")
title_label.pack(pady=10)

# Alias giriş alanı
entry_frame = tk.Frame(root)
entry_frame.pack(pady=20)

alias_label = tk.Label(entry_frame, text="Alias Adi:", font=("Courier", 12))
alias_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
alias_entry = ttk.Entry(entry_frame, width=30)
alias_entry.grid(row=0, column=1, padx=5, pady=5)

command_label = tk.Label(entry_frame, text="Komut:", font=("Courier", 12))
command_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
command_entry = ttk.Entry(entry_frame, width=30)
command_entry.grid(row=1, column=1, padx=5, pady=5)

# Alias ekleme fonksiyonu
def add_alias():
    alias_name = alias_entry.get().strip()
    command = command_entry.get().strip()
    if alias_name and command:
        with open(os.path.expanduser("~/.bash_aliases"), "a") as f:
            f.write(f"\nalias {alias_name}='{command}'\n")
        os.system("source ~/.bashrc")
        messagebox.showinfo("Başarılı", f"'{alias_name}' alias'ı başarıyla eklendi.")
        list_aliases()
    else:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun.")

# Alias listeleme fonksiyonu
def list_aliases():
    alias_listbox.delete(0, tk.END)
    if os.path.exists(os.path.expanduser("~/.bash_aliases")):
        with open(os.path.expanduser("~/.bash_aliases"), "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("alias"):
                alias_listbox.insert(tk.END, line.strip())

# Alias silme fonksiyonu
def delete_alias():
    selected_alias = alias_listbox.get(tk.ACTIVE)
    if selected_alias:
        alias_name = selected_alias.split()[1].split('=')[0]
        with open(os.path.expanduser("~/.bash_aliases"), "r") as f:
            lines = f.readlines()
        with open(os.path.expanduser("~/.bash_aliases"), "w") as f:
            for line in lines:
                if not line.startswith(f"alias {alias_name}="):
                    f.write(line)
        os.system("source ~/.bashrc")
        messagebox.showinfo("Başarılı", f"'{alias_name}' alias'ı başarıyla silindi.")
        list_aliases()

# Alias ekleme butonu
add_button = ttk.Button(root, text="Alias Ekle", command=add_alias)
add_button.pack(pady=10)

# Alias listesi ve Scrollbar ekleme
alias_list_frame = tk.Frame(root)
alias_list_frame.pack(pady=10)

alias_listbox = tk.Listbox(alias_list_frame, width=60, height=10)
alias_listbox.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(alias_list_frame, orient="vertical", command=alias_listbox.yview)
scrollbar.pack(side="right", fill="y")

alias_listbox.config(yscrollcommand=scrollbar.set)

# Alias silme butonu
delete_button = ttk.Button(root, text="Alias Sil", command=delete_alias)
delete_button.pack(pady=5)

# Tıklanabilir footer ekleme fonksiyonu
def open_website(event):
    webbrowser.open("https://algyazilim.com")

# Footer etiketi
footer_label = tk.Label(root, text="ALG Yazilim Inc.", font=("Courier", 10, "underline"), fg="blue", cursor="hand2")
footer_label.pack(side="bottom", pady=5)
footer_label.bind("<Button-1>", open_website)

# Uygulama başlatıldığında mevcut alias'ları listele
list_aliases()

# Uygulamayı başlat
root.mainloop()
