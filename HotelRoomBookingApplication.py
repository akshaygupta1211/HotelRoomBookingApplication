from tkinter import *
from tkinter import ttk


def calculate(*args):
    pass


root = Tk()
root.title("Hotel Room Booking Application")

mainframe = ttk.Frame(root, padding="3 3 12 12")
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

ttk.Label(first_frame, text="Enter Customer Name").grid(column=1, row=1, sticky=W)

name_entry = ttk.Entry(first_frame, width=7, textvariable=customer_name)
name_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(first_frame, text="Enter Email Address").grid(column=1, row=2, sticky=W)

email_entry = ttk.Entry(first_frame, width=7, textvariable=customer_email)
email_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(first_frame, text="Enter Phone No").grid(column=1, row=3, sticky=W)

phone_entry = ttk.Entry(first_frame, width=7, textvariable=customer_phone)
phone_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(first_frame, text="Enter Residential Address").grid(column=1, row=4, sticky=W)

address_entry = ttk.Entry(first_frame, width=7, textvariable=customer_address)
address_entry.grid(column=2, row=4, sticky=(W, E))

room_type_list = {'AC_SINGLE', 'AC_DOUBLE', 'NON-AC_SINGLE', 'NON-AC_DOUBLE'}
room_type.set('---None---')

ttk.Label(first_frame, text="Select Room Type").grid(column=1, row=5, sticky=W)

room_type_entry = ttk.OptionMenu(first_frame, room_type, *room_type_list)
room_type_entry.grid(column=2, row=5, sticky=(W, E))

ttk.Button(first_frame, text="Submit", command=calculate).grid(column=3, row=6, sticky=W)

ttk.Label(second_frame, text="Room has been booked successfully").grid(column=1, row=1, sticky=(W,E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.bind('<Return>', calculate)

root.mainloop()
