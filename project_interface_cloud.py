from tkinter import *
from tkinter import messagebox as mbox
from tkinter import filedialog
from tkinter.simpledialog import askstring 
import project_logic_cloud as pl

root = Tk()

root.title('Encryption and Decryption')
root.geometry('700x650')
main_frame = Frame(root,width=650,height=130).grid(row=0,column=0)
login_frame = Frame(root,width=650,height=50)
file_frame = Frame(root,width=650,height=50)
folder_frame = Frame(root,width=650,height=50)
content_frame = Frame(root,width=650,height=50)
pattern_frame = Frame(root,width=650,height=140)
Level_frame = Frame(root,width=650,height=150)
src_frame = Frame(root,width=650,height=50)
dest_frame = Frame(root,width=650,height=50)

def submit_fun(name,fp,pat,lev):
  uname = name.get().strip()
  ch = radio.get()
  pat = pat.get()
  lev = lev.get() 
  # print("hello ")
  # print(f" name = {uname}\n ch = {ch}\n fp = {fp}\n pat = {pat}\n level = {lev}\n dir => {dir}  ")
  
  if uname == "":
    mbox.showwarning("warning","please fill the details")
  else:
    # print(f" name = {uname}\n ch = {ch}\n fp = {fp}\n pat = {pat}\n level = {lev}\n dir => {dir}  ")
    data = pl.main(uname,fp,pat,lev)
    # print(data)
    # file_name['text'] = " "
    mbox.showinfo("Success", "Message Encrypted Successfully!!..") 
    Switch_user()
    

def fun():
  # Label(text="pressed!!..")  
  mbox.showinfo("Hello", "Red Button clicked") 
  # messagebox.showwarning("warning","Warning")  
  # messagebox.showerror("error","Error")   
  # messagebox.askquestion("Confirm","Are you sure?")  
  # messagebox.askokcancel("Redirect","Redirecting you to www.javatpoint.com") 
  
def submit_decrypt(src):
  
  if src.strip() == "":
    mbox.showwarning("warning","please select the folder")
  else:
    # print(src,dest) 
    decrypt_list = pl.Display_Objects(2)
    # print(decrypt_list)
    if f"{src}_decrypt.txt" in decrypt_list:
      mbox.showwarning("warning","file already decrypted!!..")
    else:
      pl.Load_Data(src)
      mbox.showinfo("Success", "Message Decrypted Successfully!!..") 
  

def Switch_user():
  # print(e1['state'])
  e1.config(state= "normal")
  login['text'] = "save"
  # file_frame.grid_forget()
  # content_frame.grid_forget()
  button.grid_forget()
  Level_frame.grid_forget()
  pattern_frame.grid_forget()
  file_frame.grid_forget()
  folder_frame.grid_forget()
  file_name['text'] = ""
 
def Encrypt_fun():
  login_frame.grid(row=1,column=0)
  file_frame.grid(row=2,column=0)
  # pattern_frame.grid(row=3, column=0)
  button.grid_forget()
  file_frame.grid_forget()
  content_frame.grid_forget()
  folder_frame.grid_forget()
  src_frame.grid_forget()
  dest_frame.grid_forget()
  button_decrypt.grid_forget()
    
def closeFrames():
  # pattern_frame.grid_forget()
  Level_frame.grid_forget()
  file_frame.grid_forget()
  login_frame.grid_forget()
  pattern_frame.grid_forget()
  button.grid_forget()
  # button.grid(row=4, column=0)
  # content_frame.grid(row=1, column=0)
  src_frame.grid(row=2,column=0)
  # Access the Menu Widget using StringVar function
 
  list_val = pl.Display_Objects(1)
  if len(list_val) > 0:
    clicked.set(list_val[0])
    main_menu = OptionMenu(src_frame, clicked, *list_val )
    main_menu.place(x=20,y=0)
    sel_folder = Button(src_frame,text="select",font = ('courier', 13,"bold"),
                    # command= lambda: Selection_folder_src() )
                    command= lambda: button_decrypt.grid(row=5,column=0) )

    sel_folder.place(x=250,y=0)

  else:
    mbox.showwarning("warning","No data to decrypt!!")
  
