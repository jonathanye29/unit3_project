# Unit 3: Airport Flight Tracker System
![pexels-lt-chan-2833379](https://user-images.githubusercontent.com/111751273/217878429-b0860c83-7789-4ebb-883c-296cb0cf58e1.jpg)
<i>Pexels image</i> [1]

# Criteria A: Planning

## Problem definition
The air traffic control manager Zaven Galoyan is facing a major challenge in effectively managing and tracking all the relevant data pertaining to airport operations, such as flight numbers, destination/arriving from, flight schedule, terminal and gate numbers. The current manual system for keeping track of this data is time-consuming, prone to mistakes, and ineffective. The data is easily mixed up and lost, and the urgent need is to create a simple centralized manual system that can assist the air traffic control crew in managing all of this information quickly and effectively without relying on automated inputs.

## Success Criteria
1. The application will have a login and register system.
2. The application will allow the user to input all attributes (flight number, destination, flight schedule, terminal, and gate number) and will be stored into the database through the interface.
3. The application will allow user to search for flights by date and flight number.
4. The application will allow the user to view all values stored in the database.
5. The application will have a page that accesses a map of the airport and the location of all flights at their gate.
6. The application will have a statistics page that includes lists of all flights categorized by cancelled, delayed, and on-time. 

## Design Statement 
I plan to develop a system for the air traffic crew using Python, Kivymd, and SQlite. This will provide a comprehensive solution to the challenges faced by the air traffic control in maintaining accurate and up-to-date records of flight information. This solution will provide the air traffic control with a reliable and user-friendly tool to manage and track all flight-related information easily, ensuring that airport operations run smoothly and effectively.

## Rationale for Proposed Solution
Considering the challenges my client is facing, in order to effectively track all relevant data related to airport operations, I will develop an easy-to-use centralized manual system that will be designed and developed using Kivymd, Python, and SQLite. This solution is designed to address the challenges faced by the air traffic control in maintaining accurate and up-to-date records of flight information.

The application will have a GUI (Graphical User Interface) output rather than text output. This is to meet the client's need for an application that is  capable of recording and showing flight information. Further, through a graphical user interface, the client will be able to both input and see the saved records in an organized and visually appealing manner. Therefore, I have chosen for the output to be a GUI.

I decided to use the Python language to develop the functions of the appliction because it is the most popular and widely used programming language and it is also among the fastest-growing programming languages in the tech industry [4]. As a result of its widespread use, the program is easier for many developers to understand than languages like C or Javascript. This will benefit application in being programmed in Python because it makes it simple for upcoming programmers to comprehend the code and advance its development. There are also a wide range of libraries that are available in Python which can be easily accessed using a basic syntax [5]. The Python programming language is adequate for developing my client's desired application.

For the application interface itself, I decided to use KivyMD as it is both easy to learn and work with. One of KivyMD's main advantages is that it is a multi-platform application development framework that runs on different platforms like Android, iOS, Windows, Linux, and is written in the Python programming language [6]. KivyMD already has a set of pre-built user-interfacce elements and styles that can be easily customized and integrated into Kivy-based applications [7]. This allows me to save the time and effort needed in creating user-interface elements from scratch, allowing me to focus on other aspects of the development so I can complete the application on time for my client. Even though there are many advantages of using KivyMD, there are also some disadvantages. For example, there are other alternatives such as Flutter or PyQt, which both have larger communities for support and are better at developing native applications, compared to KivyMD [8]. However, due to how easy it is to learn, customizability, and compatibility, I chose to use KivyMD library to construct the application's interface.

Finally, I chose SQLite as the database management system for this solution. SQLite is a free database that does not require any additional server process, and is implemented on a single file. This database fits my client's needs as it is designed to handle large amounts of data efficiently [9]. It will be able to store all kinds of information safely and quickly, as it does not require to go through long procedural routines other databases such as IBM db2 use [10]. It also updates the content continuously, so little or no work is lost in a case of power failure or crash, which is crucial for my client as the information being stored needs to be retrieved when they need it [11]. Furthermore, its cross-platform compatibilty will allow benefit the client by allowing future developers to expand the program to onto other platforms. SQLite is the best option for my client as it is reliable, efficient, and cost-friendly, and easy to use compared to other databases available.


# Criteria B: Design

## System Diagram
![jojojojojojo](https://user-images.githubusercontent.com/111751273/218300364-847958a7-0dfe-4322-96aa-054a088358a8.png)
<i>Fig. 1</i> This is the system diagram for the proposed solution.

It serves as a visual representation of the system and its components, and their relationships to each other. As shown above, the application will run on Python and KivyMD. The application will have various inputs from the user, which will all be stored within a database using SQLite. All of this will be executed within the Pycharm application, which will then display the output on a screen.

## Wireframe Diagram 
![project3wireframe](https://user-images.githubusercontent.com/111751273/222183981-e5c23a00-11df-4f00-8393-bb5c2cb1d2c7.jpg)
<i>Fig. 2</i> This is the wireframe for the application. 

As showing above in Fig. 2, the wireframe details how the application will look. The wireframe also details the plan of how different screens will appear through different buttons. The arrows that extend from the button to the screen serve to show the user which screen will open when they press and release the button. However, with two exceptions, the 'Search Flight' screen and the 'Airport Map' screen both open a pop-up window when the user clicks on the 'Search' (Search Flight Screen) or 'Show Map' (Airport Flight Map Screen) button. The purpose of this wireframe diagram is to give a visual representation of the user interface design that outlines the structure and layout of the application.

## ER Diagram
![projectERdiagram](https://user-images.githubusercontent.com/111751273/221607890-1596d013-bce7-429e-8da9-3bda8b66235d.jpg)
<i>Fig. 3</i> This is the ER Diagram showing the two tables: users, allflights. 

## UML Diagram
![project3UML](https://user-images.githubusercontent.com/111751273/222328263-4e3694af-b5a2-4c57-8a6f-ae991b0908f0.jpeg)
<i>Fig. 4</i> This is the UML Diagram showing all the classes and methods that were used in the development of the application. There are 2 main parent classes which are MDApp and MDScreen, that all methods and attributes from subclasses inherit, which can be shown by the arrows.

## Flow Diagrams

Fig. 5

Fig. 6

Fig. 7
## Test Plan

| Test Type | Target | Procedure | Expected Outcome |
|-----------|--------|-----------|------------------|
| Functional: |
| Functional: |
| Functional: |
| Non-functional: |
| Non-functional: |
| Non-functional: |

## Record of Tasks
| Task No | Planned Action | Planned Outcome | Time estimate | Target completion date | Criterion |
|--------| --------- | ----------- | ---------| -------------- | ---- |
1	|	Meet with the client	|	Talk with the client to dicuss the problems they are facing and brainstorm solutions to create a plan to help the client resolve the problems.	|	15 minutes	|	2/9/2023	|	A
2	|	Brainstorm and write the problem definition	|	A clear problem definition of what the client is facing.	|	15 minutes	|	2/9/2023	|	A
3	|	Rationale for Proposed Solution	|	A clear justification that suits the client and developer.	|	15 minutes	|	2/10/2023	|	A
4	|	"Brainstorm and write down success criterias	"	|	A clear success criteria that suits the client and resolves the problem	|	20 minutes	|	2/10/2023	|	A
5	|	Brainstorm and write down a design statement for the client        	|	A clear design statement that suits the need of the client	|	15 minutes	|	2/10/2023	|	A
6	|	Write the rationale for proposed solution 	|	A clear justification that suits the client and developer.	|	30 minutes	|	2/10/2023	|	A
7	|	Create system diagram        	|	To have a clear idea of the hardware and software requirements for the proposed solution	|	45 minutes	|	2/10/2023	|	B
8	|	Follow up meeting with client	|	Present success criteria to client to get the approval	|	20 minutes	|	2/13/2023	|	A
9	|	Create a login and registration system	|	To create a program that allows the user to register and login to the application using a username and password they set up	|	1 hour	|	2/13/2023	|	C
10	|	Create password encryption	|	Using 'sha256' to encrypt password and check password in login and registration	|	45 minutes	|	2/13/2023	|	C
11	|	Create table for all flights	|	To have a table inside the database that includes all flight data	|	15 minutes	|	2/25/2023	|	C
12	|	Create an add flight page	|	Have a page that allows the user to add flights into the 'allflights' table within the database	|	2 hours	|	2/23/2023	|	C
13	|	Draw an ER Diagram and write an explaination of the diagram	|	Have a clear ER Diagram that accurately represents the different attributes and values with a brief explanation	|	45 minutes	|	2/27/2023	|	B
14	|	Create search system for specific flights	|	Allow the user to search for specific flights by flight number and date.	|	1 hour	|	2/28/2023	|	C
15	|	Draw a wire frame and write an explanation of it	|	Have a clear wire frame that accurately represents and describes the application and have a brief explanation	|	2 hours	|	2/28/2023	|	B
16	|	Create airport map page	|	Have a page that shows a map of the airport and the current date's flights at their gate	|	3 hours	|	3/1/2023	|	C
17	|	Create flight history page	|	Have a page that shows all values stored within the database	|	1 hour	|	3/1/2023	|	C
18	|	Complete finishing touches on all buttons in the application	|	Making sure that each button executes the expected task and is accurately displayed within the application	|	2 hours	|	3/1/2023	|	C
19	|	Create table displaying the results of searched flights	|	Retrieving requested data from the database of all flights, and displaying them in an organized table 	|	2 hours	|	3/1/2023	|	C
20	|	Follow up meeting with client	|	Showing the application to the client and to ask for their opinion on the applications current progress	|	10 minutes	|	3/1/2023	|	A
21	|	Finish designing the map of the airport	|	When the program for the airport map is run, it show display a map of the airport with all the terminals and gates labeled 	|	2 hours	|	3/1/2023	|	C
22	|	Connect database to the airport map and plot flights on the map	|	When the program for the airport map is run, all flights and their flight numbers for the days date will be plotted onto the map accordingly to their gate	|	1 hour	|	3/1/2023	|	C
23	|	Create the program to calculate all flight statistics	|	All flight statistics will be outputted as percentages and grouped into three categories: on time, delayed, cancelled. 	|	30 minutes	|	3/1/2023	|	C
24	|	Create flight statistics page	|	Have a page that allows the user to see statistics of flights, grouped by flight status	|	10 minutes	|	3/1/2023	|	C
25	|	Write a program that allows the user to search for flights based off flight number or date	|	The user will be able to enter flight numbers or dates to search for flights. Requested information from the user will be displayed onto a table	|	1 hour 30 minutes	|	3/1/2023	|	C
26	|	Create search flight page	|	Have a page that allows the user to search for flights.	|	10 minutes	|	3/1/2023	|	C

# Criteria C
## Techniques Used



# Criteria D: Functionality


# Citations
1. Flight Schedule Screen Turned on · Free Stock Photo. https://www.pexels.com/photo/flight-schedule-screen-turned-on-2833379/, Accessed Feb 9
2. “Welcome to KIVYMD's Documentation.” KivyMD 1.1.1 Documentation, Accessed Feburary 9
3. “SQL Tutorial.” SQL Tutorial, Accessed Feburary 9
4. Sanyal, Sayantani. 10 Reasons Why Python Is One Of The Best Programming Languages. Accessed Feburary 10, 2023
5. Advantages and disadvantages of python - how it is dominating Programming World. DataFlair. Accessed Feburary 10, 2023
6. "Kivy vs Flutter." Educba, n.d., https://www.educba.com/kivy-vs-flutter/. Accessed Feburary 10, 2023
7.  "Building a Simple Application using KivyMD in Python." GeeksforGeeks, 17 Feb. 2021, https://www.geeksforgeeks.org/building-a-simple-application-using-kivymd-in-python/, Accessed Feb 10, 2023
8. "Kivy vs PyQt." Educba, n.d., https://www.educba.com/kivy-vs-pyqt/. Accessed Feburary 10, 2023
9. Gomathy, Kavya. "5 Reasons to Use SQLite, the Tiny Giant for Your Next Project." Medium, The Startup, 4 Jan. 2022, https://medium.com/swlh/5-reasons-to-use-sqlite-the-tiny-giant-for-your-next-project-a6bc384b2df4. Accessed Feburary 10, 2023
10. Yegulalp, Serdar. "Why You Should Use SQLite." InfoWorld, IDG Communications, Inc., 13 Feb. 2019, https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html. Accessed Feburary 10, 2023
11. "SQLite Advantages and Disadvantages." javatpoint, n.d., https://www.javatpoint.com/sqlite-advantages-and-disadvantages. Accessed Feburary 10, 2023

# Appendix

### Evidence of Consultation

#### Client approval of proposed success critereas
<img width="888" alt="Screen Shot 2023-03-01 at 12 03 11 PM" src="https://user-images.githubusercontent.com/111751273/222034489-3c8880e5-e7d3-47bd-8aab-dc20a27f228b.png">

#### Clients satisfaction of the application during development process
<img width="1173" alt="Screen Shot 2023-03-01 at 12 12 44 PM" src="https://user-images.githubusercontent.com/111751273/222035637-e178d390-664c-4789-93bd-48b542e8c634.png">


## Python Code
### Main Project Code
```.py
import sqlite3
from secure_password import encrypt_password, check_password
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date

#Class used to connect with and perform tasks on an SQLite3 database
class database_worker:
    def __init__(self, name):  # name of the sqlite3 db file
        self.connection = sqlite3.connect(name)  # Establish a connection
        self.cursor = self.connection.cursor()  # Create an object that will act as a cursor to perform commands

    def search(self, query):  # Function for searching inside the db
        result = self.cursor.execute(query).fetchall()  # Run a query and fetch the result
        return result  # Return the found result

    def run_save(self, query):  # Function to save information to the db
        self.cursor.execute(query)  # Execute a query
        self.connection.commit()  # Save changes to the db

    def close(self):  # Close the connection to the db
        self.connection.close()

# Class responsible for the Homepage MDScreen
class Homepage(MDScreen):
    pass

# Class responsible for the Login MDScreen
class LoginScreen(MDScreen):
    def try_login(self):
        if self.ids.uname.text == "":
            self.ids.uname.error = True
        if self.ids.passwd.text == "":
            self.ids.passwd.error = True

        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        query = f"SELECT * from users WHERE username ='{uname}'"
        db = database_worker("unit3project.db")
        result = db.search(query=query)
        db.close()
        if len(result) == 1:
            id, email, hashed, uname = result[0]
            if check_password(user_password=passwd, hashed_password=hashed):
                self.parent.current = "Homepage"
                self.ids.uname.text = ""
                self.ids.passwd.text = ""
            else:
                print("Passwords don't match")

        if len(result) == 0:
            dialog = MDDialog(title="User not found",
                              text=f"Username '{self.ids.uname.text}' does not have an account.")
            dialog.open()
            self.ids.uname.text = ""
            self.ids.passwd.text = ""


    def try_register(self):
        print("User trying registration")
        self.parent.current = "SignupScreen"

    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.passwd.password = not self.show_password

# Class responsible for the Signup MDScreen
class SignupScreen(MDScreen):
    def try_register(self):

        uname = self.ids.uname.text
        email = self.ids.email.text
        passwd = self.ids.passwd.text
        passwd_confirm = self.ids.passwd_confirm.text
        checker = True
        if self.ids.uname.text == "":
            self.ids.uname.error = True
            checker = False
        if self.ids.email.text == "":
            self.ids.email.error = True
            checker = False
        if self.ids.passwd.text == "":
            self.ids.passwd.error = True
            checker = False
        if passwd != passwd_confirm:
            self.ids.passwd.error = True
            self.ids.passwd_confirm.error = True
            checker = False

        if checker: #password match
            #hash the password
            hash = encrypt_password(passwd)
            db = database_worker("unit3project.db")
            query = f"INSERT into users(username, password, email) values('{uname}','{hash}','{email}')"
            db.run_save(query)
            db.close()
            print("Registration completed")
            self.parent.current = "LoginScreen"

            self.ids.uname.text = ""
            self.ids.email.text = ""
            self.ids.passwd.text = ""
            self.ids.passwd_confirm.text = ""

    def cancel(self):
        self.parent.current = "LoginScreen"
        self.ids.uname.text = ""
        self.ids.email.text = ""
        self.ids.passwd.text = ""
        self.ids.passwd_confirm.text = ""

# Class responsible for the Add Flight MDScreen
class AddFlight(MDScreen):
    def add_flight(self):
        checker = True
        flight_number = self.ids.flight_number.text
        destination = self.ids.destination.text
        date = self.ids.date.text
        flight_schedule = self.ids.flight_schedule.text
        terminal = self.ids.terminal.text
        gate_number = self.ids.gate_number.text
        status = self.ids.status.text

    # Flight number validation
        if self.ids.flight_number.text == "":
            self.ids.flight_number.error = True

    # Destination validation
        if self.ids.destination.text == "":
            self.ids.destination.error = True

    # Date validation
        if self.ids.date.text == "":
            self.ids.date.error = True

    # Flight schedule validation
        if self.ids.flight_schedule.text == "":
            self.ids.flight_schedule.error = True
            checker = False

    # Terminal validation
        if self.ids.terminal.text == "":
            self.ids.terminal.error = True
            checker = False

    # Gate number validation
        if self.ids.gate_number.text == "":
            self.ids.gate_number.error = True
            checker = False


    # Status validation
        if self.ids.status.text == "":
            self.ids.status.error = True
            checker = False

        if checker:
            db = database_worker("unit3project.db")
            query = f"INSERT into allflights(flight_number, destination, date, flight_schedule, terminal, gate_number, status) values('{flight_number}', '{destination}', '{date}', '{flight_schedule}', '{terminal}', '{gate_number}', '{status}')"
            db.run_save(query)
            db.close()
            print("Flight added")

            # Create and open the alert dialog
            dialog = MDDialog(title="Flight added",
                              text=f"Flight {self.ids.flight_number.text} has been successfully added.")
            dialog.open()


            self.ids.flight_number.text = ""
            self.ids.destination.text = ""
            self.ids.date.text = ""
            self.ids.flight_schedule.text = ""
            self.ids.terminal.text = ""
            self.ids.gate_number.text = ""
            self.ids.status.text = ""

    input_format = "%m/%d/%Y"
    def validate_date(self, text):
        """
        Validate the entered date
        """
        # Check if the entered text is a valid date in the specified format
        try:
            datetime.strptime(text, self.input_format)
            print("Valid date entered!")
        except ValueError:
            self.ids.date.error = True

    def cancel(self):
        self.parent.current = "Homepage"

# Class responsible for the Flight History MDScreen
class FlightHistory(MDScreen):
    data_table = None

    def update(self):
        db = database_worker("unit3project.db")
        query = "SELECT * FROM allflights"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)

    def delete(self):
        rows_checked = self.data_table.get_row_checks()
        print("Trying to delete")
        print(rows_checked)
        db = database_worker("unit3project.db")
        for r in rows_checked:
            id = r[0]
            query = f"delete from allflights where id = {id}"
            db.run_save(query)
        db.close()
        self.update()

    def on_pre_enter(self, *args):
        #before the screen is shown, this code runs
        self.data_table = MDDataTable(
            size_hint = (.9, .8),
            pos_hint = {"center_x":.5, "center_y":.5},
            use_pagination = True,
            check = True,
            column_data = [("ID", 40), ("Flight Number", 50), ("Destination", 40),
                           ("Date", 45), ("Flight Schedule", 30), ("Terminal", 30), ("Gate Number", 30), ("Status", 30)]
        )
        #add the table
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)
        self.update()

    def row_pressed(self, table, row):
        print("Row pressed", row.text)
        row.md_bg_color = "#FFF0000"

    def check_pressed(self, table, current_row):
        print("Check pressed", current_row)

# Class responsible for the Search Flight MDScreen
class SearchFlight(MDScreen):
    data_table = None
    def search(self):
        self.data_table = MDDataTable(
            size_hint=(.9, .8),
            pos_hint={"center_x": .5, "center_y": .5},
            use_pagination=False,
            check=True,
            column_data=[("ID", 40), ("Flight Number", 50), ("Destination", 40)
                ,("Date", 45) ,("Flight Schedule", 30), ("Terminal", 30), ("Gate Number", 30),
                ("Status", 30)]
        )

        db = database_worker("unit3project.db")
        query = f"SELECT * FROM allflights WHERE flight_number = '{self.ids.flight_number.text}' or date = '{self.ids.date.text}'"
        print(query)
        data = db.search(query)
        db.close()
        if len(data) == 0:
            self.ids.flight_number.error = True
            self.ids.date.error = True
            return
        else:
            self.data_table.update_row_data(None, data)
            self.add_widget(self.data_table)
            self.ids.flight_number.text = ""
            self.ids.date.text = ""

        self.close_button = MDRectangleFlatButton(text="Close table", pos_hint={'center_x': 0.5, 'center_y': 0.15},
                                                  md_bg_color='#8dbcd6',
                                                  text_color= '#FFFFFF',
                                                  on_release=self.close_table)
        self.add_widget(self.close_button)

    def close_table(self, *args):
        self.remove_widget(self.data_table)
        self.remove_widget(self.close_button)

    def cancel(self):
        self.parent.current = "Homepage"
        self.ids.flight_number.text = ""
        self.ids.date.text = ""

# Class responsible for the Airport Map MDScreen
class AirportMap(MDScreen):
    def show_map(self):
        # Define the airport layout
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim([0, 10])
        ax.set_ylim([0, 10])
        ax.set_xticks([])
        ax.set_yticks([])

        # Add terminals
        ax.add_patch(plt.Rectangle((1, 1), 2, 2, facecolor='#C0C0C0', edgecolor='black'))
        ax.text(2, 3.2, 'Terminal 1', ha='center', va='center', fontsize=12, fontweight='bold')
        ax.add_patch(plt.Rectangle((5, 1), 2, 2, facecolor='#C0C0C0', edgecolor='black'))
        ax.text(6, 3.2, 'Terminal 2', ha='center', va='center', fontsize=12, fontweight='bold')

        # Add runway
        ax.add_patch(plt.Rectangle((2, 4), 6, 1, facecolor='#808080', edgecolor='black'))
        ax.add_patch(plt.Rectangle((2, 5), 6, 1, facecolor='#808080', edgecolor='black'))
        ax.text(5, 4.5, 'Runway 1', ha='center', va='center', fontsize=12, fontweight='bold')
        ax.text(5, 5.5, 'Runway 2', ha='center', va='center', fontsize=12, fontweight='bold')

        # Add gates
        gates = {
            'Gate A1': [1.5, 2.5],
            'Gate A2': [2.5, 2.5],
            'Gate A3': [1.5, 1.5],
            'Gate A4': [2.5, 1.5],
            'Gate B1': [5.5, 2.5],
            'Gate B2': [6.5, 2.5],
            'Gate B3': [5.5, 1.5],
            'Gate B4': [6.5, 1.5],

        }

        for gate, pos in gates.items():
            ax.text(pos[0], pos[1], gate, ha='center', va='center', fontsize=10, fontweight='bold')
            ax.add_patch(plt.Rectangle((pos[0] - 0.5, pos[1] - 0.5), 1, 1, facecolor='#F0E68C', edgecolor='black'))

        today = date.today()
        today = today.strftime("%m/%d/%Y")
        db = database_worker('unit3project.db')
        query = f"SELECT flight_number, gate_number FROM allflights where date = '{today}'"
        data = db.search(query)
        db.close()

        # Add the flight number to the gate on the graph
        for flight in data:
            flight_number = flight[0]
            gate_number = flight[1]
            gate_pos = gates['Gate ' + gate_number]
            if gate_number in ['A1', 'A3', 'B1', 'B3']:
                ax.text(gate_pos[0] - 1, gate_pos[1], flight_number, ha='center', va='center', fontsize=10,
                        fontweight='bold', color='red')
            else:
                ax.text(gate_pos[0] + 1, gate_pos[1], flight_number, ha='center', va='center', fontsize=10,
                        fontweight='bold', color='red')

        # Show the plot
        plt.show()

        self.parent.current = "Homepage"
        return

    def cancel(self):
        self.parent.current = "Homepage"

# Class responsible for the Flight Statistics MDScreen
class FlightStatistics(MDScreen):
    def on_pre_enter(self, *args):
        db = database_worker("unit3project.db")
        query_ontime = "SELECT count(status) from allflights where status = 'on time'"
        ontime = db.search(query_ontime)
        query_delayed = "SELECT count(status) from allflights where status = 'delayed'"
        delayed = db.search(query_delayed)
        query_cancelled = "SELECT count(status) from allflights where status = 'cancelled'"
        cancelled = db.search(query_cancelled)
        db.close()

        total_flights = ontime[0][0] + delayed[0][0] + cancelled[0][0]
        percent_ontime = ontime[0][0] / total_flights * 100
        percent_delayed = delayed[0][0] / total_flights * 100
        percent_cancelled = cancelled[0][0] / total_flights * 100

        self.ids.ontime.text = f"Percent of flights on time: {percent_ontime:.2f}%"
        self.ids.delayed.text = f"Percent of flights delayed: {percent_delayed:.2f}%"
        self.ids.cancelled.text = f"Percent of flights cancelled: {percent_cancelled:.2f}%"

# This class defines the main application for the Unit 3 project.
class unit3project(MDApp):
    def build(self):
        return


test = unit3project()
test.run()

```

## KV Code
```.kv
ScreenManager:

    LoginScreen:
        name: "LoginScreen"

    SignupScreen:
        name: "SignupScreen"

    Homepage:
        name: "Homepage"

    AddFlight:
        name: "AddFlight"

    FlightHistory:
        name: "FlightHistory"

    SearchFlight:
        name: "SearchFlight"

    AirportMap:
        name: "AirportMap"

    FlightStatistics:
        name: "FlightStatistics"

<LoginScreen>:
    size: 500, 500
    FitImage:
        source: "background.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#F4F4F6"

        MDLabel:
            text: "Login"
            font_style: "H2"
            size_hint: 1, .4
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, None
            height: dp(120)

            MDTextField:
                id: uname
                hint_text: "Please enter your username"
                icon_left: "account"
                helper_text_mode: "on_error"
                helper_text: "Please enter username"

            MDTextField:
                id: passwd
                hint_text: "Enter your password"
                icon_left: "lock"
                password: not show_pass.active
                helper_text_mode: "on_error"
                helper_text: "Please enter password"

            MDBoxLayout:
                orientation: "horizontal"
                size_hint: 1, None
                height: dp(40)
                MDCheckbox:
                    id: show_pass
                    size_hint_x: 0.1
                    on_active: passwd.password = not self.active
                    active: False
                MDLabel:
                    text: "Show password"
                    font_size: 25
                    size_hint_x: 0.7

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                id: login
                text: "Login"
                on_press: root.try_login()
                size_hint: .3, .4
                md_bg_color: "#8dbcd6"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: signup
                text: "Register"
                on_press: root.try_register()
                size_hint: .3, .4
                md_bg_color: "#8dbcd6"

<SignupScreen>:
    size: 500, 500
    FitImage:
        source: "background.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#F4F4F6"


        MDLabel:
            text: "Register"
            font_style: 'H2'
            size_hint: 1, .2
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            id:uname
            hint_text: "Enter username"
            icon_left: "account"
            helper_text_mode: "on_error"
            helper_text: "Username already exists"


        MDTextField:
            id:email
            hint_text: "Enter email"
            icon_left: "email"
            helper_text_mode: "on_error"
            helper_text: "Please enter email"


        MDTextField:
            id:passwd
            hint_text: "Enter password"
            icon_left: "lock"
            password: True
            size_hint: 1, .1
            helper_text_mode: "on_error"
            helper_text: "Please enter password"


        MDTextField:
            id:passwd_confirm
            size_hint: 1, .1
            hint_text: "Confirm password"

            icon_left: "lock"
            password: True

            helper_text_mode: "on_error"
            helper_text: "Password does not match"


        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                id: register_submit
                text: "Submit"
                on_press: root.try_register()
                size_hint: .3, .65
                md_bg_color: "#8dbcd6"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id:register_cancel
                text: "Cancel"
                on_press: root.cancel()
                size_hint: .3, .65
                md_bg_color: "#8dbcd6"

<Homepage>:
    size:500,500
    FitImage:
        source: "background.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#F4F4F6"

        MDLabel:
            text: "Welcome to Air Traffic Control"
            underline: True
            font_style: "H5"
            size_hint: 1, .1
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, .9
            spacing: 50

            MDFillRoundFlatIconButton:
                icon: "airplane-takeoff"
                text: "Add Flight"
                on_release: app.root.current = 'AddFlight'
                md_bg_color: "#8dbcd6"
                pos_hint: {"center_x": .5, "center_y": .5}


            MDFillRoundFlatIconButton:
                icon: "history"
                text: "Flight History"
                on_release: app.root.current = 'FlightHistory'
                md_bg_color: "#8dbcd6"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDFillRoundFlatIconButton:
                icon: "airplane-search"
                text: "Search Flight"
                on_release: app.root.current = 'SearchFlight'
                md_bg_color: "#8dbcd6"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDFillRoundFlatIconButton:
                icon: "map-marker"
                text: "Airport Flight Map"
                on_release: app.root.current = 'AirportMap'
                md_bg_color: "#8dbcd6"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDFillRoundFlatIconButton:
                icon: "information"
                text: "Flight Statistics"
                on_release: app.root.current = 'FlightStatistics'
                md_bg_color: "#8dbcd6"
                pos_hint: {"center_x": .5, "center_y": .5}

            MDFillRoundFlatIconButton:
                id: logout_button
                text: "Logout"
                icon: "logout"
                on_release: app.root.current = 'LoginScreen'
                md_bg_color: "#8dbcd6"
                pos_hint: {"center_x": .5, "center_y": .5}

<AddFlight>:
    size:500,500
    FitImage:
        source: "background.jpg"

    MDCard:
        size_hint: .85, .95
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: "#F4F4F6"
        padding: dp(10)

        MDLabel:
            text: "Add Flight"
            underline: True
            font_style: "H5"
            size_hint: 1, .05
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            id: flight_number
            hint_text: "Please enter flight number"
            icon_left: "airplane"
            helper_text_mode: "on_error"
            helper_text: "Please enter flight number"

        MDTextField:
            id: destination
            hint_text: "Please enter flight destination"
            icon_left: "airplane-takeoff"
            helper_text_mode: "on_error"
            helper_text: "Please enter flight destination"

        MDTextField:
            id: date
            hint_text: "Please enter today's date (mm/dd/yyyy)"
            icon_left: "calendar"
            on_text_validate: root.validate_date(self.text)
            helper_text_mode: "on_error"
            helper_text: "Please enter date: mm/dd/yyyy"

        MDTextField:
            id: flight_schedule
            hint_text: "Please enter flights scheduled time (--:--)"
            icon_left: "airplane-clock"
            helper_text_mode: "on_error"
            helper_text: "Please enter flights scheduled time (--:--)"

        MDTextField:
            id: terminal
            hint_text: "Please enter terminal (T1 or T2)"
            icon_left: "airport"
            helper_text_mode: "on_error"
            helper_text: "Please enter terminal (T1 or T2)"

        MDTextField:
            id: gate_number
            hint_text: "Please enter gate number (A1-A4, B1-B4)"
            icon_left: "airplane-marker"
            helper_text_mode: "on_error"
            helper_text: "Please enter gate number (A1-A4, B1-B4)"

        MDTextField:
            id: status
            hint_text: "Please enter flight status (on time, delayed, cancelled)"
            icon_left: "airplane-alert"
            helper_text_mode: "on_error"
            helper_text: "Please enter flight status (on time, delayed, cancelled)"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, None

            MDLabel:
                size_hint: .1, 1

            MDRaisedButton:
                id: addflight_submit
                text: "Submit"
                on_press: root.add_flight()
                size_hint: .2, .5
                md_bg_color: "#8dbcd6"


            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: addflight_cancel
                text: "Return home"
                on_press: root.cancel()
                size_hint: .2, .5
                md_bg_color: "#8dbcd6"

            MDLabel:
                size_hint: .1, 1

        MDLabel:
            size_hint:1, .05

<FlightHistory>:
    size:500,500
    FitImage:
        source: "background.jpg"

    MDBoxLayout:
        orientation: "vertical"

        MDLabel:
            text: "Flight History"
            underline: True
            halign: "center"
            font_style: "H4"
            size_hint: 1, .1

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .9

            MDBoxLayout:
                orientation: "horizontal"
                size_hint: .8, .1

                MDLabel:
                    size_hint: .1, 1

                MDRaisedButton:
                    id: delete_flight
                    text: "Delete Selected Flight(s)"
                    size_hint: .2, 0.65
                    pos_hint: {"center_y": .7}
                    on_press: root.delete()
                    md_bg_color: "#8dbcd6"

                MDLabel:
                    size_hint: .2, 1

                MDRaisedButton:
                    id: return_home
                    text: "Return home"
                    size_hint: .2, 0.65
                    pos_hint: {"center_y": .7}
                    on_press: app.root.current = 'Homepage'
                    md_bg_color: "#8dbcd6"

                MDLabel:
                    size_hint: .1, 1

<SearchFlight>:
    size:500,500
    FitImage:
        source: "background.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#F4F4F6"

        MDLabel:
            text: "Search Flight"
            font_style: "H3"
            size_hint: 1, .4
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, None
            height: dp(120)

            MDTextField:
                id: flight_number
                hint_text: "Please enter flight number"
                icon_left: "airplane"
                helper_text_mode: "on_error"
                helper_text: "Flight does not exist"

            MDTextField:
                id: date
                hint_text: "Please enter flight date"
                icon_left: "calendar"
                helper_text_mode: "on_error"
                helper_text: "Flight does not exist"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                id: search
                text: "Search"
                on_press: root.search()
                size_hint: .3, .4
                md_bg_color: "#8dbcd6"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: search_cancel
                text: "Return home"
                on_press: root.cancel()
                size_hint: .3, .4
                md_bg_color: "#8dbcd6"


<AirportMap>
    size:500,500
    FitImage:
        source: "background.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#F4F4F6"

        MDLabel:
            text: "Airport Map"
            font_style: "H3"
            size_hint: 1, .8
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Please click on the map to view all flights at their gate number"
            font_style: "H5"
            halign: "center"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                on_press: root.show_map()
                text: "Show Map"
                md_bg_color: "#8dbcd6"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: map_cancel
                text: "Return home"
                on_press: app.root.current = 'Homepage'
                md_bg_color: "#8dbcd6"

<FlightStatistics>:
    size:500,500
    FitImage:
        source: "background.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#F4F4F6"

        MDLabel:
            text: "Flight Statistics"
            font_style: "H4"
            underline: True
            size_hint: 1, .4
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, .8


            MDLabel:
                id: ontime
                font_size: 35

            MDLabel:
                id: delayed
                font_size: 35

            MDLabel:
                id: cancelled
                font_size: 35

            MDLabel:
                size_hint: 1, .05

            MDRaisedButton:
                id: stats_cancel
                text: "Return home"
                size_hint: .5, .1
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: app.root.current = 'Homepage'
                md_bg_color: "#8dbcd6"
```
