import os
import re
import tkinter
import fuzzywuzzy
import tkintertable

from os import walk
from tkinter import *
from fuzzywuzzy import fuzz
from tkintertable import TableCanvas, TableModel

#using fuzzywuzzy for text matching
def getselectedmovie():
    basepath = '/Volumes/SeagateBackupPlusDrive/Anay/Entertainment/Movies/HW/'
    movies = getallmovies()
    subtitles, sub_path  = getSubtitles()
    ratios = []
    for m in movies:
        ratio = fuzz.ratio(e1.get(), m)
        ratios.append(ratio)
    movie = movies[ratios.index(max(ratios))]
    # subtitle = subtitles[ratios.index(max(ratios))]
    print(movie)
    # print(subtitle)
    moviepath = os.path.join(basepath, movie).replace(" ", "\\ ")
    #takes care of spaces

    os.system('open ' + moviepath)
    os.system('open ' + sub_path)




# input1 = input("What movie would you like to watch? ")
# main('I would like to watch Interstellar')

def getallmovies():
    path = '/Volumes/SeagateBackupPlusDrive/Anay/Entertainment/Movies/HW/'
    movies = []
    folders = []
    for (dirpath, dirnames, filenames) in walk(path):
        movies.extend(filenames)
        # folders.extend(dirnames)
        # paths.extend(dirpath)
        break
    # movies = os.system('open /Volumes/SeagateBackupPlusDrive/Anay/Entertainment/Movies/HW/')

    #MAKE THIS RECURSIVE
    # morefolders = []
    # for f in folders:
    #     path = temp+f
    #     for (dirpath, dirnames, filenames) in walk(path):
    #         # print(dirpath)
    #         movies.extend(filenames)
    #         morefolders.extend(dirnames)
    #
    # if (len(morefolders) > 0):
    #     evenmorefolders = []
    #     for m in morefolders:
    #         path = path+f+m
    #         for (dirpath, dirnames, filenames) in walk(path):
    #             movies.extend(filenames)
    #             evenmorefolders.extend(dirnames)
    print(movies)
    movies.sort()
    return movies

def getSubtitles():
    path = '/Volumes/SeagateBackupPlusDrive/Anay/Entertainment/Movies/HW/SUBTITLES'
    subtitles = []
    folders = []
    for (dirpath, dirnames, filenames) in walk(path):
        subtitles.extend(filenames)
        # folders.extend(dirnames)
        # paths.extend(dirpath)
        break
    return subtitles, path
def centerwindow(root):
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

def callback(self):
    getselectedmovie()
def idk_callback():
    movies = getallmovies()
    # tframe = Frame(secondmaster)
    # tframe.grid(row=4, column=0)
    # model = TableModel()
    # table = TableCanvas(tframe, model=movies)
    label2 = Label(master, text = 'Figure it out and then come back')
    label2.grid(row = 4, column = 0)


master = Tk()
master.title('Main Window')
master.geometry("300x300")

centerwindow(master)
# master.configure(background='black')

#set label
label = Label(master, text = 'What movie would you like to watch today?')
label.grid(row = 0, column = 0)
#set entry field (text field)
e1 = Entry(master)
e1.grid(row=1, column=0)
#set enter button

b1 = Button(master, text = 'Enter', command = callback)
b1.grid(row = 2, column = 0)
master.bind('<Return>', callback)   #enables user to hit enter button
b2 = Button(master, text = 'I don\'t know', command = idk_callback)
b2.grid(row = 3, column = 0)
# e2.grid(row=1, column=1)

master.mainloop()

# to make everything black => <widget>.configure(background='black')
