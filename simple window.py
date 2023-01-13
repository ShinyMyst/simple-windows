import tkinter as tk

class MessageWindow():
    def __init__(self, title, size=None):
        # Create root window and hide it until called.
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size) # Size in format "intxint"
        self.root.withdraw()

        # Store Entry Data
        self.entry_data = []


    def create_label(self, text, size=None):
        """Creates a line of text in the window."""
        label = tk.Label(self.root, text=text, font=(size))
        label.pack()


    def create_entry(self):
        """Creates an entry box for the window"""
        entry = tk.Entry(self.root)
        self.entry_data.append(entry)
        entry.pack()


    def create_button(self, text, size=None,  command=None):
        """Create a button that executes given command"""
        button = tk.Button(self.root, text=text, font=(size), command=command)
        button.pack()
        
    def get_entry_data(self):
        """Collect and return the data from all entry fields."""
        data = []
        for entry in self.entry_data:
            data.append(entry.get())
        return data
        # print(data)


    def hide_window(self):
        """Hides window from screen, stopping the event loop."""
        self.root.quit()
        self.root.withdraw()

    def display_window(self):
        """Shows window on screen, restarting the event loop."""
        self.root.update()
        self.root.deiconify()
        self.root.mainloop()


def main():
    window = MessageWindow("Test Window", "300x150")
    window.create_label("Entry 1:", 20)
    window.create_entry()
    window.create_label("Entry 2:", 20)
    window.create_entry()
    window.create_button("Submit", command=window.get_entry_data)
    input()
    window.display_window()

if __name__ == "__main__":
    main()



