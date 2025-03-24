#Author: M.T.T.K.S.Perera
#Date: 23/09/2024
#Student ID:20232673

import csv
# Task A: Input Validation
def validate_date_input():
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
                continue
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


def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
    try:
        restarting_the_task = input("Do you want to run this task again? (Yes = 'Y' , No = 'N'):")
        if restarting_the_task.lower() == "y":
            return
                    
        if restarting_the_task.lower() == "n":
            print("Exiting...")
            exit()
    except ValueError:
        print("Please Enter an valid Input")
    


# Task B: Processed Outcomes
def process_csv_data(file_path):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    
    #Globalize the variables
    global total_electric_vehicles,total_trucks,total_vehicles,total_two_wheels,total_busses_elmAvenue,total_vehicles_without_turning,percentage_of_trucks,avg_bicycles_per_hour,total_over_speed_vehicles,total_scooters_elmAvenue,hours_with_traffic,busiest_hour,busiest_count,total_rain_hours,total_vehicles_ElmAvenue_RabbitRoad,total_vehicles_Hanley_highway_Westway,percentage_of_scooters_ElmAvenue_RabbitRoad,results
    
    #Initialise the variables and lists
    results = []
    data = 0
    total_vehicles = 0
    total_trucks = 0
    total_electric_vehicles = 0
    total_two_wheels = 0
    total_busses_elmAvenue = 0
    total_vehicles_without_turning = 0
    total_bicycles = 0
    total_over_speed_vehicles = 0
    total_vehicles_ElmAvenue_RabbitRoad = 0
    total_vehicles_Hanley_highway_Westway = 0
    total_scooters_elmAvenue = 0
    busiest_hour = None
    busiest_count = 0
    rain_hours = []
    wheather = 0
    time = 0
    rain_hour = 0
    splitted_time_for_rain = 0
    total_rain_hours = 0
    hours_with_traffic = {}  # Initialize hours_with_traffic as an empty dictionary
    
    # Logic for processing data goes here
    

    # Reading the CSV file
    try:
        with open(f'{file_path}.csv','r') as file:
            data = csv.reader(file)
            for row in data:
                total_vehicles = total_vehicles + 1 # when printing we should have to -1 beacause table headers
                if row[8] == "Truck":
                    total_trucks = total_trucks + 1
                if row[9] == "True":
                    total_electric_vehicles = total_electric_vehicles + 1   
                if (row[8] == "Bicycle") or (row[8] == "Scooter") or (row[8] == "Motorcycle"):
                    total_two_wheels = total_two_wheels + 1
                if (row[8] == "Buss") and (row[0] == "Elm Avenue/Rabbit Road"):
                    total_busses_elmAvenue = total_busses_elmAvenue + 1
                if row[3] == row[4]:
                    total_vehicles_without_turning = total_vehicles_without_turning + 1
                if row[8] == "Bicycle":
                    total_bicycles = total_bicycles + 1
                    avg_bicycles_per_hour = round(total_bicycles/24)
                if row[6] < row[7]:
                    total_over_speed_vehicles = total_over_speed_vehicles + 1
                if row[0] == "Hanley Highway/Westway":
                    total_vehicles_Hanley_highway_Westway = total_vehicles_Hanley_highway_Westway + 1
                if row[0] == "Elm Avenue/Rabbit Road":
                    total_vehicles_ElmAvenue_RabbitRoad = total_vehicles_ElmAvenue_RabbitRoad + 1
                if (row[8] == "Scooter") and (row[0] == "Elm Avenue/Rabbit Road"):
                    total_scooters_elmAvenue = total_scooters_elmAvenue + 1
                    
                if row[0] == "Hanley Highway/Westway":  #Check if the junction matches
                    time_of_day = row[2]  #column 2 contains the time
                    splitted_time = time_of_day.split(":") #splitting the hour part
                    hour = splitted_time[0] #hours are in 0th index
                    if hour not in hours_with_traffic:
                        hours_with_traffic[hour] = 0  # Initialize the hour in the dictionary
                    hours_with_traffic[hour] += 1  # Increment the count for this hour
                
                for hour in hours_with_traffic:  # Basic iteration over keys
                    count = hours_with_traffic[hour]  # Get the count for this hour
                    if count > busiest_count:  # Compare to find the maximum
                        busiest_hour = hour
                        busiest_count = count
                
                #assinging the data for the calcultions of rain hours
                wheather = row[5]
                time = row[2]
                
                if "Rain" in wheather:
                    splitted_time_for_rain = time.split(":")
                    rain_hour = splitted_time_for_rain[0]
                    if rain_hour not in rain_hours:
                        rain_hours.append(rain_hour)
        percentage_of_trucks = round((total_trucks / (total_vehicles - 1)) * 100)
        percentage_of_scooters_ElmAvenue_RabbitRoad = round(total_scooters_elmAvenue / (total_vehicles_ElmAvenue_RabbitRoad) * 100)        
        total_rain_hours = len(rain_hours)
               
                
    
    
        results = [f"The data file selected is traffic_data{formated_day}{formated_month}{year}.csv",
                f"The total number of vehicles recorded for the date is {total_vehicles-1}",
                f"The total number of trucks recorded for the date is {total_trucks}",
                f"The total number of electric vehicles for this date is {total_electric_vehicles}",
                f"The total number of two-wheeled vehicles for this date is {total_two_wheels}",
                f"The total number of busses leaving Elm Avenue/Rabbit Road heading north is {total_busses_elmAvenue}",
                f"The total number of vehicles through both junctions not turning left or right is {total_vehicles_without_turning}",
                f"The percentage of total vehicles recorded that are trucks for this date is {percentage_of_trucks}%",
                f"The average number of bikes per hour for this date is {avg_bicycles_per_hour}",
                f"The total number of vehicles recorded as over the speed limit for this date is {total_over_speed_vehicles}",
                f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {total_vehicles_ElmAvenue_RabbitRoad}",
                f"The total number of vehicles recorded through Hanley Highway/Westway junction is {total_vehicles_Hanley_highway_Westway}",
                f"{percentage_of_scooters_ElmAvenue_RabbitRoad}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters",
                f"The highest number of vehicles in an hour on Hanley Highway/Westway is {busiest_count}",
                f"The most vehicles through Hanley Highway/Westway were recorded between {busiest_hour}:00 and {int(busiest_hour)+1}:00",
                f"The number of hours of rain for this date is {total_rain_hours}"]            
    except FileNotFoundError:
        print(f"There is not such file as {file_path}.csv") 

