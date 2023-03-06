from database_handler import database_worker
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
