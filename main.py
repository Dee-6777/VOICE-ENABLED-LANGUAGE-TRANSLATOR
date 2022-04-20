from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
import speech_recognition as sr
import pyttsx3

root = Tk()

root.title("My language translator")

root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="lightblue")


def speak_now():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('speak now')
            audio = r.listen(source)
            try:
                text3 = r.recognize_google(audio, language="en-IN")
            except:
                pass
            return text3


def SpeechToText():
    combo1 = ttk.Combobox(root, values=languageV, font="Times 20 italic bold", state="r")
    combo1.place(x=110, y=20)
    combo1.set("english")

    label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=12, bd=5, relief=GROOVE)
    label1.place(x=112, y=60)
    f = Frame(root, bg="Black", bd=5)
    f.place(x=112, y=118, width=300, height=210)
    text2 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
    text2.place(x=0, y=0, width=430, height=200)
    recordbutton = Button(f, text='Record', bg='Sienna', command=lambda: text2.insert(END, speak_now()))
    recordbutton.place(x=120, y=50)

    translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                       width=10, height=2, bg="black", fg="white", command=translate_now_for_speech)
    translate.place(x=485, y=290)

def translate_now_for_speech():
    # delete any previous translations
    text2.delete(1.0, END)
    global from_language_key, to_language_key
    try:
        # get the languages from dictionary keys
        # get the from_language_key
        for key, value in languages.items():
            if value == combo1.get():
                from_language_key = key

        # get the To Language Key
        for key, value in languages.items():
            if value == combo2.get():
                to_language_key = key

        # turn original text into a textblob
        words = textblob.TextBlob(speak_now().get(1.0, END))

        # translate text
        words = words.translate(from_lang = from_language_key,to = to_language_key)

        # output translated text to screen
        text2.insert(1.0, words)

        # initial the speech engine
        engine = pyttsx3.init()

        # pass text to speech engine
        engine.say(text2.get(1.0, END))

        # run the engine
        engine.runAndWait()

    except Exception as e:
        messagebox.showerror("My language translator", e)


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_now():
    # delete any previous translations
    text2.delete(1.0, END)
    global from_language_key, to_language_key
    try:
        # get the languages from dictionary keys
        # get the from_language_key
        for key, value in languages.items():
            if value == combo1.get():
                from_language_key = key

        # get the To Language Key
        for key, value in languages.items():
            if value == combo2.get():
                to_language_key = key

        # turn original text into a textblob
        words = textblob.TextBlob(text1.get(1.0, END))

        # translate text
        words = words.translate(from_lang = from_language_key,to = to_language_key)

        # output translated text to screen
        text2.insert(1.0, words)

        # initial the speech engine
        engine = pyttsx3.init()

        # pass text to speech engine
        engine.say(text2.get(1.0, END))

        # run the engine
        engine.runAndWait()

    except Exception as e:
        messagebox.showerror("My language translator", e)




# grab language list from GoogleTrans
languages = googletrans.LANGUAGES
language_list = list(languages.values())  # converting the languages dictionary into list
print(language_list)


def clear():
    # Clear the text boxes
    text1.delete(1.0, END)
    text2.delete(1.0, END)


bg = PhotoImage(file="20309261.png")

bg_label = Label(image=bg)
bg_label.pack()

image_icon = PhotoImage(file="7060297.png")
root.iconphoto(False, image_icon)

# arrow_image = PhotoImage(file="arrow.png")
# image_label = Label(root, image=arrow_image, width=150)
# image_label.place(x=470, y=50)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Times 20 italic bold", state="r")
combo1.place(x=110, y=20)
combo1.set("english")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=12, bd=5, relief=GROOVE)
label1.place(x=112, y=60)

combo2 = ttk.Combobox(root, values=languageV, font="Times 20 italic bold", state="r")
combo2.place(x=670, y=20)
combo2.set("select language")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=12, bd=5, relief=GROOVE)
label2.place(x=672, y=60)

# 1st frame
f = Frame(root, bg="Black", bd=5)
f.place(x=112, y=118, width=300, height=210)

# original text
text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# 2nd frame
f = Frame(root, bg="White", bd=5)
f.place(x=672, y=118, width=300, height=210)

# translated text
text2 = Text(f, font="Robote 20", bg="black", relief=GROOVE, wrap=WORD, fg="white")
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text1.configure(yscrollcommand=scrollbar2.set)

# translate button

translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                   width=10, height=2, bg="black", fg="white", command=translate_now)
translate.place(x=485, y=290)

# speak button

speak = Button(root, text="Speak", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                   width=10, height=1, bg="black", fg="white", command=SpeechToText)
speak.place(x=485, y=360)

label_change()
root.mainloop()