def display_outcomes():
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    # Printing outcomes to the console
    try:
        print("*"*30)
        for item in results:
            print(item)
        print("*"*30)
    except:
        print("An error occured.")



# Task C: Save Results to Text File
def save_results_to_file(file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    # File writing logic goes here
    results_file = open(file_name,"a")
    
    #writing the file
    for item in results:
        results_file.write(f"{item}\n")
    
    breaklines = ("\n","\n","\n")
    results_file.writelines(breaklines)
    results_file.write("****************************************************************\n")
#Functions to start the program



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
        file_path = (f"traffic_data{formated_day}{formated_month}{year}")
        
        try:
            with open(f'{file_path}.csv','r') as file:
                data = csv.reader(file)
                hours_elm = [0]*24
                hours_han = [0]*24
                for row in data:
                    if row[0] == "Elm Avenue/Rabbit Road":
                        for hour in range(24):
                            if int(row[2][0:2]) == hour:
                                hours_elm[hour] += 1
                    if row[0] == "Hanley Highway/Westway":
                        for hour in range(24):
                            if int(row[2][0:2]) == hour:
                                hours_han[hour] +=1
                current_data = {    
                    "Elm Avenue/Rabbit Road": hours_elm,
                    "Hanley Highway/Westway": hours_han
                }
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
        self.current_data = None
        print("Previous data cleared.")

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            try:
                restarting_the_task = input("Do you want to run this task again? (Yes = 'Y' , No = 'N'):")
                if restarting_the_task.lower() == "y":
                    self.clear_previous_data()
                    validate_date_input()
                    process_csv_data(f"traffic_data{formated_day}{formated_month}{year}")
                    display_outcomes()
                    save_results_to_file()
                    self.load_csv_file()
                elif restarting_the_task.lower() == "n":
                    print("Exiting...")
                    exit()
                else:
                    print("Please enter a valid input (Y/N).")
            except ValueError:
                print("Please enter a valid input (Y/N).")

if __name__ == "__main__":
    validate_date_input()
    process_csv_data(f"traffic_data{formated_day}{formated_month}{year}")
    display_outcomes()
    save_results_to_file()
    processor = MultiCSVProcessor()
    processor.load_csv_file()
    processor.process_files()