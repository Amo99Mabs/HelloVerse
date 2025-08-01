import tkinter

window = tkinter.Tk()
window.title("GUI")
window.geometry("640x420")

hello_message = tkinter.Message(window, text="Amo the Software Engineer")
hello_message.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
window.mainloop()