# Magic 8 Ball with GUI
# theLabel = Label(root, text="McConnell's Magic 8 Ball")  # Label(goes where, what to write).
# theLabel.pack()  # Where it goes. Pack it in. Wherever it can go.
from tkinter import *
from random import *

root = Tk()
root.wm_title("McConnell's Magic 8 Ball!")
root.geometry("675x630")


def ask8ball():
    responses = ['It is certain', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.',
                 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
                 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
                 'Outlook not so good.', 'Very doubtful.']
    question = entry1.get()
    if not question.endswith('?'):
        errornoquestion()
    else:
        clear()
        answer = responses[randint(0, 20)]
        popupmsg(answer)


def clear():
    entry1.delete(0, END)


def errornoquestion():
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text='You must enter a question for the 8 ball to respond!')
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def popupmsg(msg):
    popup = Tk()
    popup.geometry("250x100")
    popup.wm_title("Magic 8 Ball Says...")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


image = PhotoImage(file="8ball.png")
label = Label(image=image)

topFrame = Frame(root)  # Invisible container in main window (root).
middleFrame = Frame(root)
bottomFrame = Frame(root)  # Usable frame for bottom

label1 = Label(topFrame, text="Ask the Magic 8 Ball your question:")
entry1 = Entry(topFrame, width=50)
button1 = Button(bottomFrame, text="Submit", fg='Black', command=ask8ball)
button2 = Button(bottomFrame, text='Close Magic 8 Ball.', fg='Red', command=root.destroy)

topFrame.pack()  # Place it somewhere, wherever it fits.
middleFrame.pack(side=BOTTOM)
bottomFrame.pack(side=BOTTOM)  # Place it somewhere, but on the bottom
label.pack()
label1.grid(row=0)
entry1.grid(row=0, column=1)
button1.grid(row=1)
button2.grid(row=1, column=3)

root.mainloop()
