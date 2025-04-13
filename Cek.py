import tkinter as tk
from tkinter import messagebox

# Məhsullar və qiymətləri (ad: qiymət)
products = {
    "Alma": 1.2,
    "Armud": 1.5,
    "Banan": 1.1,
    "Kivi": 2.0,
    "Üzüm": 2.5,
    "Nar": 1.8,
    "Şaftalı": 2.2,
    "Çiyələk": 3.0,
    "Ananas": 4.0,
    "Mango": 3.5
}

# Checkbox-ları saxlamaq üçün
checkbox_vars = {}

# Məhsulları göstərən funksiya
def show_products():
    for widget in product_frame.winfo_children():
        widget.destroy()

    for i, (name, price) in enumerate(products.items()):
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(product_frame, text=f"{name} - {price} AZN", variable=var)
        checkbox.grid(row=i, column=0, sticky="w")
        checkbox_vars[name] = (var, price)

# Seçilmiş məhsulların ümumi qiymətini hesablayan funksiya
def calculate_total(event=None):
    total = 0
    selected_items = []
    for name, (var, price) in checkbox_vars.items():
        if var.get():
            total += price
            selected_items.append(name)

    messagebox.showinfo("Ümumi Qiymət", f"Seçdiyiniz məhsullar: {', '.join(selected_items)}\nÜmumi Qiymət: {total:.2f} AZN")

# Əsas pəncərə
root = tk.Tk()
root.title("Məhsul Qiymətləri")

# Məhsul siyahısı üçün frame
product_frame = tk.Frame(root)
product_frame.pack(pady=10)

# Price düyməsi
price_button = tk.Button(root, text="Price", command=show_products)
price_button.pack(pady=5)

# Enter düyməsini enter klaviatura düyməsi ilə əlaqələndir
root.bind('<Return>', calculate_total)

# Enter düyməsi (manual klik üçün də)
enter_button = tk.Button(root, text="Enter", command=calculate_total)
enter_button.pack(pady=5)

root.mainloop()
