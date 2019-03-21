# Tkinter dnd npc generator base
import tkinter as tk


# root = tk.Tk()
# root.title("DnD NPC Generator")

# w = tk.Label(root, text="Hello Tkinter!")
# w.pack()

# button = tk.Button(
#     root, text='Stop', width=25, command=root.destroy)
# button.pack

# root.mainloop()

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
def generate_npc():
    label2.config(text="asdliufcmvhasoidufnvyasiodufbynvaiosudnyfoiausdynfviausndhfvlasdf2")
    return


root = tk.Tk()
root.title("DnD NPC Generator")
root.geometry("400x100")
root.resizable(0, 0)

back = tk.Frame(master=root)
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)

label = tk.Label(back, fg="green")
label.grid(row=0, column=1)
counter_label(label)

button = tk.Button(back, text='Stop', width=25, command=root.destroy)
button.grid(row=0, column=0)

label2 = tk.Label(back,
                  text="asdliufcmvhasoidufnvyasiodufbynvaiosudnyfoiausdynfviausndhfvlasdf",
                  fg="green",
                  padx=10,
                  justify=tk.RIGHT,
                  wraplength=100)
label2.grid(row=1, column=1)

button2 = tk.Button(back, text="Test 2", width=25, command=generate_npc)
button2.grid(row=1, column=0)
root.mainloop()
