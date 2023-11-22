from tkinter import*
import tkinter.messagebox

root=Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElements:
    def __init___(self):
        print("This is create element class.")
        
    def createNewElement(self):
        label=Label(root,text="A new label is being created using class.",fg="red")
        label.pack()
        class_btn=Button(root, text="Button", command=self.message)
        class_btn.pack(padx=20,pady=10)
        
    def message(self):
        messagebox.showinfo("showinfo","You clicked the button created using the class")
        
obj_of_CreateElements=CreateElements()

btn=Button(root, text="click to create label and button element", command=obj_of_CreateElements.createNewElement)
btn.pack(padx=20, pady=10)

root.mainloop()
