#importing library
from tkinter import *

window = Tk()

#Declaring Window Title
window.title('Registration form')

#Declaring Window size
window.geometry("1080x1080")

#Declaring Window Color
window.configure(background="red")

#Below fields are declared
Heading = Label(window, text="Registration form", width=15, bg='black', fg='white', font=("bold", 20)).place(x=375, y=60)

First_Name = Label(window, text="First Name", width=10, font=("bold", 10)).place(x=70, y=130)
First_Name1 = Entry(window).place(x=240, y=130)

Last_Name = Label(window, text="Last Name", width=10, font=("bold", 10)).place(x=70, y=180)
Last_Name1 = Entry(window).place(x=240, y=180)


#Radio button
Gender = Label(window, text="Gender", width=10, font=("bold", 10)).place(x=70, y=230)
# the variable 'var' mentioned here holds Integer Value, by deault 0
v = IntVar()
# this creates 'Radio button' widget and uses place() method
Radiobutton(window, text="Male", padx=5, variable=v, value=1).place(x=235, y=230)
Radiobutton(window, text="Female", padx=20, variable=v, value=2).place(x=290, y=230)


Job_title = Label(window, text="Job Title", width=10, font=("bold", 10)).place(x=70, y=280)
Job_title = Entry(window).place(x=240, y=280)

Department = Label(window, text="Department", width=10, font=("bold", 10)).place(x=70, y=330)
Department1 = Entry(window).place(x=240, y=330)

Department_id = Label(window, text="Department id", width=10, font=("bold", 10)).place(x=70, y=380)
Department_id1 = Entry(window).place(x=240, y=380)

Salary = Label(window, text="Salary", width=10, font=("bold", 10)).place(x=70, y=430)
Salary = Entry(window).place(x=240, y=430)

Email = Label(window, text="E-mail", width=10, font=("bold", 10)).place(x=70, y=480)
Email1 = Entry(window).place(x=240, y=480)

Contact_number = Label(window, text="Phone Number", width=10, font=("bold", 10)).place(x=70, y=530)
Contact_number1 = Entry(window).place(x=240, y=530)


#Dropdown button
Country = Label(window, text="Country", width=10, font=("bold", 10)).place(x=70, y=580)
list_of_country = ['India', 'US', 'UK', 'Germany', 'Austria']

c = StringVar()
droplist = OptionMenu(window, c, *list_of_country)
droplist.config(width=20)
c.set('Select your Country')
droplist.place(x=230, y=580)


#Submit button
Button(window, text='Submit', width=25, bg="black", fg='white').place(x=100, y=630)

window.mainloop()
