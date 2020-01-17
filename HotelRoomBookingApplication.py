from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re


def print_customer_details(*args):
    if not re.match("[A-Z][a-z\\sA-Z]{,15}", customer_name.get()):
        messagebox.showerror(message='Please enter a valid name', icon='error', title='Error')
        name_entry.focus()
        return
    elif not re.match("[a-zA-Z][a-zA-Z0-9_.]*@[a-z]+([.][a-zA-Z]+)", customer_email.get()):
        messagebox.showerror(message='Please enter a valid email id', icon='error', title='Error')
        email_entry.focus()
        return
    elif not re.match("[6789][0-9]{9}", customer_phone.get()):
        messagebox.showerror(message='Please enter a valid mobile number', icon='error', title='Error')
        phone_entry.focus()
        return
    elif not re.match("[A-Za-z0-9\\s]{1,25}", customer_address.get()):
        messagebox.showerror(message='Please enter a valid address', icon='error', title='Error')
        address_entry.focus()
        return
    print("CustomerDetails [customer_name=", customer_name.get(), "email=", customer_email.get(), "customer_address=",
          customer_address.get(), "mobileNo=", customer_phone.get(), "roomType=", room_type.get(), "]")
    success_message = "Room has been booked successfully"
    message.set(success_message)


root = Tk()
root.title("Hotel Room Booking Application")

s = ttk.Style()
s.theme_use('alt')

mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

first_frame = ttk.Frame(mainframe)
first_frame.grid(column=0, row=0, sticky=(N, W, E, S))
second_frame = ttk.Frame(mainframe)
second_frame.grid(column=0, row=1, sticky=(N, W, E, S))

first_frame['borderwidth'] = 3
first_frame['relief'] = 'sunken'

second_frame['borderwidth'] = 3
second_frame['relief'] = 'sunken'

customer_name = StringVar()
customer_email = StringVar()
customer_phone = StringVar()
customer_address = StringVar()
room_type = StringVar()
message = StringVar()

ttk.Label(first_frame, text="Enter Customer Name").grid(column=1, row=1, sticky=W)

name_entry = ttk.Entry(first_frame, width=25, textvariable=customer_name)
name_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(first_frame, text="Enter Email Address").grid(column=1, row=2, sticky=W)

email_entry = ttk.Entry(first_frame, width=25, textvariable=customer_email)
email_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(first_frame, text="Enter Mobile No").grid(column=1, row=3, sticky=W)

phone_entry = ttk.Entry(first_frame, width=25, textvariable=customer_phone)
phone_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(first_frame, text="Enter Residential Address").grid(column=1, row=4, sticky=W)

address_entry = ttk.Entry(first_frame, width=25, textvariable=customer_address)
address_entry.grid(column=2, row=4, sticky=(W, E))

room_type_list = {'AC_SINGLE', 'AC_DOUBLE', 'NON-AC_SINGLE', 'NON-AC_DOUBLE'}
room_type.set('---None---')

ttk.Label(first_frame, text="Select Room Type").grid(column=1, row=5, sticky=W)

room_type_entry = ttk.OptionMenu(first_frame, room_type, *room_type_list)
room_type_entry.grid(column=2, row=5, sticky=(W, E))

ttk.Button(first_frame, text="Submit", command=print_customer_details).grid(column=3, row=6, sticky=W)

message.set('Welcome to Hotel Room Booking Application')
ttk.Label(second_frame, textvariable=message).grid(column=1, row=1, sticky=(N, W, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

name_entry.focus()
root.bind('<Return>', print_customer_details)

root.mainloop()
