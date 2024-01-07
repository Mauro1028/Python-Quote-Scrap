import requests
import tkinter as tk

def fetch_traffic_data():
    url_api = 'https://api.midway.tomtom.com/ranking/liveHourly/USA_miami'
    usa_req = requests.get(url_api)
    usa_json = usa_req.json()
    return usa_json

def update_display():
    traffic_data = fetch_traffic_data()
    display_label.config(text=str(traffic_data))  # You might want to format this better

# Create the main window
root = tk.Tk()
root.title("Traffic Data Display")

# Create a label to display the traffic data
display_label = tk.Label(root, text="", wraplength=500)
display_label.pack(pady=20)

# Button to manually update the display
update_button = tk.Button(root, text="Update Display", command=update_display)
update_button.pack()

# Initial update on startup
update_display()

# Run the main loop
root.mainloop()
