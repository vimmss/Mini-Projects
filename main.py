from tkinter import*
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

root = Tk()
#For the title
root.title("LEPLA :-: PDF Viwer")

#for the icon change
root.iconbitmap('D:/Icons/bush.ico')

#windows geometry 
root.geometry('630x700+400+100')

def browsefiles():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Your PDF File", filetypes=(("PDF File",".pdf"),
                                                  ("PDF File",".PDF"),
                                                  ("All File","txt")))
    v1=pdf.ShowPdf()
    v2=v1.pdf_view(root, pdf_location=open(filename,"r"), width=77, height=100)
    v2.pack(pady=(0,0))

button=Button(root, text="PDF Viwer",command=browsefiles, width=40, bd=4)
button.pack()

# for background colour 
root.configure(bg='#E7D7CB')
root.mainloop()