def Login_User(name):
  name = name.get().strip()
  
  if name == "":
    mbox.showinfo("Message", "Enter the user name.") 
  else:
    # print(login['text'])
    data_list = pl.Display_Objects(1)
    if name in data_list:
       mbox.showwarning("warning","File already exit with the same name!!..")
    else:
      if login['text'] == "save":
        
        file_frame.grid(row=2,column=0)
        file_list = pl.Display_Objects(3)
        if len(file_list) > 0:
          input_file.set(file_list[0])
          file_menu = OptionMenu(file_frame, input_file, *file_list )
          file_menu.place(x=300,y=0)
          label_file = Label(file_frame,text="Select the input file : ",font = ('courier', 13,"bold"))
          label_file.place(x=20,y=0)
          # sel_file.place(x=350,y=0)
          # main_frame.grid(row=0, column=0)
          pattern_frame.grid(row=3, column=0)
          e1.config(state= "disabled")
          login['text'] = "Change"
        else:
          Top_Level_Win(1)
        
      elif login['text'] == "Change":
        ans = mbox.askyesno("Confirm","Are you sure ?")
        file_frame.grid_forget()
        if ans:
          Switch_user()
    
    
def Selection_file():
  root.filename = filedialog.askopenfilename()
  file_path = root.filename
  
  # fp = file_path[file_path.rindex("/"):]
  # file_name['text'] = file_path
  # pattern_frame.grid(row=3, column=0)  

def Selection_folder():
  root.foldername = filedialog.askdirectory()
  folder_path = root.foldername
  # fp = file_path[file_path.rindex("/"):]
  folder_name['text'] = folder_path
  button.grid(row=6,column=0)
  
def Selection_folder_src():
  # root.foldername = filedialog.askdirectory()
  # src_path = root.foldername
  # fp = file_path[file_path.rindex("/"):]
  # src_name['text'] = src_path
  # print(clicked.get())
  src_path =  clicked.get()
  # dest_frame.grid(row=3,column=0)
  button_decrypt.grid(row=5,column=0)


def Selection_folder_dest():
  root.foldername = filedialog.askdirectory()
  dest_path = root.foldername
  # fp = file_path[file_path.rindex("/"):]
  dest_name['text'] = dest_path
  button_decrypt.grid(row=5,column=0)
  
radio = IntVar() 
patterns = IntVar() 
level = IntVar() 
name = StringVar()
file_path = StringVar()
folder_path = StringVar()
src_path = StringVar()
dest_path = StringVar()
menu= StringVar()
clicked = StringVar()
input_file = StringVar()

