import tkinter as tk
from tkinter import messagebox
from sharepoint_connector import connect_to_sharepoint
from operations.manage_lists import get_all_lists, delete_list

class SharePointApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SharePoint Manager")
        
        self.domain = tk.StringVar()
        self.site_name = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.ctx = None
        
        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self.root, text="SharePoint Domain:").pack()
        tk.Entry(self.root, textvariable=self.domain).pack()

        tk.Label(self.root, text="Site Name:").pack()
        tk.Entry(self.root, textvariable=self.site_name).pack()

        tk.Label(self.root, text="Username:").pack()
        tk.Entry(self.root, textvariable=self.username).pack()

        tk.Label(self.root, text="Password:").pack()
        tk.Entry(self.root, textvariable=self.password, show="*").pack()

        tk.Button(self.root, text="Connect to SharePoint", command=self.connect_to_sharepoint).pack()
        tk.Button(self.root, text="List Lists", command=self.list_lists).pack()
        tk.Button(self.root, text="Delete List", command=self.delete_list_prompt).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def connect_to_sharepoint(self):
        """Conecta ao SharePoint com as credenciais fornecidas."""
        try:
            self.ctx = connect_to_sharepoint(self.domain.get(), self.site_name.get(), self.username.get(), self.password.get())
            messagebox.showinfo("Success", "Connected to SharePoint successfully!")
        except Exception as e:
            messagebox.showerror("Connection Failed", f"Failed to connect: {e}")

    def list_lists(self):
        """Lista todas as listas disponíveis no site."""
        if not self.ctx:
            messagebox.showerror("Error", "You need to connect first.")
            return
        try:
            lists = get_all_lists(self.ctx)
            messagebox.showinfo("Available Lists", "\n".join(lists) if lists else "No lists available.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve lists: {e}")

    def delete_list_prompt(self):
        """Prompt para escolher uma lista para deletar."""
        if not self.ctx:
            messagebox.showerror("Error", "You need to connect first.")
            return
        try:
            lists = get_all_lists(self.ctx)
            if not lists:
                messagebox.showinfo("Info", "No lists available to delete.")
                return
            
            delete_list_name = tk.simpledialog.askstring("Delete List", "Enter the name of the list to delete:")
            if delete_list_name in lists:
                delete_list(self.ctx, delete_list_name)
                messagebox.showinfo("Success", f"List '{delete_list_name}' deleted successfully!")
            else:
                messagebox.showinfo("Error", "List not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete list: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SharePointApp(root)
    root.mainloop()
