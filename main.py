import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class SymposiumEventManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Symposium Event Management System")

        self.event_list = []

        # Create a notebook to organize pages
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Create pages with different colors
        self.create_welcome_page()
        self.page1 = ttk.Frame(self.notebook, style='Page.TFrame')
        self.page2 = ttk.Frame(self.notebook, style='Page.TFrame')
        self.page3 = ttk.Frame(self.notebook, style='Page.TFrame')

        self.notebook.add(self.welcome_page, text="Welcome", padding=10)
        self.notebook.add(self.page1, text="Add Event", padding=10)
        self.notebook.add(self.page2, text="Search Event", padding=10)
        self.notebook.add(self.page3, text="Event List", padding=10)

        # Create a style for pages
        self.page_style = ttk.Style()
        self.page_style.configure('Page.TFrame', background='lightgray')

        # Configure the style for notebook tabs
        self.notebook_style = ttk.Style()
        self.notebook_style.configure('TNotebook.Tab', padding=(10, 5), font=("Helvetica", 12))

        # Set the background color for each tab button
        self.notebook_style.map('TNotebook.Tab', background=[('selected', 'lightblue'), ('active', 'lightblue')])

        # Initialize widgets for each page
        self.init_add_event_page()
        self.init_search_event_page()
        self.init_event_list_page()

        # Apply consistent styles to labels
        self.label_style = ttk.Style()
        self.label_style.configure('Label.TLabel', font=("Helvetica", 12), padding=(5, 2))

        # Apply consistent styles to buttons
        self.button_style = ttk.Style()
        self.button_style.configure('Button.TButton', font=("Helvetica", 12), padding=5)

        # Apply consistent styles to entry fields
        self.entry_style = ttk.Style()
        self.entry_style.configure('Entry.TEntry', font=("Helvetica", 12), padding=(5, 2))

    def init_add_event_page(self):
        # Add event page
        self.name_label = ttk.Label(self.page1, text="Event Name:", style='Label.TLabel')
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.page1, style='Entry.TEntry')
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Event Type
        self.type_label = ttk.Label(self.page1, text="Event Type:", style='Label.TLabel')
        self.type_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.type_entry = ttk.Entry(self.page1, style='Entry.TEntry')
        self.type_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Event Date
        self.date_label = ttk.Label(self.page1, text="Event Date:", style='Label.TLabel')
        self.date_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.date_Combobox = ttk.Combobox(self.page1, values=self.get_date_options(), state="readonly")
        self.date_Combobox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Event Venue
        self.venue_label = ttk.Label(self.page1, text="Event Venue:", style='Label.TLabel')
        self.venue_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.venue_entry = ttk.Entry(self.page1, style='Entry.TEntry')
        self.venue_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Add Event Button
        self.add_button = ttk.Button(self.page1, text="Add Event", command=self.add_event, style='Button.TButton')
        self.add_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="we")


    def init_registration_page(self):
        self.registration_page = ttk.Frame(self.notebook, style='Page.TFrame')

        # Participant Details Labels and Entry Widgets
        ttk.Label(self.registration_page, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.registration_page)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.registration_page, text="Mobile Number:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.mobile_entry = ttk.Entry(self.registration_page)
        self.mobile_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.registration_page, text="College Name:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.college_entry = ttk.Entry(self.registration_page)
        self.college_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.registration_page, text="Event Name:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        event_names = ["Zeal Tech", "Trio Tech"]  # Replace with your event names
        self.event_Combobox = ttk.Combobox(self.registration_page, values=event_names, state="readonly")
        self.event_Combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.registration_page, text="Email ID:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = ttk.Entry(self.registration_page)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Register Button
        ttk.Button(self.registration_page, text="Register", command=self.register_participant).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Add the registration page to the notebook
        self.notebook.add(self.registration_page, text="Registration", padding=10)

    def register_participant(self):
        name = self.name_entry.get()
        mobile = self.mobile_entry.get()
        college = self.college_entry.get()
        event = self.event_Combobox.get()
        email = self.email_entry.get()

        if name and mobile and college and event and email:
            participant_info = f"Name: {name}\nMobile: {mobile}\nCollege: {college}\nEvent: {event}\nEmail: {email}"
            # You can save or display the participant_info as needed
            messagebox.showinfo("Registration Successful", "Participant details:\n" + participant_info)
            # You may also want to clear the entry fields after registration
            self.name_entry.delete(0, tk.END)
            self.mobile_entry.delete(0, tk.END)
            self.college_entry.delete(0, tk.END)
            self.event_Combobox.set("")  # Reset the event combobox
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please provide all participant details.")

    def create_welcome_page(self):
        # Welcome Page
        self.welcome_page = ttk.Frame(self.notebook, style='Page.TFrame')
        welcome_label = ttk.Label(self.welcome_page, text="Welcome to the Symposium Event Management System!", font=("Helvetica", 16))
        welcome_label.pack(padx=20, pady=20)
        instructions_label = ttk.Label(self.welcome_page, text="Use the tabs above to navigate the application.")
        instructions_label.pack(padx=20, pady=10)

    def init_search_event_page(self):
        # Search Event Page
        self.search_label = ttk.Label(self.page2, text="Search Event:")
        self.search_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.search_entry = ttk.Entry(self.page2)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Search Event Button
        self.search_button = ttk.Button(self.page2, text="Search Event", command=self.search_event)
        self.search_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="we")

    def init_event_list_page(self):
        # Event List Page
        self.event_listbox = tk.Listbox(self.page3, bg="lightyellow", height=10)
        self.event_listbox.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        # List Events Button
        self.list_button = ttk.Button(self.page3, text="List Events", command=self.list_events)
        self.list_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="we")

        # Clear List Button
        self.clear_button = ttk.Button(self.page3, text="Clear List", command=self.clear_list)
        self.clear_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="we")

        # Set grid row and column weights to make the listbox expand
        self.page3.grid_rowconfigure(0, weight=1)
        self.page3.grid_columnconfigure(0, weight=1)

    def get_date_options(self):
        days = [str(day).zfill(2) for day in range(1, 32)]
        months = [str(month).zfill(2) for month in range(1, 13)]
        years = [str(year) for year in range(2023, 2031)]
        return [f"{day}/{month}/{year}" for year in years for month in months for day in days]

    # Rest of the code remains the same...
    def add_event(self):
        event_name = self.name_entry.get()
        event_type = self.type_entry.get()
        event_date = self.date_Combobox.get()
        event_venue = self.venue_entry.get()

        if event_name and event_type and event_date and event_venue:
            event = f"Name: {event_name}\nType: {event_type}\nDate: {event_date}\nVenue: {event_venue}"
            self.event_list.append(event)
            self.name_entry.delete(0, tk.END)
            self.type_entry.set("")
            self.date_Combobox.set("")  # Change to set the date entry
            self.venue_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Event added successfully!")
        else:
            messagebox.showerror("Error", "Please provide event details.")

    def search_event(self):
        search_term = self.search_entry.get()
        if search_term:
            matching_events = [event for event in self.event_list if search_term.lower() in event.lower()]
            if matching_events:
                events = "\n".join(matching_events)
                messagebox.showinfo("Search Results", events)
            else:
                messagebox.showinfo("Search Results", "No matching events found.")
        else:
            messagebox.showerror("Error", "Please provide a search term.")

    def list_events(self):
        events = "\n".join(self.event_list)
        if events:
            messagebox.showinfo("Event List", events)
        else:
            messagebox.showinfo("Event List", "No events to display.")

    def clear_list(self):
        self.event_list = []
        self.event_listbox.delete(0, tk.END)
        messagebox.showinfo("Success", "Event list cleared successfully!")



def main():
    root = tk.Tk()
    root.geometry("800x600")
    app = SymposiumEventManagementApp(root)
    app.init_registration_page()  # Initialize the registration page
    root.mainloop()

if __name__ == "__main__":
    main()
