from __future__ import unicode_literals
import tkinter as tk
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print_to_box(msg)


def my_hook(d):
    if d['status'] == 'downloading':
        print_to_box(d['filename'] + ' ' + d['_percent_str'] + ' ' + d['_eta_str'] + '\n')
    if d['status'] == 'finished':
        print_to_box("Download complete. \n\n")


dl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def download(ipt):
    with youtube_dl.YoutubeDL(dl_opts) as ydl:
        ydl.download([ipt])

def convert_pressed():
    url = entry_url.get()
    if len(url) == 0:
        print_to_box("ERROR: invalid URL\n")
    else:
        print_to_box("Starting...\n")
        download(url)

def print_to_box(msg):
    output_box.config(state='normal')
    output_box.insert(tk.END, msg)

window = tk.Tk()
window.title("Youtube to MP3")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

label_url = tk.Label(master=frm_form, text="Enter URL:")
entry_url = tk.Entry(master=frm_form, width=50)

frm_output = tk.Frame(relief=tk.GROOVE, borderwidth=3)
frm_output.pack()

output_label =tk.Label(master=frm_output, text="Output:")
output_box = tk.Text(master=frm_output, state='disabled', width=80)

output_label.grid(row=0, column = 0)
output_box.grid(row=1, column = 1)

label_url.grid(row=0, column=0)
entry_url.grid(row=0, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_convert = tk.Button(master=frm_buttons, text="Convert!", command=convert_pressed)
btn_convert.pack(side=tk.RIGHT, padx=10, ipadx=10)

window.mainloop()