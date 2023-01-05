from tkinter import Tk, Canvas, Button, simpledialog

from datetime import datetime, date

# Get today's Date
today = date.today()

vertical_space = 100

fname = ""

# initialize the UI board
root = Tk()
c = Canvas(root, width = 1000, height = 800, bg = 'black')
c.pack()
c.create_text(100, 50, anchor='w', fill = 'orange', font = 'Arial 28 bold underline', text = 'My Countdown Calendar')

# Get the lists of important dates from the file
def get_events():
    global fname
    list_events = []
    fname = simpledialog.askstring("Path", "Enter the path of the file you want to load: ")
    file = open(fname)
    lines = file.readlines()
    file.close()
    lines = [l.strip() for l in lines]
    file_data = []
    for line in lines:
        # split each line by data and digest
        current_event = line.split(',')
        date = current_event[1]
        event_date = datetime.strptime(date, '%d/%m/%y').date()
        # Calculate the difference and add it in if the event difference is postive
        diff = difference(event_date, today)
        if int(diff) > 0:
            # adding data line to selected data file
            file_data.append(line+"\n")
            # add event to selected event list
            current_event[1] = event_date
            list_events.append(current_event)
    # overwrite the data file
    with open(fname, 'w') as filename:
        filename.writelines(file_data)
    return list_events

def add_event():
    global vertical_space
    # adding the data into the file
    f = open("event.txt", "a")
    new_event = simpledialog.askstring("event", "Enter an event: ")
    day = simpledialog.askstring("date", "Enter the date of an event: ")
    new_date = [new_event, ",", day, "\n"]
    f.writelines(new_date)
    f.close()
    # shwoing the data on the canvas
    d = difference(datetime.strptime(day, '%d/%m/%y').date(), today)
    f = "It is {} days until {} ".format(d, new_event)
    c.create_text(100, vertical_space, anchor = 'w', fill = 'lightblue', font = 'Arial 28 bold', text=f)
    vertical_space += 30
    
def clear():
    openfile = open("event.txt", "r+")
    openfile.truncate(0)
    openfile.close()
    c.delete("all")
    c.create_text(100, 50, anchor='w', fill = 'orange', font = 'Arial 28 bold underline', text = 'My Countdown Calendar')
button2 = Button(root, text = "Remove all events", command = clear)
button2.pack()

# Calculate the number of days until the event
def difference(date1, date2):
    time_between = str(date1 - date2)
    print(time_between)
    number_of_days = time_between.split()
    print(number_of_days)
    return number_of_days[0]


events = get_events()




button1 = Button(root, text = "Add Event", command=add_event)
button1.pack()

# Calculate and Display the result
for event in events:
    name = event[0]
    d = difference(event[1], today)
    f = "It is {} days until {} ".format(d, name)
    c.create_text(100, vertical_space, anchor = 'w', fill = 'lightblue', font = 'Arial 28 bold', text=f)
    vertical_space += 30
root.mainloop()