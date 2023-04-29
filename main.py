import customtkinter
import tkinter as tk
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Creates a new window
root = customtkinter.CTk()

# Sets the window title
root.title("Where should I throw away my trash?")

# Sets the window size
width = "500"
height = "570"
root.geometry(width + "x" + height)


#Creates the introFrame
introFrame = customtkinter.CTkFrame(root, width = 400, height = 400)

# Adds a label to the frame
label = customtkinter.CTkLabel(master=introFrame, text="WASTE MANAGEMENT APP", fg_color=('white' ,"green"), corner_radius=8, height=30, width=400, font=("Helvetica", 24) )
label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


userWaste = ""
currentFrame = introFrame


# BUTTON/ENTER EVENT
def originalButton():
    global entry
    userWaste = entry.get()
    
    # if statements to check for types of trash
    if "recycle" in userWaste.lower():
        recycle()
        currentFrame = recycleFrame
    elif "trash" in userWaste.lower():
        trash()
        currentFrame = trashFrame
    elif "compost" in userWaste.lower():
        compost()
        currentFrame = compostFrame
    else:
        notAvailable()
        currentFrame = notAvailableFrame

  
    

# ENTRY
entry = customtkinter.CTkEntry(master=introFrame, width=200, height=50, corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)



# BUTTON
button = customtkinter.CTkButton(master=introFrame, text="Classify My Waste", command=originalButton, width=120, 
                                 height=32, border_width=0, corner_radius=8)
button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
entry.bind('<Return>', lambda event: originalButton())

def returnButton(currentFrame):
    returnButton = customtkinter.CTkButton(master=currentFrame, text="Return to home", command=lambda: leaveButton(currentFrame), width=120,
                                           height=32, border_width=0, corner_radius=8)
    returnButton.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


#different frames depending on the type of waste

recycleFrame = customtkinter.CTkFrame(root, width = 400, height = 400)
recycleLabel = customtkinter.CTkLabel(recycleFrame, text="Recylce Info Goes Here")
recycleLabel.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
returnButton(recycleFrame)

trashFrame = customtkinter.CTkFrame(root, width = 400, height = 400)
trashLabel = customtkinter.CTkLabel(trashFrame, text="Trash Info Goes Here")
trashLabel.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
returnButton(trashFrame)

compostFrame = customtkinter.CTkFrame(root, width = 400, height = 400)
label = customtkinter.CTkLabel(master=compostFrame, text="COMPOST", fg_color=('white', "#099c2b"), corner_radius=8, height=60, width=180, font=("Helvetica", 24))
label.place(relx=0.28, rely=0.1, anchor=customtkinter.CENTER)
# Text box
textbox = customtkinter.CTkTextbox(master=compostFrame, height=40, width=120, corner_radius=8)
textbox.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER, relwidth=0.8, relheight=0.6)
# Insert text into the text box
textbox.insert(tk.END,"This item will be composted due to it being one of these options:\n 1. NewsPapers\n 2. Leaves/yard waste  \n 3. Veggie and fruit scraps \n 4. Egg shells (crushed)\n 5. Coffee grounds\n 6. Tissues, paper towels, napkins\n 7. Herbivore manure")
textbox.insert(tk.END, "\n\n More information will be found here:\n https://www.azdeq.gov/what-can-and-cant-i-compost-compost-guide")
textbox.configure(state="disabled", height= 120, width=500)
returnButton(compostFrame)

notAvailableFrame = customtkinter.CTkFrame(root, width = 400, height = 400)
notAvailableLabel = customtkinter.CTkLabel(notAvailableFrame, text="ur a retard just shove the trash up ur ass")
notAvailableLabel.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
returnButton(notAvailableFrame)


#different types of wastes and their pages

def recycle():
    introFrame.pack_forget()
    currentFrame = recycleFrame
    currentFrame.pack()
    
    
def trash():
    introFrame.pack_forget()
    currentFrame = trashFrame
    currentFrame.pack()

def compost():
    introFrame.pack_forget()
    currentFrame = compostFrame
    compostFrame.pack()

def notAvailable():
    introFrame.pack_forget()
    currentFrame = notAvailableFrame
    currentFrame.pack()
    
def leaveButton(currentFrame):
    currentFrame.pack_forget()
    introFrame.pack()




introFrame.pack()


# Run the main loop to start the app
root.mainloop()







introFrame.pack()


# Run the main loop to start the app
root.mainloop()

