# Unit 3: Airport Flight Tracker System
![pexels-lt-chan-2833379](https://user-images.githubusercontent.com/111751273/217878429-b0860c83-7789-4ebb-883c-296cb0cf58e1.jpg)
<i>Pexels image</i> [1]

# Criteria A: Planning

## Problem definition
My client, air traffic control manager Zaven Galoyan is facing a major challenge in effectively managing and tracking all the relevant data pertaining to airport operations, such as flight numbers, destination/arriving from, flight schedule, terminal and gate numbers. The current manual system for keeping track of this data is time-consuming, prone to mistakes, and ineffective. The data is easily mixed up and lost, and the urgent need is to create a simple centralized manual system that can assist the air traffic control crew in managing all of this information quickly and effectively without relying on automated inputs.

## Success Criteria
1. The application will have a login and registration system.
2. The application will allow the user to input all attributes (flight number, destination, flight schedule, terminal, and gate number) and will be stored into the database through the interface.
3. The application will allow user to search for flights by date and flight number.
4. The application will allow the user to view all values stored in the database.
5. The application will have a page that accesses a map of the airport and the location of all flights at their gate.
6. The application will have a statistics page that includes percentages of all flights categorized by cancelled, delayed, and on-time. 

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
![project3uml (1)](https://user-images.githubusercontent.com/111751273/223026201-2b814d9a-bbab-4fc1-8fdd-f006761bf004.jpeg)
<i>Fig. 4</i> This is the UML diagram for the application, which displays the classes and methods that were used in its development. The diagram includes two main parent classes: MDApp and MDScreen. All subclasses inherit methods and attributes from these parent classes, as indicated by the arrows in the diagram.

## Flow Diagrams
![project3flowchart1](https://user-images.githubusercontent.com/111751273/222959574-c2700376-0e36-4e39-9bf6-49b6e391d8d6.jpeg)
<i>Fig. 5</i> This is the flow diagram that details the process of how the search method works. 

This method is used to search for flight information in a database. It creates a table using the MDDataTable class and specifies the columns of the table. It then connects to a SQLite database using a database_worker class and runs a SQL query to search for flight information based on the flight number or date provided by the user. If data is found, it updates the table with the search results and displays it on the screen. If no data is found, it displays an error message using a pop-up dialog.

![project3flowchart2 jpg](https://user-images.githubusercontent.com/111751273/222961252-2696019e-96c7-40d0-826f-06838853b379.jpeg)
<i>Fig. 6</i> This is the flow diagram that details the process of how the add flight method works. 

This method is used to add flight information to a database. It first validates the input fields to ensure that they are not empty. If all the fields are valid, it connects to a SQLite database using the database_worker class and runs an SQL query to insert the flight information into the database. It then displays a pop-up message indicating that the flight has been successfully added to the database. Finally, it clears the input fields so that the user can add another flight.

![project3flowchart3 jpg (1)](https://user-images.githubusercontent.com/111751273/223020533-453cc1e2-da9d-4d22-a47e-d57c31416998.jpeg)
<i>Fig. 7</i> This is the flow diagram that details the process of how the delete method works.

This is a method that is used to delete checked rows in a table. First, it gets the checked rows from the table. Then it connects to a SQLite database and loops through each checked row to execute a delete query for that particular row using the id field as a reference. After each row is deleted, an alert dialog is created and opened to confirm that the row has been successfully deleted. Finally, the database connection is closed and the table is updated to reflect the changes.
## Test Plan

| Description | Test Type|  Input | Expected Output |
|-----------|--------|-------|------------------|
| Test for Registration System | Unit test | 1. Run unit3project.py file 2. Click the Register button on the application screen 3. Input the appropiate information in each textfield following the hint text 4. Click register | After clicking the register button, if the user already exists, a pop up message will appear letting the user know that the username already exists. If the password entered and the confirm password don't match, a red message will appear and notify the user that the passwords do not match. If all instructions were correctly followed it will take the user back to the Login screen.
|  Test for Login System | Unit test | 1. Run  unit3.project.py file 2. Follow instructions and enter the appropiate information in each textfield following the hint text 3. Click Login 4 | After clicking login, if the account does not exist, a pop up message will appear letting the user know that the account was not found. If the account credentials do exist, it should take the user to the homepage. |
|  Test for Logout System | Unit test | 1. Login 2. Press the logout button on the homepage  | When the logout button is pressed, it should direct the user back to the log in screen |
|   Test for Add Flight System   | Unit test | 1. Login 2. Click Add Flight button 3. Enter the appropiate flight information in the textfields accordingly to the hint text. 4. Press add flight button | When the user enters flight information correctly, a pop up message should appear telling the user that the flight has been added. When a piece of information is incorrect within the textfield, error hint texts in red will appear to show the user that the information entered was incorrect.
| Test for allflights database | Integration test | 1. Login 2. Click Add Flight button 3. Enter the appropiate flight information in the textfields accordingly to the hint text. 4. Press add flight button 5. Open unit3project.db and go to allflights table | When the flight is added, it should be stored into the database, and stored in the allflights table. Everytime the user adds a flight, it should update and appear in the allflights table.
|  Test for Flight History Screen | Unit test | 1. Login 2. Click Flight History button | When the Flight History button is clicked, it should direct the user to another page that displays a table of all past and recent flight information entered from the user. |
| Test delete function for Flight History Screen | Unit test | 1. Login 2. Click Flight History button 3. Select a row 4. Click delete selected flight(s) button. | When the user clicks on the checkbox next to the flight, a checkmark should appear within the box. Then when they click the delete flight(s) button, the selected flight(s) should delete from the table |
| Test for Search Flight Screen | Unit test | 1. Login 2. Click Search Flight button | When the Search Flight button is clicked, it should direct the user to another page that will allow the user to search for specific flight information. | 
| Test for Search Flight System | Integration test | 1. Login 2. Click Search Flight button 3. Enter the appropiate information in the textfields accordingly to the hint text 4. Press the search flight button | When the user has entered appropiate flight information for the flight they are searching for, a table of just that single flight or multiple flights should appear. They can search for flights with just the flight number, date, or both. If the pieces of information entered is incorrect, an error hint text will appear letting the user know that the flight does not exist. The information being showed on the table should be retrieved from the database, and show the correct flight searched by the user. |
| Test for Airport Flight Map Screen | Unit test  |1. Login 2. Click Airport Flight Map button | When the Airport Flight Map button is clicked, it should direct the user to another page that will allow the user to see the map, or return back home | 
| Test for Airport Flight Map | Integration test | 1. Login 2. Click Airport Flight Map button 3. Click Show Map | When the show map button is pressed, a new window should open, showing the user a map of the whole airport, all terminals and gates. Further, it should display the flight numbers at their assigned gates for the current day. This data should be retrieved from the database, getting all flights for the current day, and accurately placing the flight numbers at the correct gate. |
| Test for Flight Statistics Screen | Unit test | 1. Login 2. Click Flight Statistics button | When the Flight Statistics button is clicked, it should direct the user to another page that will shows all flight statistics. It should have three lines of data. The percentages for flights on time, delayed, and cancelled. | 
| Code Review | Code Review | Reviewing if the code has adequate comments, function names, and variable names: 1. Open unit3project.py file. 2. Review the code and make changes or add comments where it is necessary | Revised version of the code that is easy to follow and understand | 


## Record of Tasks
| Task No | Planned Action| Planned Outcome | Time estimate | Target completion date | Criterion |
|---------|---------------|------------------|---------------|------------------------|-----------|
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
15	|	Draw a wire frame and write an explanation of it	|	Have a clear wire frame that accurately represents and describes the application and have a brief explanation	|	1 hour	|	2/28/2023	|	B
16	|	Create airport map page	|	Have a page that shows a map of the airport and the current date's flights at their gate	|	3 hours	|	3/1/2023	|	C
17	|	Create flight history page	|	Have a page that shows all values stored within the database	|	1 hour	|	3/1/2023	|	C
18	|	Complete finishing touches on all buttons in the application	|	Making sure that each button executes the expected task and is accurately displayed within the application	|	1 hour	|	3/1/2023	|	C
19	|	Create table displaying the results of searched flights	|	Retrieving requested data from the database of all flights, and displaying them in an organized table 	|	1 hour	|	3/1/2023	|	C
20	|	Follow up meeting with client	|	Showing the application to the client and to ask for their opinion on the applications current progress	|	10 minutes	|	3/1/2023	|	A
21	|	Finish designing the map of the airport	|	When the program for the airport map is run, it show display a map of the airport with all the terminals and gates labeled 	|	2 hours	|	3/1/2023	|	C
22	|	Connect database to the airport map and plot flights on the map	|	When the program for the airport map is run, all flights and their flight numbers for the days date will be plotted onto the map accordingly to their gate	|	1 hour	|	3/1/2023	|	C
23	|	Create the program to calculate all flight statistics	|	All flight statistics will be outputted as percentages and grouped into three categories: on time, delayed, cancelled. 	|	30 minutes	|	3/1/2023	|	C
24	|	Create flight statistics page	|	Have a page that allows the user to see statistics of flights, grouped by flight status	|	10 minutes	|	3/1/2023	|	C
25	|	Write a program that allows the user to search for flights based off flight number or date	|	The user will be able to enter flight numbers or dates to search for flights. Requested information from the user will be displayed onto a table	|	1 hour 30 minutes	|	3/1/2023	|	C
26	|	Create search flight page	|	Have a page that allows the user to search for flights.	|	10 minutes	|	3/1/2023	|	C
27	|	Create UML Diagram and write a brief description 	|	Have a clear UML Diagram that accurately shows the different classes and methods used with a brief explanation	|	30 minutes	|	3/2/2023	|	B
28	|	Write the test plans	|	Procedures one should take to test the program and the expected outcome of each test is recorded 	|	45 minutes	|	3/2/2023	|	B
29  | Create flow diagrams and write brief explanations for each| Have accurate flow diagrams for different parts of the porgram with brief explanations | 1 hour | 3/5/2023 | B
30	|	Finish Criteria C	|	Write the descriptions of the code and the detail of the techniques that were used 	|	2 hours	|	3/5/2023	|	C

# Criteria C: Development
## Techniques Used
1. Object Oriented Programming (OOP)
2. KivyMD Library
3. SQLite Database
4. For loops
5. If statements
6. Matplotlib
7. Functions
8. Classes
9. Inheritence

## Development of User Interface Using KivyMD

### Screen Manager
```.kv
ScreenManager:

    LoginScreen:
        name: "LoginScreen"
```
The client requires an application that allows them to record and store flight information. Developing a user interface is best fit for thier need as it is easier to use and visually appealing.

The KV code snippet above shows a ScreenManager with a single screen called "LoginScreen". To create additional screens for the flight information application, I followed a similar structure by defining each screen with a unique name and id within the ScreenManager. For example, I created a signup screen with a name of "SignupScreen". I repeated this process for each screen in the application, such as the "Homepage" screen, "AddFlight" screen, "FlightHistory" screen, "SearchFlight" screen, "AirportMap" screen, and "FlightStatistics" screen.

Each screen is defined using a separate KV code block that specifies the layout and widgets for that screen. For example, the "AddFlight" screen might include text input fields for the user to enter flight information, while the "FlightHistory" screen might display a list of previously recorded flights.

By using a ScreenManager and defining each screen as a separate widget, I can easily switch between screens and manage the application flow. For example, when the user logs in or signs up, I can switch from the "LoginScreen" or "SignupScreen" to the "Homepage" screen. Similarly, I can navigate from the "Homepage" screen to the "AddFlight" screen when the user wants to record a new flight, or to the "FlightHistory" screen to view past flights. This approach allows for a more organized and user-friendly interface, and can help improve the overall user experience.

### General Application Screen
```.kv
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
```
This is a Kivy language code block defining the visual layout of a screen named "LoginScreen". This is an example of one of many screens in the application. MDCard is a component in the KivyMD library that represents a rectangular card with rounded corners, which can contain other widgets inside it. I use this as the general basic set up of each screen in the application, so all screens had the same set up and background image, as my client wanted a professional and clean aesthetic look.

### MDFillRoundFlatIconButton
```.kv
MDFillRoundFlatIconButton:
    icon: "airplane-takeoff"
    text: "Add Flight"
    on_release: app.root.current = 'AddFlight'
    md_bg_color: "#8dbcd6"
    pos_hint: {"center_x": .5, "center_y": .5}
```
The KV code above shows one of the homepage buttons that will direct the user to the defined screen in ScreenManager. This kind of button used in the homepage is simple and visually appealing, fitting the client's needs for professionality and clean aesthetic appearance. This is one of the buttons I had decided to use, to add variety in the shapes of buttons I had. The other button I used was MDRaisedButton, which is basically the same as the button shown in the code above, but it just does not have an icon or circular shape.

### MDLabel
```.kv
MDLabel:
    text: "Welcome to Air Traffic Control"
    underline: True
    font_style: "H5"
    size_hint: 1, .1
    halign: "center"
    pos_hint: {"center_x": .5, "center_y": .5}
```
This is the KV code for an MDLabel. MDLabels are text labels on the screen that serve as indicators to guide the user on where they are in the application. In this case, I used the MDLabel as the title for my homepage screen, which allows the user to know that they have entered the air traffic control application.

### MDTextField
```.kv
MDTextField:
    id: destination
    hint_text: "Please enter flight destination"
    icon_left: "airplane-takeoff"
    helper_text_mode: "on_error"
    helper_text: "Please enter flight destination"
```
This is an example of an MDTextField I used for my client's application. MDTextFields are text fields on the applications page that allows the user to input information through their keyboard. This is an important aspect to the user interface for my client's application as it will allow them to input information they want into the program. When I was programming the MDTextFields, I realized that there is a high chance for the user to make mistakes when typing information into the MDTextField. As shown above, I have helper text, so when the user forgets to input a piece of information, an error will appear in red helper text to guide the user.

### MDCheckbox
```.py
MDCheckbox:
    id: terminal1
    group: 'terminals' #this group is so that all the checkboxes are linked and only one can be selected
    size_hint: None, None
    size: dp(48), dp(48)
    active: True
    on_active: root.checkbox_click(self, self.active, "T1")
    pos_hint: {"center_y":.5}
```
This is a KivyMD widget that creates a checkbox. This is an example of how I used MDCheckbox for the selection of certain values. The checkbox has an ID of "terminal1", which can be used to reference the widget in the Python code. The "group" property is set to "terminals", which means that this checkbox is part of a group of checkboxes with the same group name. Only one checkbox in the group can be selected at a time. I use this for other parts of the application such as for selecting the gate number and flight status.


## Development of Application Using Python

### Database Handler
#### Accessing Information Inside of the Database
```.py
def search(self, query):  # Function for searching inside the db
    result = self.cursor.execute(query).fetchall()  # Run a query and fetch the result
    return result  # Return the found result
```
This is a method called search that takes a query parameter as input. The method executes the query using a cursor object and fetches all the results using the fetchall() method. The result is stored in the result variable and then returned to the user. This method can be used to search for records in a database table by executing a SQL query provided as the query parameter. Its usage allows me to acquire query results across areas of development throughout the application necessary for my solution and my client's needs. 

### Login System
#### User Credential Verification
```.py
# Check if password matches
if len(result) == 1:
    id, email, hashed, uname = result[0]
    if check_password(user_password=passwd, hashed_password=hashed):
        self.parent.current = "Homepage"
        self.ids.uname.text = ""
        self.ids.passwd.text = ""
    else:
        print("Passwords don't match")
```
This is the program used for the login system. As shown in the code above, this program works by checking if anything with a length of one or greater is returned. Then after that, the code verifies if the inputted password matches with the password stored in the database under the username entered. This meets the first criteria of having a login system. I was able to apply this method to other parts of the code such as the register and search flight system to check if data inputted exists or not.

#### Pop Up Message
```.py
# If username does not exist, a pop up message will appear
if len(result) == 0:
    dialog = MDDialog(title="User not found",
                      text=f"Username '{self.ids.uname.text}' does not have an account.")
    dialog.open()
    self.ids.uname.text = ""
    self.ids.passwd.text = ""
```

When programming the login system, I came across the challenge of how I was going to show two different error messages, due to the fact that helper texts can only be used once for each MDTextField. I was able solve this by discovering MDDialog (pop up message) on the KivyMD website[2]. As shown in the code above, I display pop up message when a username entered does not exist. This increases both the professionality and quality of the application for my client. I was able to use this method in other parts of the application such as the register, add flight, and search flight systems.

### Registration System

#### Password Policy
```.py
pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*()_+]).{8,}$'
# Check if the password matches the pattern
if not re.match(pattern, passwd):
    self.ids.passwd.error = True
    return
```


This is the password policy I use to increase the security of the application. It requires the user to input a password that is at least 8 characters long, contains at least 1 digit, 1 lowercase letter, and 1 special character. This fits my client's need for increased protection of the stored data, as passwords that meet these criteria have a lower likelihood of being guessed or cracked. 

I found it challenging at first trying to figure out how to create a secure password policy for my application. I knew that I needed to require users to create strong passwords, but I wasn't sure what criteria to use or how to implement them. I also wanted to make sure that my policy was up-to-date and followed best practices for password security. After doing some research online, I came across Stack Overflow, which is a great resource for developers and students like myself. I found a post on Stack Overflow that explained how to use regular expressions to validate password strength, and it provided some example code that I could use as a starting point for my own implementation [15].

To implement this policy, I used the "re" module from the Python standard library, which provides support for regular expressions. Regular expressions are a powerful tool for text processing and pattern matching, and in this case, I used them to define a pattern that checks for the required password criteria. The pattern I used is: r'^(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*()_+]).{8,}$'

This pattern consists of several parts, including positive lookahead assertions that check for the presence of at least one digit, one lowercase letter, and one special character, and a minimum length of 8 characters. I then used the "re.match()" function to check if a given password matches this pattern. If the password does not meet the criteria, the user is prompted to input a stronger password. This policy helps to increase the security of the application and protect the sensitive data stored within it.

### Add Flight System
#### Missing Value Validation
```.py
# Flight number validation
if self.ids.flight_number.text == "":
    self.ids.flight_number.error = True
```
This piece of code is used for validating the user input in the add flights page. It ensures that the user has typed something into the textfield, and if not, it raises and error. This is an important aspect of the application to my client as there can not be missing values for flight information. By using this method of validation, I reduce the risk for mistakes and missing pieces of information. I use this throughout the application where there are textfields that are required to be filled out.

#### Time Picker
```.py
# Time picker
def show_time_picker(self):
    from datetime import datetime

    # Define default time
    default_time = datetime.strptime("12:00", '%H:%M').time()

    time_dialog = MDTimePicker(
        primary_color="#8dbcd6",
        accent_color = "#f4f4f4",
        text_button_color = "#f4f4f4",
    )
    # Set default Time
    time_dialog.set_time(default_time)
    time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time, on_save=self.on_save_time)
    time_dialog.open()
```
MDTimePicker is a time picker widget in the KivyMD library that allows users to easily select a time. The code snippet above shows how I integrated MDTimePicker into my application to allow users to input time. By using MDTimePicker, users can easily select the time they want in a format that is easy to understand. This reduces the possibility of user mistakes and increases efficiency. As you can see in the code, the "open_picker" method opens the time picker, and the "on_save" method saves the time selected in the correct format "hh:mm". Overall, the integration of MDTimePicker has made the time input process much easier and more efficient for the user.


#### Date Picker
```.py
# Date calendar picker
    def date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.selected_date = value
        value = value.strftime("%m/%d/%Y")
        self.ids.date.text = f"{value}"
```
The piece of code above shows how I allowed the user to input date. The application is sensitive to the date inputted, as it needs to be in the exact format it is asking for. This is because later on the database will match the date inputted to the date stored to retrieve stored information. This was a challenge as I needed the date in a specific format. However, after doing some research, I found that using the date picker from KivyMD library was the best option, as it makes it easier to choose a specific format of the date I wanted [2]. As you can see in the code, the "date" method opens the calander, and the "on_save" method saves the date selected in the correct format "mm/dd/yyy". I also use this method in the search system of the application to increase efficieny and reduce the possibilities of user mistakes.

#### Checkboxes
```.py
# Checkboxes
def checkbox_click(self, checkbox, value, terminal):
    if value:  # if the check is true
        self.selected_location = terminal
        print(terminal)
        self.ids.terminal.text = f"{terminal}"
```

To decrease the possibility of human errors, I decided to use checkboxes to select certain values such as the terminal. Instead of having the user have to type in which terminal the flight is in, they can just select the right one using a checkbox. The method shown in the code above handles the click event of a checkbox. The method takes three arguments, checkbox, value, and terminal. If the value of the checkbox is true (meaning it has been checked), the method sets the value of the selected_location attribute to the terminal value. It then sets the text of the terminal to the selected terminal, and when the user adds the flight, the selected terminal is inputted into the database. I use this more than once, for other values such as gate numbers and the statuses of flights, and in other parts of the application such as the login and registration system.


#### Insert Query
```.py
db = database_worker("unit3project.db")
query = f"INSERT into allflights(flight_number, destination, date, flight_schedule, terminal, gate_number, status) values('{flight_number}', '{destination}', '{date}', '{flight_schedule}', '{terminal}', '{gate_number}', '{status}')"
db.run_save(query)
db.close()
```
The is the program used to add flights into the database. My client requested to have a system that allows the them to enter flight information and store them. In order to do this, I used executed a query in the program that inserts flight information into a table inside the database (allflights table).

This code inserts data into a database table called "allflights" using the information provided by the variables flight_number, destination, date, flight_schedule, terminal, gate_number, and status. The database connection is created using the database_worker function and the unit3project.db database file. The SQL query is constructed using the query variable by inserting the values from the variables. Then, the run_save method is used to execute the SQL query and save the changes to the database. Finally, the database connection is closed using the close method.This system fulfills the second criteria, by having the application allow the user to input all attributes (flight number, destination, flight schedule, terminal, and gate number) and store them into the database. I also used this insert query method in other parts of the program such as the register system.


### Flight History System
#### Data Table
```.py
# Displays the table on the screen
def on_pre_enter(self, *args):
    self.data_table = MDDataTable(
        size_hint = (.9, .8),
        pos_hint = {"center_x":.5, "center_y":.5},
        use_pagination = True,
        check = True,
        column_data = [("ID", 40), ("Flight Number", 50), ("Destination", 40),
                       ("Date", 45), ("Flight Schedule", 30), ("Terminal", 30), ("Gate Number", 30), ("Status", 30)]
    )
    self.add_widget(self.data_table)
    self.update()
```
The piece of code above shows how I am able to display a table with data onto the screen. I use a select query before this, to retrieve all the necessary data, then display it onto the table using the program above. I used this method for other parts of the application such as the search flight system. However, while programming the table to show data, I did come across the challenge of being able to close the table. After attempting to use a pop up window, I decided that using a button to close the table screen was the better option, as it was more user friendly and visually appealing. 

### Search Flight System
#### Select Query
```.py
db = database_worker("unit3project.db")
query = f"SELECT * FROM allflights WHERE flight_number = '{self.ids.flight_number.text}' or date = '{self.ids.date.text}'"
print(query)
data = db.search(query)
db.close()
```
The program above details how the application will access the database and search for the flight the user is looking for. I executed a query in the program that selects specific data from a specifc table within the database.

This code queries a database table called allflights using the database_worker function and the unit3project.db database file. The SQL query is constructed using the f-string formatting and searches for all the rows in the table where the flight_number is equal to the text entered in an element with an id of flight_number or the date is equal to the text entered in an element with an id of date. The search method of the database_worker class is used to execute the SQL query and retrieve the matching data from the database. The retrieved data is stored in the data variable.

I use this select query method in other parts of the program such as the login system. The program takes the username inputted by the user to try and select a match within the users table to see if the user exists. This fulfills the third criteria by allowing the user to search for flights by date and flight number to locate specific flights. Further, I use this select query method in other parts of the program such as the login, airport map, and flight statistics system. 

### Airport Flight Map System
#### Plotting Airport Map
```.py
# Add terminal
ax.add_patch(plt.Rectangle((1, 1), 2, 2, facecolor='#C0C0C0', edgecolor='black'))
ax.text(2, 3.2, 'Terminal 1', ha='center', va='center', fontsize=12, fontweight='bold')
```
This code above is a part of the program I created in plotting the map of the airport. I used the matplotlib library in python to help me create a map of the airport on a graph [13]. The code above shows how I was able to plot the terminal. I repeated the same method to plot the other terminal and runways for the rest of the airport map. This meets my client's request to have a page that accesses a map of the airport. 

#### Plotting Flight Numbers
```.py
# Retrieve today's flight
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
```
The program above shows how the application displays a labelled map of the airport with all the flights at their assigned gates. This was one of the biggest challenges I had when programming map. I had to meet my client's need of plotting the location of all flights at their gate. This was because I needed to gather all the flights for the current day's date. I was able to achieve this by using the datetime library [12]. After I was able to retrieve only the current day's flights, I could plot the flight numbers at their assigned terminals and gates using if statements and lists, as shown in line 5 in the code above.   

### Flight Statistics System
#### Calculating Flight Statistics
```.py
# On time, delayed, and cancelled values are queried from table in database
total_flights = ontime[0][0] + delayed[0][0] + cancelled[0][0]
percent_ontime = ontime[0][0] / total_flights * 100
percent_delayed = delayed[0][0] / total_flights * 100
percent_cancelled = cancelled[0][0] / total_flights * 100
```
The program above details how I was able to calculate the statistics for all flights. My client wanted a page that would show the different statistics of flight statuses; for all flights on time, delayed, and cancelled. I chose to represent each statistic in percentage form, as it would give my client an easy way to compare the different flight statistics.

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
12. Python Software Foundation. “datetime — Basic Date and Time Types.” Python 3 Documentation, 2021, https://docs.python.org/3/library/datetime.html. Accessed March 2, 2023
13. "Matplotlib." Matplotlib, https://matplotlib.org/., Accessed March 2, 2023
14. ChatGPT. OpenAI, 2023, https://openai.com/. Accessed March 2, 2023
15. Stack Overflow. "Validation of a Password - Python." Stack Overflow, 14 Dec. 2016, https://stackoverflow.com/questions/41117733/validation-of-a-password-python. Accessed March 5, 2023


# Appendix

## Evidence of Consultation

### Client approval of proposed success critereas
<img width="1001" alt="Screen Shot 2023-03-06 at 11 19 48 AM" src="https://user-images.githubusercontent.com/111751273/223004760-b79bb2c4-7aa5-4be0-9025-7550eeb5233c.png">

### Client's review of application during development process
<img width="1173" alt="Screen Shot 2023-03-01 at 12 12 44 PM" src="https://user-images.githubusercontent.com/111751273/222035637-e178d390-664c-4789-93bd-48b542e8c634.png">

### Client's review of final product
<img width="1165" alt="Screen Shot 2023-03-05 at 10 34 02 PM" src="https://user-images.githubusercontent.com/111751273/222963697-2049e75d-386d-4b28-b9ff-bf0c1a78d266.png">



## Python Code
```.py
import sqlite3
from secure_password import encrypt_password, check_password
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.button import MDFlatButton
import re
import matplotlib.pyplot as plt
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
    # Function to log out the user
    def try_logout(self):
        # Create an MDDialog to confirm whether the user wants to sign out or not
        self.sign_out_confirmation_dialog = MDDialog(
            title="Logout",
            text="Are you sure you want to logout?",
            buttons=[
                MDFlatButton(
                    text="Yes",
                    on_release=self.log_out_user
                ),
                MDFlatButton(
                    text="No",
                    on_release=self.dismiss_dialog
                ),
            ],
        )
        self.sign_out_confirmation_dialog.open()

    def log_out_user(self, instance):
        # Perform the signout actions
        print("User logging out")
        self.parent.current = "LoginScreen"
        self.sign_out_confirmation_dialog.dismiss()

    def dismiss_dialog(self, instance):
        self.sign_out_confirmation_dialog.dismiss()

# Class responsible for the Login MDScreen
class LoginScreen(MDScreen):
    def try_login(self):
        if self.ids.uname.text == "":
            self.ids.uname.error = True
        if self.ids.passwd.text == "":
            self.ids.passwd.error = True

        # Check if username exists
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        query = f"SELECT * from users WHERE username ='{uname}'"
        db = database_worker("unit3project.db")
        result = db.search(query=query)
        db.close()

        # Check if password matches
        if len(result) == 1:
            id, uname, hashed = result[0]
            if check_password(user_password=passwd, hashed_password=hashed):
                self.parent.current = "Homepage"
                self.ids.uname.text = ""
                self.ids.passwd.text = ""
            else:
                self.ids.passwd.error = True
                print("Passwords don't match")

        # If username does not exist
        if len(result) == 0:
            dialog = MDDialog(title="User not found",
                              text=f"Username '{self.ids.uname.text}' does not have an account.")
            dialog.open()
            self.ids.uname.text = ""
            self.ids.passwd.text = ""

    # When the user clicks the "Register" button
    def try_register(self):
        print("User trying registration")
        self.parent.current = "SignupScreen"
        self.ids.uname.text = ""
        self.ids.passwd.text = ""

    # Function to toggle the password visibility
    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.passwd.password = not self.show_password

# Class responsible for the Signup MDScreen
class SignupScreen(MDScreen):
    def try_register(self):
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        passwd_confirm = self.ids.passwd_confirm.text
        checker = True
        # Check if all fields are filled
        if self.ids.uname.text == "":
            self.ids.uname.error = True
            checker = False
        if self.ids.passwd.text == "":
            self.ids.passwd.error = True
            checker = False

        pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*()_+]).{8,}$'
        # Check if the password matches the pattern
        if not re.match(pattern, passwd):
            self.ids.passwd.error = True
            return

        if passwd != passwd_confirm:
            self.ids.passwd_confirm.error = True
            checker = False

        # Check if username exists
        db = database_worker("unit3project.db")
        query = f"SELECT * from users WHERE username ='{uname}'"
        result = db.search(query=query)
        # If user exists, a pop up message will appears
        if len(result) == 1:
            dialog = MDDialog(title="User exists",
                              text=f"The username you entered: {self.ids.uname.text} already exists.")
            dialog.open()
            self.ids.uname.text = ""
            self.ids.passwd.text = ""
            self.ids.passwd_confirm.text = ""

        elif checker:
            # Inserts the new user into the database and hashes their password
            hash = encrypt_password(passwd)
            query = f"INSERT into users(username, password) values('{uname}','{hash}')"
            db.run_save(query)
            db.close()
            dialog = MDDialog(title="Registration completed",
                              text=f"Your account has been successfully registered.")
            dialog.open()
            print("Registration completed")
            self.parent.current = "LoginScreen"

            self.ids.uname.text = ""
            self.ids.passwd.text = ""
            self.ids.passwd_confirm.text = ""

    # Function to toggle the password visibility
    def toggle_show_password(self):
        self.show_password = not self.show_password
        self.ids.passwd.password = not self.show_password
        self.ids.passwd_confirm.password = not self.show_password

    # When the user clicks the "Cancel" button
    def cancel(self):
        self.parent.current = "LoginScreen"
        self.ids.uname.text = ""
        self.ids.uname.error = False
        self.ids.passwd.text = ""
        self.ids.passwd.error = False
        self.ids.passwd_confirm.text = ""
        self.ids.passwd_confirm.error = False

# Class responsible for the Add Flight MDScreen
class AddFlight(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_date = None
        self.selected_terminal = None
        self.selected_gate = None

    def get_time(self, instance, time):
        self.ids.flight_schedule.text = time.strftime("%H:%M")
    # Cancel
    def on_cancel(self, instance, time):
        instance.dismiss()

    # Time picker
    def show_time_picker(self):
        from datetime import datetime

        # Define default time
        default_time = datetime.strptime("12:00", '%H:%M').time()

        time_dialog = MDTimePicker(
            primary_color="#8dbcd6",
            accent_color = "#f4f4f4",
            text_button_color = "#f4f4f4",
        )
        # Set default Time
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time, on_save=self.on_save_time)
        time_dialog.open()

    def on_save_time(self, instance, value):
        self.selected_time = value
        value = value.strftime("%H:%M")
        self.ids.flight_schedule.text = f"{value}"

    # Date calendar picker
    def date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.selected_date = value
        value = value.strftime("%m/%d/%Y")
        self.ids.date.text = f"{value}"

    # Checkboxes
    def checkbox_click(self, checkbox, value, terminal):
        if value:  # if the check is true
            self.selected_location = terminal
            print(terminal)
            self.ids.terminal.text = f"{terminal}"

    def checkbox_click_gate(self, checkbox, value, gate_number):
        if value:  # if the check is true
            self.selected_location = gate_number
            print(gate_number)
            self.ids.gate_number.text = f"{gate_number}"

    def checkbox_click_status(self, checkbox, value, status):
        if value:  # if the check is true
            self.selected_location = status
            print(status)
            self.ids.status.text = f"{status}"

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
            checker = False

    # Destination validation
        if self.ids.destination.text == "":
            self.ids.destination.error = True
            checker = False

        if checker:
            db = database_worker("unit3project.db")
            query = f"INSERT into allflights(flight_number, destination, date, flight_schedule, terminal, gate_number, status) values('{flight_number}', '{destination}', '{date}', '{flight_schedule}', '{terminal}', '{gate_number}', '{status}')"
            db.run_save(query)
            db.close()

            # Pop up message
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

    def clear(self):
        self.ids.flight_number.text = ""
        self.ids.destination.text = ""
        self.ids.date.text = ""
        self.ids.flight_schedule.text = ""
        self.ids.terminal.text = ""
        self.ids.gate_number.text = ""
        self.ids.status.text = ""

    def cancel(self):
        self.parent.current = "Homepage"

# Class responsible for the Flight History MDScreen
class FlightHistory(MDScreen):
    data_table = None

    # Gets all data from allflights table from the database
    def update(self):
        db = database_worker("unit3project.db")
        query = "SELECT * FROM allflights"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)

    def delete(self):
        # Function to delete checked rows in the table
        checked_rows = self.data_table.get_row_checks()  # Get the checked rows
        print(checked_rows)
        # delete
        db = database_worker("unit3project.db")
        for r in checked_rows:
            id = r[0]  # use item_id instead of id
            print(id)
            query = f"delete from allflights where id = {id}"  # use item_id instead of id
            print(query)
            db.run_save(query)
            # Create and open the alert dialog to confirm item has been deleted
            dialog = MDDialog(title="Thank you, flight deleted!",
                              text=f"Flight {id} has successfully been deleted.")
            dialog.open()
        db.close()
        self.update()

    # Displays the table on the screen
    def on_pre_enter(self, *args):
        self.data_table = MDDataTable(
            size_hint = (.9, .8),
            pos_hint = {"center_x":.5, "center_y":.5},
            use_pagination = True,
            check = True,
            column_data = [("ID", 40), ("Flight Number", 50), ("Destination", 40),
                           ("Date", 45), ("Flight Schedule", 30), ("Terminal", 30), ("Gate Number", 30), ("Status", 30)]
        )
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)
        self.update()

    # When a row is pressed
    def row_pressed(self, table, row):
        print("Row pressed", row.text)
        row.md_bg_color = "#FFF0000"

    # When a row is checked
    def check_pressed(self, table, current_row):
        print("Check pressed", current_row)

# Class responsible for the Search Flight MDScreen
class SearchFlight(MDScreen):
    data_table = None

    # Date calendar picker
    def date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.selected_date = value
        value = value.strftime("%m/%d/%Y")
        self.ids.date.text = f"{value}"

    # Retrieves the data from the database based on the flight number or date entered
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
        data = db.search(query)
        db.close()
        # If no data is returned, display an error message
        if self.ids.flight_number.text == "" :
            self.ids.flight_number.error = True
        # if self.ids.date.text == "":
        #     self.ids.date.error = True
        if len(data) == 0:
            # Pop up message
            dialog = MDDialog(title="Flight not found",
                              text=f"Flight entered does not exist.")
            dialog.open()
            return
        # If data is returned, display the table
        else:
            self.data_table.update_row_data(None, data)
            self.add_widget(self.data_table)
            self.ids.flight_number.text = ""
            self.ids.date.text = "Select flight date"

        # Button for closing the table
        self.close_button = MDRectangleFlatButton(text="Close table", pos_hint={'center_x': 0.5, 'center_y': 0.15},
                                                  md_bg_color='#8dbcd6',
                                                  text_color= '#FFFFFF',
                                                  on_release=self.close_table)
        self.add_widget(self.close_button)

    # Closes the table
    def close_table(self, *args):
        self.remove_widget(self.data_table)
        self.remove_widget(self.close_button)

    # When the cancel button is pressed
    def cancel(self):
        self.parent.current = "Homepage"
        self.ids.flight_number.text = ""
        self.ids.date.text = "Select flight date"

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

        # Show current date
        ax.text(5, 9, today, ha='center', va='center', fontsize=12, fontweight='bold')

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
                helper_text: "Password does not match"

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

        MDLabel:
            size_hint: 1, .1

        MDTextField:
            id:uname
            hint_text: "Enter username"
            icon_left: "account"
            helper_text_mode: "on_error"
            helper_text: "Please enter username"

        MDTextField:
            id:passwd
            hint_text: "Enter password"
            icon_left: "lock"
            password: True
            helper_text_mode: "on_error"
            helper_text: "Must include min. 8 characters with min. 1 special character"


        MDTextField:
            id:passwd_confirm
            hint_text: "Confirm password"
            icon_left: "lock"
            password: True
            helper_text_mode: "on_error"
            helper_text: "Password does not match"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, None
            height: dp(40)
            MDCheckbox:
                id: show_pass
                size_hint_x: 0.1
                on_active: passwd.password = not self.active
                on_active: passwd_confirm.password = not self.active
                active: False
            MDLabel:
                text: "Show password"
                font_size: 25
                size_hint_x: 0.7
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
                on_release: root.try_logout()
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

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                id: time_button
                text: "Select flight time"
                md_bg_color: "#8dbcd6"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_press: root.show_time_picker()

            MDLabel:
                size_hint: 0.1, 1

            MDLabel:
                id: flight_schedule

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                id:date_button
                text: "Select flight date"
                text_pos_hint: {"center_x":1}
                md_bg_color: "#8dbcd6"
                size_hint: .5, .5
                pos_hint: {"center_x":.5, "center_y":.5}
                on_press: root.date()

            MDLabel:
                size_hint: 0.1, 1

            MDLabel:
                id: date

        MDBoxLayout:
            id:terminal
            size_hint: 1, .1
            pos_hint: {"center_x":.5}

            MDLabel:
                size_hint: 1,.5
                font_size: 30
                pos_hint: {"center_y":.5}
                text: "Terminals:"

            MDCheckbox:
                id: terminal1
                group: 'terminals' #this group is so that all the checkboxes are linked and only one can be selected
                size_hint: None, None
                size: dp(48), dp(48)
                active: True
                on_active: root.checkbox_click(self, self.active, "T1")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'Terminal 1'
                pos_hint: {"center_y":.5}
                font_size:30

            MDCheckbox:
                id: terminal2
                group: 'terminals'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click(self, self.active, "T2")
                pos_hint: {"center_y":.5}
            MDLabel:
                text: 'Terminal 2'
                pos_hint: {"center_y":.5}
                font_size:30
        MDLabel:
            size_hint: 1,.1
            font_size: 30
            pos_hint: {"center_y":.5}
            text: "Gates:"
        MDBoxLayout:
            id:gate_number
            size_hint: 1, .1
            pos_hint: {"center_x":.5}

            MDCheckbox:
                id:a1
                group: 'gates' #this group is so that all the checkboxes are linked and only one can be selected
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "A1")
                pos_hint: {"center_y":.5}
            MDLabel:
                text: 'A1'
                font_size:20
                pos_hint: {"center_y":.5}

            MDCheckbox:
                id: a2
                group: 'gates'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "A2")
                pos_hint: {"center_y":.5}
            MDLabel:
                text: 'A2'
                pos_hint: {"center_y":.5}
                font_size:16

            MDCheckbox:
                id: a3
                group: 'gates'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "A3")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'A3'
                pos_hint: {"center_y":.5}
                font_size:16

            MDCheckbox:
                id: a4
                group: 'gates'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "A4")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'A4'
                pos_hint: {"center_y":.5}
                font_size:16

            MDCheckbox:
                id: b1
                group: 'gates'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "B1")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'B1'
                pos_hint: {"center_y":.5}
                font_size:16

            MDCheckbox:
                id: b2
                group: 'gates'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "B2")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'B2'
                pos_hint: {"center_y":.5}
                font_size:16

            MDCheckbox:
                id: b3
                group: 'gates'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "B3")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'B3'
                pos_hint: {"center_y":.5}
                font_size:16

            MDCheckbox:
                id: b4
                group: 'gates'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_gate(self, self.active, "B4")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'B4'
                pos_hint: {"center_y":.5}
                font_size:16

        MDBoxLayout:
            id:status
            size_hint: 1, .1
            pos_hint: {"center_x":.5}

            MDLabel:
                size_hint: 1,.5
                font_size: 30
                pos_hint: {"center_y":.5}
                text: "Status:"

            MDCheckbox:
                id: ontime
                group: 'status' #this group is so that all the checkboxes are linked and only one can be selected
                size_hint: None, None
                size: dp(48), dp(48)
                active: True
                on_active: root.checkbox_click_status(self, self.active, "on time")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'on time'
                pos_hint: {"center_y":.5}
                font_size:30

            MDCheckbox:
                id: delayed
                group: 'status'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_status(self, self.active, "delayed")
                pos_hint: {"center_y":.5}

            MDLabel:
                text: 'delayed'
                pos_hint: {"center_y":.5}
                font_size:30

            MDCheckbox:
                id: cancelled
                group: 'status'
                size_hint: None, None
                size: dp(48), dp(48)
                on_active: root.checkbox_click_status(self, self.active, "cancelled")
                pos_hint: {"center_y":.5}
            MDLabel:
                text: 'cancelled'
                pos_hint: {"center_y":.5}
                font_size:30

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
                size_hint: .1, 1

            MDRaisedButton:
                id: addflight_clear
                text: "Clear"
                on_press: root.clear()
                size_hint: .2, .5
                md_bg_color: "#8dbcd6"

            MDLabel:
                size_hint: .1, 1

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
                helper_text: "Please enter flight number"

            MDRaisedButton:
                id:date
                text: "Select flight date"
                text_pos_hint: {"center_x":1}
                md_bg_color: "#8dbcd6"
                size_hint: .5, .05
                pos_hint: {"center_x":.5, "center_y":.5}
                on_press: root.date()

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
