from tkinter import *
def buttonclick1(key, data):
        alphabet="abcdefghijklmnopqrstuvwxyz"
        print("key is ", key)
        global ans_enc
        ans_enc=""
        for i in data:
          if i in alphabet:
            pos=alphabet.find(i)
            newPos=(int(pos)+int(key))%26
            newChar=alphabet[newPos]
            ans_enc+=newChar
          else:
            ans_enc+=i
        outputis1=Label(frame1, text=ans_enc, bg='yellow')         #label of enter data 1
        outputis1.place(x=134, y=200)


def buttonclick2(key, data):
    global ans_dec
    ans_dec=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in data:
        if i in alphabet:
            pos=alphabet.find(i)
            newPos=(int(pos)-int(key))%26
            newChar=alphabet[newPos]
            ans_dec+=newChar
        else:
            ans_dec+=i
    outputis2=Label(frame2, text=ans_dec, bg='cyan')         #label of enter data 2
    outputis2.place(x=134, y=200)



ans_enc=""
ans_dec=""
        
root1=Tk()                                                              #window1
root2=Tk()                                                              #window2                                            

root1.geometry("500x400")
root2.geometry("500x400")

root1.title("Encryption")
root2.title("Decryption")

frame1=Frame(root1, height=400, width=500, bg='yellow', cursor='cross')
frame2=Frame(root2, height=400, width=500, bg='cyan', cursor='cross')

frame1.propagate(0)
frame2.propagate(0)

abc1=Label(frame1, text="Encryption", fg="red", bg='yellow', font=('Georgia', 20))
abc2=Label(frame2, text="Decryption", fg="red", bg='cyan', font=('Georgia', 20))

abc1.place(x=10, y=40)
abc2.place(x=10, y=40)

enter_key1=Label(frame1, text="Enter key:", bg='yellow')         #label of enter key 1
enter_key1.place(x=10, y=100)
enter_key2=Label(frame2, text="Enter key:", bg='cyan')         #label of enter key 2
enter_key2.place(x=10, y=100)

enter_data1=Label(frame1, text="Enter data:", bg='yellow')         #label of enter data 1
enter_data1.place(x=10, y=150)
enter_data2=Label(frame2, text="Enter code:", bg='cyan')         #label of enter data 2
enter_data2.place(x=10, y=150)


key1=Entry(frame1, width=30)                                        #key1
key1.place(x=134, y=100)
key2=Entry(frame2, width=30)                                        #key2
key2.place(x=134, y=100)

data1=Entry(frame1, width=30)                                        #data1
data1.place(x=134, y=150)
data2=Entry(frame2, width=30)                                        #data2
data2.place(x=134, y=150)


encrypt=Button(frame1, height=2, width=7, text='Encrypt', command=lambda:buttonclick1(key1.get(), data1.get()))
encrypt.pack(side=BOTTOM, pady=10)
decrypt=Button(frame2, height=2, width=7, text='Decrypt', command=lambda:buttonclick2(key2.get(), data2.get()))
decrypt.pack(side=BOTTOM, pady=10)


outputis1=Label(frame1, text="Encrytion:", bg='yellow')         #label of enter data 1
outputis1.place(x=10, y=200)
outputis2=Label(frame2, text="Decryption:", bg='cyan')         #label of enter data 2
outputis2.place(x=10, y=200)

frame1.pack()
frame2.pack()               
root1.mainloop()
root2.mainloop()
