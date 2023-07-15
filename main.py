# Base code found at: https://github.com/codefirstio/tkinter-data-entry.git

from tkinter import *
from tkinter import ttk
import datetime

# coursework information form
window = Tk()
window.title("Coursework Information Form")
frame = Frame(window)
frame.pack()

# Assignment Information
assignment_info_frame = LabelFrame(frame)
assignment_info_frame.grid(row=0, column=0, padx=10, pady=10)

    # Name
title_label = Label(assignment_info_frame, text="Title:")
title_label.grid(row=0, column=0, sticky="e")
title_entry = Entry(assignment_info_frame)
title_entry.grid(row=0, column=1)

    # Type (homework, quiz, exam, project, etc.)
type_label = Label(assignment_info_frame, text="Type:")
type_label.grid(row=1, column=0, sticky="e")
type_combobox = ttk.Combobox(assignment_info_frame, values=["Homework", "Quiz", "Exam", "Project", "Other"])
type_combobox.grid(row=1, column=1)

    # Course
course_label = Label(assignment_info_frame, text="Course:")
course_label.grid(row=2, column=0, sticky="e")
course_combobox = ttk.Combobox(assignment_info_frame)
course_combobox.grid(row=2, column=1)

    # Delivery
delivery_label = Label(assignment_info_frame, text="Delivery:")
delivery_label.grid(row=3, column=0, sticky="e")
delivery_combobox = ttk.Combobox(assignment_info_frame, values=["In Class", "Online", "Other"])
delivery_combobox.grid(row=3, column=1)

    # Additional Notes
notes_label = Label(assignment_info_frame, text="Additional Notes:")
notes_label.grid(row=4, column=0, sticky="e")
notes_entry = Entry(assignment_info_frame)
notes_entry.grid(row=4, column=1)

    # Due Date
due_date_frame = LabelFrame(frame)
due_date_frame.grid(row=0, column=1, padx=10, pady=10)

due_date_label = Label(due_date_frame, text="Due Date:")
due_date_label.grid(row=5, column=0)
        # Month
month_combobox = ttk.Combobox(due_date_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], width=11)
month_combobox.grid(row=5, column=1)
        # Day
day_spinbox = Spinbox(due_date_frame, from_=1, to=31, width=3)
day_spinbox.grid(row=5, column=2)
        # Year
year_spinbox = Spinbox(due_date_frame, from_=datetime.date.today().year, to=datetime.date.today().year+10, width=5)
year_spinbox.grid(row=5, column=3)

    # Due Time
due_time_label = Label(due_date_frame, text="Due Time:")
due_time_label.grid(row=6, column=0)
        # Hour
hour_spinbox = Spinbox(due_date_frame, from_=1, to=12, width=3)
hour_spinbox.grid(row=6, column=1)
        # Minute
minute_spinbox = Spinbox(due_date_frame, from_=0, to=59, width=3)
minute_spinbox.grid(row=6, column=2)
        # AM/PM
am_pm_combobox = ttk.Combobox(due_date_frame, values=["AM", "PM"], width=3)
am_pm_combobox.grid(row=6, column=3)

window.mainloop()