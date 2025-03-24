import csv
# Task D: Histogram Display

from tkinter import *

class HistogramApp:
    def __init__(self, traffic_data, date,root):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date
        self.root = root
        self.canvas = Canvas(self.root, width=1920,height=1080, bg="white") # Will hold the canvas for drawing
        self.canvas.pack()

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.root.title(f"Traffic Data Histogram - {self.date}")
        self.root.geometry("1600x900")
        self.canvas.pack(pady=20)

    def draw_histogram(self):
        """
        Draws the histogram with fixed spacing and improved layout.
        """
        bar_width = 20  # Width of each bar
        hour_group_gap = 15  # Space between groups of bars for each hour
        junction_gap = 5  # Space between bars of different junctions
        max_volume = max(max(self.traffic_data[junction]) for junction in self.traffic_data)
        scale_factor = 400 / max_volume  # Scale factor for fitting bars within Y-axis height

        # Base position for the histogram
        x_start = 100
        y_base = 550

        for hour in range(24):
            # Starting X position for the current hour's group of bars
            hour_x_start = x_start + hour * (bar_width * len(self.traffic_data) + junction_gap * (len(self.traffic_data) - 1) + hour_group_gap)

            for i, (junction, volumes) in enumerate(self.traffic_data.items()):
                volume = volumes[hour]
                bar_height = volume * scale_factor
                color = "#824ce0" if junction == "Elm Avenue/Rabbit Road" else "#0095b6"

                # Calculate bar positions
                bar_x_start = hour_x_start + i * (bar_width + junction_gap)
                bar_x_end = bar_x_start + bar_width

                # Draw the bar
                self.canvas.create_rectangle(
                    bar_x_start, y_base - bar_height, bar_x_end, y_base, fill=color, outline="black"
                )

                # Display the volume above the bar
                self.canvas.create_text(
                    (bar_x_start + bar_x_end) // 2, y_base - bar_height - 10, text=str(volume), font=("Arial", 8)
                )

            # Label the hour below the group of bars
            self.canvas.create_text(
                hour_x_start + (bar_width * len(self.traffic_data) + junction_gap * (len(self.traffic_data) - 1)) // 2,
                y_base + 20,
                text=str(hour),
                font=("Arial", 10, "bold"),
            )

        # Draw the X-axis and Y-axis
        self.canvas.create_line(80, y_base, 1560, y_base, width=2)  # X-axis
        self.canvas.create_line(80, y_base, 80, 50, width=2)  # Y-axis

        # Add Y-axis labels
        y_step = max_volume // 10 if max_volume > 10 else 1
        for i in range(0, max_volume + 1, y_step):
            y_pos = y_base - (i * scale_factor)
            self.canvas.create_text(60, y_pos, text=str(i), font=("Arial", 8))
            self.canvas.create_line(75, y_pos, 80, y_pos, width=1)

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """

        # Adding a legend to the histogram
        self.canvas.create_text(1420, 100, text="Legend:", anchor="ne", font=("Arial", 10, "bold"))

        self.canvas.create_rectangle(1420, 140, 1440, 160, fill="#824ce0", outline="black")
        self.canvas.create_text(1410, 150, text="Elm Avenue/Rabbit Road", anchor="e", font=("Arial", 8))

        self.canvas.create_rectangle(1420, 170, 1440, 190, fill="#0095b6", outline="black")
        self.canvas.create_text(1410, 180, text="Hanley Highway/Westway", anchor="e", font=("Arial", 8))
    

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        # Tkinter main loop logic
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        


# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None

    def load_csv_file(self):
        """
        Loads a CSV file and processes its data.
        """
        """
        Prompts the user for a date in DD MM YYYY format, validates the input for:
        - Correct data type
        - Correct range for day, month, and year
        """
        #Initialise the variables
        global day 
        day = 0
        global month
        month = 0
        global year
        year = 0 
        global formated_day
        global formated_month

        #Day
        while True:
            try:
                day = int(input("Please enter the day of the survey in the format dd: "))
                formated_day = f"{day:02}"
                if 0 < day <= 31:
                    break
                else:
                    print("Out of range - values must range from 1 and 31.")
            except ValueError:
                print("Integer required.")
        #Month
        while True:
            try:
                month = int(input("Please enter the month of the survey in the format MM: "))
                formated_month = f"{month:02}"
                if 0 < month <= 12:
                    break
                else:
                    print("Out of range - values must range from 1 and 12.")
                    continue
            except ValueError:
                        print("Integer required.")
        #Year
        while True:
            try:
                year = int(input("Please enter the year of the survey in the format YYYY: "))
                if 2000 <= year <= 2024:
                    break
                else:
                    print("Out of range - values must range from 2000 and 2024.")
                    continue
            except ValueError:
                print("Integer required.")
        file_path = (f"traffic_data{formated_day}{formated_month}{year}")
        
    # Logic for processing data goes here

    # Reading the CSV file
        try:
            
            with open(f'{file_path}.csv','r') as file:
                data = csv.reader(file)
                #initialising the lists for hours
                hours_elm = [0]*24 #List to store the number of vehicles per hour (elm avenue)
                hours_han = [0]*24 #List to store the number of vehicles per hour (hanley highway)
                for row in data:
                    if row[0] == "Elm Avenue/Rabbit Road":
                        for hour in range(24):
                            if int(row[2][0:2]) == hour:
                                hours_elm[hour] += 1
                    if row[0] == "Hanley Highway/Westway":
                        for hour in range(24):
                            if int(row[2][0:2]) == hour:
                                hours_han[hour] +=1
                #Dictionary to store the data
                current_data = {    
                    "Elm Avenue/Rabbit Road": hours_elm,
                    "Hanley Highway/Westway": hours_han
                }
                # Display the histogram after loading the data
                root = Tk()
                date = f"{formated_day}/{formated_month}/{year}"
                app = HistogramApp(current_data, date, root)
                app.run()
                root.mainloop()
        except FileNotFoundError:
            print(f"There is not such file as {file_path}.csv")


    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        # Logic for clearing data
        self.curent_data = None
        print("Previous data cleared.")
        
        

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        # Logic for user interaction
        
    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        # Loop logic for handling multiple files
        """
        Prompts the user to decide whether to load another dataset:
        - Validates "Y" or "N" input
        """
        while True:
            try:
                restarting_the_task = input("Do you want to run this task again? (Yes = 'Y' , No = 'N'):")
                if restarting_the_task.lower() == "y":
                    self.clear_previous_data()
                    print(self.current_data)
                    
                    self.load_csv_file()
                if restarting_the_task.lower() == "n":
                    print("Exiting...")
                    break
            except ValueError:
                print("Please Enter an valid Input")
                continue

if __name__ == "__main__":
    while True:
        try:
            processor = MultiCSVProcessor()
            processor.load_csv_file()
            processor.process_files() 
            break  
        except:  
            print("An error occured, please try again")
            continue