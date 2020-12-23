import tkinter as tk
import convert

def convert_pressed():
    url = entry_url.get()
    convert.download(url)

window = tk.Tk()
window.title("Youtube to MP3")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

label_url = tk.Label(master=frm_form, text="Enter URL:")
entry_url = tk.Entry(master=frm_form, width=50)

label_url.grid(row=0, column=0)
entry_url.grid(row=0, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_convert = tk.Button(master=frm_buttons, text="Convert!", command=convert_pressed)
btn_convert.pack(side=tk.RIGHT, padx=10, ipadx=10)

window.mainloop()