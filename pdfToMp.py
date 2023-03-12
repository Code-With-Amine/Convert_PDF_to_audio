import PyPDF2,pyttsx3
from tkinter import *

win = Tk()
win.title('convert a pdf to audio')
win.maxsize(500,400)

def show_message():

    showText = Listbox(win,width = 40, height = 0)
    # I create a listbox without coordinates inorder to not be shown in the first place
    return showText
    

def Convert_to_audio():
    #i added the coordinates here to make the listbox visible but only if Convert_to_audio() been called
    message_box.place(x = 50 , y = 350)

    try:    
        pdfReader = PyPDF2.PdfReader(open(pdfNameEntry.get(), 'rb'))
        speaker = pyttsx3.init()

        for eachPage in range(len(pdfReader.pages)):
            text = pdfReader.pages[eachPage].extract_text()
            clean_text = text.strip().replace('\n',' ')

        speaker.save_to_file(clean_text, f'{nameOfTheAudioEntry.get()}.mp3')
        speaker.runAndWait()
        message_box.insert(0,f"{nameOfTheAudioEntry.get()} has been saved successfully in your folder")

    except:
        message_box.insert(0,"somthing went wrong please try again")

def Clear():
    pdfNameEntry.delete(0,END)
    nameOfTheAudioEntry.delete(0,END)
    try:
      message_box.delete(0,END)
      message_box.place_forget() # hide the listebox
    except:
        pass
    pdfNameEntry.focus()


def Quit():
    win.quit()


message_box = show_message()

Convert = Button(win,text="Convert to audio", bg='red',command=Convert_to_audio)
Convert.place(x = 20 , y = 30)

clear = Button(win,text="clear",command=Clear)
clear.place(x = 200 , y = 30)

Quit_app = Button(win,text="Quit",command=Quit)
Quit_app.place(x = 300 , y = 30)

label = Label(win,text="Enter the name of the PDF :")
label.place(x = 20 , y = 100)

pdfNameEntry = Entry(win)
pdfNameEntry.place(x = 200 , y = 100)

nameOfTheAudioLabel = Label(win,text="Entre the audio name")
nameOfTheAudioLabel.place(x = 20 , y = 200)

nameOfTheAudioEntry = Entry(win)
nameOfTheAudioEntry.place(x = 200 , y = 200)

mainloop()

