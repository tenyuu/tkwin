import tkinter

root = tkinter.Tk()
root.title("practice!")
root.geometry("500x500")
root.resizable(0,0)

frame_1 = tkinter.LabelFrame(root,text="テキストフレームです")
frame_2 = tkinter.Frame(root)
frame_1.pack(padx=10,pady=10)
frame_2.pack(padx=10,pady=(0,10))
             
radio_1 = tkinter.Radiobutton(frame_1,text="1を出力します")
radio_2 = tkinter.Radiobutton(frame_1,text="2を出力します")
radio_1.grid(row=0,column=0,padx=10,pady=10)
radio_2.grid(row=0,column=1,padx=10,pady=10)


root.mainloop()