# Upload/Delete/Download
def Top_Level_Win(ch):
  file_win = Toplevel()
  file_win.geometry("580x400")
  
  def Selection_file():
    root.filename = filedialog.askopenfilename()
    file_path = root.filename
    file_name['text'] = file_path
  
  def Selection_folder():
    root.foldername = filedialog.askdirectory()
    folder_path = root.foldername
    # fp = file_path[file_path.rindex("/"):]
    folder_name['text'] = folder_path
    # button.grid(row=6,column=0)
  
  def Selection_Delete_file(ch):
    
    sel_frame = Frame(file_win,width=550,height=50)
    error_frame = Frame(file_win,width=550,height=50)
    
    
    if ch == 1:
      list_val = pl.Display_Objects(3)
      if len(list_val) > 0:
        clicked.set(list_val[0])
        Label(sel_frame,width=30 , text="Select the Input file : "  ,
                      font = ('courier', 13)).place(x=0,y=0)
        # file_label.place(x=50,y=10)
        main_menu = OptionMenu(sel_frame, clicked, *list_val)
        main_menu.place(x=350,y=0)
        sel_frame.place(x=20,y=150)
        error_frame.place_forget()
      else:
        sel_frame.place_forget()
        error_label = Label(error_frame, text="No Data Available").place(x=0,y=0)
        error_frame.place(x=20,y=150)
        mbox.showwarning("warning","NO file to Delete!!..")
        
    elif ch == 2:
      list_val = pl.Display_Objects(1)
      if len(list_val) > 0:
        clicked.set(list_val[0])
        Label(sel_frame,width=30 , text="Select the Encrypted file : "  ,
                      font = ('courier', 13)).place(x=0,y=0)
        # file_label.place(x=50,y=10)
        main_menu = OptionMenu(sel_frame, clicked, *list_val)
        main_menu.place(x=350,y=0)
        error_frame.place_forget()
        sel_frame.place(x=20,y=150)
      else:
        sel_frame.place_forget()
        error_label = Label(error_frame, text="No Data Available").place(x=0,y=0)
        error_frame.place(x=20,y=150)
        mbox.showwarning("warning","NO file to Delete!!..")
        
    elif ch == 3:
      list_val = pl.Display_Objects(2)
      if len(list_val) > 0:
        clicked.set(list_val[0])
        Label(sel_frame,width=30 , text="Select the Decrypted file : "  ,
                      font = ('courier', 13)).place(x=0,y=0)
        # file_label.place(x=50,y=10)
        main_menu = OptionMenu(sel_frame, clicked, *list_val)
        error_frame.place_forget()
        main_menu.place(x=350,y=0) 
        sel_frame.place(x=20,y=150)
      else:
        sel_frame.place_forget()
        error_label = Label(error_frame, text="No Data Available").place(x=0,y=0)
        error_frame.place(x=350,y=150)
        mbox.showwarning("warning","NO file to Delete!!..")
  
  
  def Upload_file(file_path):
    if file_path.strip() == "":
      mbox.showwarning("warning","Please Select the file!!..")
    else:
      name = file_path[file_path.rindex("/")+1: ]
      if pl.Upload_to_bucket(f"input_files/{name}", file_path):
        mbox.showinfo("Success", "Uploaded Successfully!!..")
        file_name['text'] = ""
      else:
         mbox.showwarning("warning","some thing went wrong!!..")
  
  def Download_file(src_file,dest_path):
    if src_file == "" or dest_path == "":
      mbox.showwarning("warning","Please Select the fields!!..")
    else:
      pl.download_blob(f"Decrypted/{src_file}", f"{dest_path}/{src_file}.txt")
      mbox.showinfo("Success", "Downloaded Successfully!!..")
  
  def Delete_file(ch , f_name):
    
    if ch == 1:
     if  pl.delete_blob(f"input_files/{f_name}"):
       mbox.showinfo("Success", "Downloaded Successfully!!..")
     else:
       mbox.showwarning("warning","Something went Wrong!!..")
    elif ch == 2:
      file_list = pl.Display_Objects(1,f_name)
      # print(file_list)
      
      for item in file_list:
        flag = pl.delete_blob(f"Encrypted/{f_name}/{item}")
      
      if  flag:
        mbox.showinfo("Success", "Downloaded Successfully!!..")
      else:
        mbox.showwarning("warning","Something went Wrong!!..")

    elif ch == 3:
      if  pl.delete_blob(f"Decrypted/{f_name}"):
        mbox.showinfo("Success", "Deleted Successfully!!..")
      else:
        mbox.showwarning("warning","Something went Wrong!!..")
  
  if ch == 1:
    file_win.title("Upload Files")
    # pl.Upload_to_bucket("input_files/", input_data)
    
    file_label = Label(file_win,width=30 , text="Upload Input Files "  ,
                  font = ('courier', 18))
    file_label.place(x=50,y=10)

    file_name = Label(file_win,width=30 , text=file_path.get()  ,
                  font = ('courier', 12))
    file_name.place(x=20,y=100)

    sel_file = Button(file_win,text="Browse file",font = ('courier', 13,"bold"),
                      command= lambda: Selection_file() )
    sel_file.place(x=350,y=100)
    

    exit_button = Button(file_win, text="close",font = ('courier', 13,"bold"), command=file_win.destroy )
    submit_button = Button(file_win, text="Upload",font = ('courier', 13,"bold"), command=lambda: Upload_file(file_name['text']) )
    # upload_button.pack()
       
  elif ch == 2:
    file_win.title("Delete Files")
    
    file_label = Label(file_win,width=30 , text="Delete Files "  ,
                  font = ('courier', 18))
    file_label.place(x=70,y=10)

        # ==================  Selection Deletion ========================
    R1 = Radiobutton(file_win, text="Input Files", variable=radio, value=1, 
                    #  command=lambda: pattern_frame.place(x=20,y=150), 
                    command=lambda: Selection_Delete_file(1), 
                    font = ('courier', 15))  
    # R1.place(x=20,y=70) 
    R1.place(x=20,y=40) 
      
    R2 = Radiobutton(file_win, text="Encrypted File", variable=radio, value=2, 
                    #  command=lambda: pattern_frame.place_forget(),
                    command=lambda: Selection_Delete_file(2),
                    font = ('courier', 15))   
    # R2.place(x=20,y=100) 
    R2.place(x=20,y=70) 

    R3 = Radiobutton(file_win, text="Decrypted File", variable=radio, value=3, 
                    #  command=lambda: pattern_frame.place_forget(),
                    command=lambda: Selection_Delete_file(3),
                    font = ('courier', 15))   
    # R2.place(x=20,y=100) 
    R3.place(x=20,y=100) 
    
    


    exit_button = Button(file_win, text="close",font = ('courier', 13,"bold"), command=file_win.destroy )
    submit_button = Button(file_win, text="Delete",font = ('courier', 13,"bold"),command=lambda: Delete_file(radio.get() ,clicked.get()) )

  elif ch == 3:
    file_win.title("Download files")
    
    file_label = Label(file_win,width=30 , text="Download Decrypted Files "  ,
                  font = ('courier', 18))
    file_label.place(x=50,y=10)
    
    list_val = pl.Display_Objects(2)
    if len(list_val) > 0:
      clicked.set(list_val[0])
      Label(file_win,width=30 , text="Select the Decrypted file : "  ,
                    font = ('courier', 13)).place(x=20,y=70)
      # file_label.place(x=50,y=10)
      main_menu = OptionMenu(file_win, clicked, *list_val)
      main_menu.place(x=350,y=70)
      sel_folder = Button(file_win,text="select",font = ('courier', 13,"bold"),
                      # command= lambda: Selection_folder_src() )
                      command= lambda: button_decrypt.grid(row=5,column=0) )

      # sel_folder.place(x=250,y=70)
      
      folder_name = Label(file_win, width=30 , text=folder_path.get()  ,
                    font = ('courier', 12))
      folder_name.place(x=20,y=120)
      sel_folder = Button(file_win,text="Browse folder",font = ('courier', 13,"bold"),
                        command= lambda: Selection_folder() )
      sel_folder.place(x=350,y=120)

    else:
      mbox.showwarning("warning","No data to download!!")
      
      
    exit_button = Button(file_win, text="close",font = ('courier', 13,"bold"), command=file_win.destroy )
    submit_button = Button(file_win, text="Download",font = ('courier', 13,"bold"), 
                          command=lambda: Download_file( clicked.get() ,folder_name['text']) )
      
  exit_button.place(x=200,y=200)
  submit_button.place(x=300,y=200)
   

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Upload file", command= lambda: Top_Level_Win(1))
filemenu.add_command(label="Delete file", command=lambda: Top_Level_Win(2))
filemenu.add_command(label="Download file", command=lambda: Top_Level_Win(3))


filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
  
# ===================== login Info ============================
nameLabel = Label(login_frame,text = "Name :",font = ('courier', 15, 'bold'))
nameLabel.place(x=20,y=0)
e1 = Entry(login_frame,width=30, textvariable=name ,font = ('courier', 15, 'bold'))
e1.place(x=130,y=0)
login = Button(login_frame,text="save", font = ('courier', 12, 'bold'), command= lambda: Login_User(name) )
login.place(x=510, y=0)


# ================== Operation Selection ========================
R1 = Radiobutton(main_frame, text="Encryption", variable=radio, value=1, 
                #  command=lambda: pattern_frame.place(x=20,y=150), 
                 command=lambda: Encrypt_fun(), 
                 font = ('courier', 15))  
# R1.place(x=20,y=70) 
R1.place(x=20,y=20) 
  
R2 = Radiobutton(main_frame, text="Decryption", variable=radio, value=2, 
                #  command=lambda: pattern_frame.place_forget(),
                 command=lambda: closeFrames(),
                 font = ('courier', 15))   
# R2.place(x=20,y=100) 
R2.place(x=20,y=60) 


# ================== Select File ==============================
# file_name = Label(file_frame,width=30 , text=file_path.get()  ,
#                   font = ('courier', 12))
# file_name.place(x=20,y=0)
# print(file_path.get())
# sel_file = Button(file_frame,text="Browse file",font = ('courier', 13,"bold"),
#                   command= lambda: Selection_file() )
# sel_file.place(x=350,y=0)


# ================== Select Folder ==============================
folder_name = Label(folder_frame, width=30 , text=folder_path.get()  ,
                  font = ('courier', 12))
