from Tkinter import *
import pdb
from tkFileDialog import askopenfilename
import os

# Settings
log=savVid=sourceVid=sourceCam=0

# Frame
root = Tk()
root.minsize(width=400, height=200)

# Choose video source
Label(root,text="Choose Video Source",padx = 20).pack(anchor=W)
v = IntVar()
Radiobutton(root,text="Video File",padx = 20,variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="Webcam",padx = 20,variable=v,value=2).pack(anchor=W)

# Draw separator
w = Canvas(root, width=400, height=10)
w.pack()
w.create_line(20, 10, 380, 10)

#LogFIle  & save video Check
Label(root,text="Options",padx = 20).pack(anchor=W)
chk = IntVar()
Checkbutton(root, text="Generate Log",padx=20, variable=chk).pack(anchor=W)

#Save video Check
sv = IntVar()
Checkbutton(root, text="Save Video",padx=20, variable=sv).pack(anchor=W)

#make graph
gg = IntVar()
Checkbutton(root, text="Generate Graph",padx=20, variable=gg).pack(anchor=W)

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    return inputValue

textBox=Text(root,padx=20, height=1, width=10)
textBox.pack(anchor=W)

# Button
def detect():
    srcVidPath ="None"
    ggraph = 0

    if gg.get():
        ggraph =1
    else:
        ggraph=0

    if sv.get():
        savVid=1
    else:
        savVid=0

    if chk.get():
        log=1
    else:
        log=0

    if v.get() ==1:
        sourceVid = 1
        sourceCam=0

        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        srcVidPath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(srcVidPath)

    elif v.get() ==2:
        sourceVid = 0
        sourceCam=1

    print "file = "+srcVidPath

    global command

    command= "python peepCount.py "

    if log ==1:
        command += " --generateLog "

    if savVid==1:
        outputFile = retrieve_input()
        command += " --saveOutput --output "+outputFile+".avi "

    if ggraph ==1:
        command += "--makeGraph "

    if sourceVid==1 and sourceCam==0:
        command += " --video "+srcVidPath+" "

    elif sourceVid==0 and sourceCam==1:
        command += " --webcam "

        print command


b = Button(root, text="Configure", padx=20, command=detect)
b.pack()

def g():
    print command

    os.system(command)

b2 = Button(root, text="Go!", padx=20, command=g)
b2.pack()


mainloop()
