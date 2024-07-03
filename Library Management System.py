import tkinter as tk
from tkinter import messagebox

# Base Class
class LibraryItem:
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    def display_info(self):
        pass

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

# Derived Class for Books
class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self._genre = genre

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    def display_info(self):
        return f"Book Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nGenre: {self.genre}"

# Derived Class for Magazines
class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self._issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value):
        self._issue_number = value

    def display_info(self):
        return f"Magazine Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nIssue Number: {self.issue_number}"

# GUI Class
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.configure(bg='#5dd9a7')  # Set the background color

        self.items = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="\t  Title: \t\t", bg='#d9ce5d')
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.author_label = tk.Label(self.root, text="\tAuthor: \t".upper(), bg='#d9ce5d')
        self.author_label.grid(row=1, column=0, padx=10, pady=10)
        self.author_entry = tk.Entry(self.root)
        self.author_entry.grid(row=1, column=1, padx=10, pady=10)

        self.year_label = tk.Label(self.root, text="\t Year: \t\t".upper(), bg='#d9ce5d')
        self.year_label.grid(row=2, column=0, padx=10, pady=10)
        self.year_entry = tk.Entry(self.root)
        self.year_entry.grid(row=2, column=1, padx=10, pady=10)

        self.type_label = tk.Label(self.root, text="\tType:\t\t", bg='#d9ce5d')
        self.type_label.grid(row=3, column=0, padx=10, pady=10)
        self.type_var = tk.StringVar(value="Book")
        self.book_radio = tk.Radiobutton(self.root, text="Book", variable=self.type_var, value="Book", bg='#5dd9a7')
        self.book_radio.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.magazine_radio = tk.Radiobutton(self.root, text="Magazine", variable=self.type_var, value="Magazine", bg='#5dd9a7')
        self.magazine_radio.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        self.extra_label = tk.Label(self.root, text="Genre/Issue Number:", bg='#d9ce5d')
        self.extra_label.grid(row=4, column=0, padx=10, pady=10)
        self.extra_entry = tk.Entry(self.root)
        self.extra_entry.grid(row=4, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item, bg='#4caf50', fg='white')
        self.add_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Item", command=self.delete_item, bg='#f44336', fg='white')
        self.delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.display_button = tk.Button(self.root, text="Display Items", command=self.display_items, bg='#2196f3', fg='white')
        self.display_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.items_list = tk.Text(self.root, height=10, width=50)
        self.items_list.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def add_item(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        extra = self.extra_entry.get()
        item_type = self.type_var.get()

        if not title or not author or not year or not extra:
            messagebox.showerror("Error", "All fields must be filled out")
            return

        try:
            year = int(year)
        except ValueError:
            messagebox.showerror("Error", "Year must be an integer")
            return

        if item_type == "Book":
            item = Book(title, author, year, extra)
        else:
            item = Magazine(title, author, year, extra)

        self.items.append(item)
        messagebox.showinfo("Success", f"{item_type} added successfully")
        self.clear_entries()

    def delete_item(self):
        selected_item = self.items_list.tag_ranges(tk.SEL)
        if selected_item:
            item_info = self.items_list.get(selected_item[0], selected_item[1])
            for item in self.items:
                if item.display_info() == item_info:
                    self.items.remove(item)
                    self.items_list.delete(selected_item[0], selected_item[1])
                    messagebox.showinfo("Success", "Item deleted successfully")
                    return
        else:
            messagebox.showerror("Error", "No item selected")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.extra_entry.delete(0, tk.END)

    def display_items(self):
        self.items_list.delete(1.0, tk.END)
        for item in self.items:
            self.items_list.insert(tk.END, item.display_info() + "\n" + "-" * 20 + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