folder_name.place(x=20,y=0)
sel_folder = Button(folder_frame,text="Browse folder",font = ('courier', 13,"bold"),
                  command= lambda: Selection_folder() )
sel_folder.place(x=350,y=0)

# ================== Select source Folder ==============================
# src_name = Label(src_frame, width=30 , text="Select the source folder"  ,
#                   font = ('courier', 12))
# src_name.place(x=20,y=0)
# sel_folder = Button(src_frame,text="source folder",font = ('courier', 13,"bold"),
#                   command= lambda: Selection_folder_src() )

# # Access the Menu Widget using StringVar function
# clicked = StringVar()
# list_val = pl.Display_Objects()
# if len(list_val) > 0:
#   clicked.set(list_val[0])
  # main_menu = OptionMenu(src_frame, clicked, *list_val )
#   main_menu.place(x=20,y=0)
#   sel_folder = Button(src_frame,text="select",font = ('courier', 13,"bold"),
#                   command= lambda: Selection_folder_src() )

#   sel_folder.place(x=250,y=0)

# else:
#   mbox.showwarning("warning","No data to decrypt!!")


# Create an instance of Menu in the frame
# main_menu = OptionMenu(src_frame, clicked, *list_val )
# main_menu = OptionMenu(src_frame, clicked, *list_val )



# ================== Select destination Folder ==============================
dest_name = Label(dest_frame, width=30 , text=dest_path.get()  ,
                  font = ('courier', 12))
dest_name.place(x=20,y=0)
sel_folder = Button(dest_frame,text="destination folder",font = ('courier', 13,"bold"),
                  command= lambda: Selection_folder_dest() )
sel_folder.place(x=350,y=0)


# ================== Select Content to Decrypt ==============================
# en_msg = ["message1", "data2", "data 3"]
# menu.set(en_msg[0])
# drop = OptionMenu(content_frame, menu,*en_msg)
# drop.place(x=20,y=0) 

# ================== Patterns Selection ========================
msg_pat = Label( pattern_frame, text = "Select the Pattern", font = ('courier', 15))
msg_pat.place(x=20,y=0) 
P1 = Radiobutton(pattern_frame, text="Line Pattern", variable=patterns, value=1,
                 command=lambda: Level_frame.grid(row=4,column=0), 
                 font = ('courier', 15))  
# P1.place(x=20,y=30) 
P2 = Radiobutton(pattern_frame, text="Pyramid Pattern", variable=patterns, value=2,
                 command=lambda: Level_frame.grid(row=4,column=0), 
                 font = ('courier', 15))  
# P2.place(x=20,y=65) 
P2.place(x=20,y=30) 
  
P3 = Radiobutton(pattern_frame, text="QR Pattern", variable=patterns, value=3, 
                 command=lambda: Level_frame.grid(row=4,column=0),
                 font = ('courier', 15))   
# P3.place(x=20,y=95)
P3.place(x=20,y=60)


# ================== Level Selection ========================
msg_level = Label(Level_frame, text = "Select the Complexity", font = ('courier', 15))
msg_level.place(x=20,y=0) 
L1 = Radiobutton(Level_frame, text="Low", variable=level, value=3, 
                #  command=lambda: folder_frame.grid(row=5, column=0), 
                 command=lambda: button.grid(row=6,column=0), 
                 font = ('courier', 15))   
L1.place(x=20,y=30) 
  
L2 = Radiobutton(Level_frame, text="Medium", variable=level, value=5,
                #  command=lambda: folder_frame.grid(row=5, column=0),
                 command=lambda: button.grid(row=6,column=0),
                 font = ('courier', 15))   
L2.place(x=20,y=60)

L2 = Radiobutton(Level_frame, text="High", variable=level, value=7,
                #  command=lambda:  folder_frame.grid(row=5,column=0),
                 command=lambda:  button.grid(row=6,column=0),
                 font = ('courier', 15))   
L2.place(x=20,y=90)
  
# encryption submit button
button = Button(root, text='submit', width=20,font = ('courier', 15,'bold'), 
                command= lambda: submit_fun(name,input_file.get(),patterns,level) )

# decryption submit button
button_decrypt = Button(root, text='submit', width=20,font = ('courier', 15,'bold'), 
                command= lambda: submit_decrypt(clicked.get()) )
                # command= lambda: submit_decrypt(src_path) )

root.mainloop()