# Tkinter dnd npc generator base
import tkinter as tk
from dnd_class_npcs import *

# npc_data = ['Cuchu: Male Elf Priest, N. Str 12, Dex 12, Con 11, Int 10, Wis 8, Cha 9. Cuchu has a narrow face, with short black hair and bright hazel eyes. He wears well-made clothing and an amulet of luminous crystal. Cuchu secretly serves Sadya, an ancient monstrous god.', 'Garib Boffin: Male Halfling Fighter, LE. Str 12, Dex 13, Con 7, Int 5, Wis 13, Cha 10. Garib is heavyset, with braided red hair and dark brown eyes. He wears half plate and wields a warhammer and net.', 'Hamas: Male Human Craftsman, N. Str 11, Dex 7, Con 9, Int 14, Wis 11, Cha 7. Hamas is rugged in appearance, with black hair and hazel eyes. He wears modest garments and a yellow cloak. Hamas secretly serves Beraie, an ancient demonic god.', 'Nerdelye: Female Elf Servant, LN. Str 12, Dex 10, Con 13, Int 9, Wis 7, Cha 13. Nerdelye has gray hair and sharp gray eyes, and pointed ears. She wears modest garments and several small tools hang from her belt.', 'Estol: Male Elf Scholar, NE. Str 7, Dex 11, Con 11, Int 10, Wis 9, Cha 6. Estol has curly gray hair and soft green eyes, and numerous horrific scars. He wears modest garments and a dragonscale cloak. Estol is deceitful and fanatical.', 'Ether Hewe: Male Human Scholar, N. Str 9, Dex 12, Con 12, Int 12, Wis 15, Cha 9. Ether is rough in appearance, with tangled auburn hair and blue eyes. He wears modest garments and numerous rings. Ether is practical and honest.', 'Anthond: Male Half-elf Rogue, LG. Str 12, Dex 13, Con 9, Int 11, Wis 13, Cha 7. Anthond is tall, with straight brown hair and sharp green eyes. He wears leather armor and wields a rapier.', 'Eahburg: Female Human Paladin, Good. Str 10, Dex 12, Con 7, Int 11, Wis 9, Cha 14. Eahburg is fair in appearance, with tangled silver hair and soft hazel eyes. She wears splint armor and wields a whip. Eahburg is steadfast and hardworking.', 'Damay: Female Halfling Wizard, N. Str 12, Dex 8, Con 11, Int 12, Wis 11, Cha 9. Damay has an angular face, with brown hair and blue eyes. She wears plain clothing and wields a dagger. Damay suffers a mild allergy to shellfish.', 'Houna: Female Human Monk, N. Str 13, Dex 11, Con 11, Int 14, Wis 17, Cha 9. Houna has red hair and sharp green eyes, and a beaked nose. She wears modest garments and wields nunchaku (club) and sai (dagger). Houna seeks to discover why she keeps having the same dream.']

npcs_class = npcs()
npcs_class.init_npcs()
npc_data = npcs_class.list_npcs()

# counter = 0 
# def counter_label(label):
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()
 
def generate_npcs():
    """Reconfigure all currently loaded NPC summaries."""
    # label_gen_npc.config(text="asdliufcmvhasoidufnvyasiodufbynvaiosudnyfoiausdynfviausndhfvlasdf2")
    npcs_class.refresh_npcs()
    npc_data = npcs_class.list_npcs()
    for i in range(len(npc_data)):
        label[i].config(text=npc_data[i])
    return

def generate_error():
    """Create an error that should appear in the window."""
    return


root = tk.Tk()
root.title("DnD NPC Generator")
root.geometry("320x900")
root.resizable(0, 0)

back = tk.Frame(master=root)
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)

# label = tk.Label(back, fg="green")
# label.grid(row=0, column=1)
# counter_label(label)

# button = tk.Button(back, text='Stop', width=25, command=root.destroy)
# button.grid(row=0, column=0)

# label_gen_npc = tk.Label(back,
#                         text="asdliufcmvhasoidufnvyasiodufbynvaiosudnyfoiausdynfviausndhfvlasdf",
#                         fg="green",
#                         padx=10,
#                         justify=tk.RIGHT,
#                         wraplength=100)
# label_gen_npc.grid(row=1, column=1)

label = []
for i in range(len(npc_data)):
    label.append(tk.Label(back,
             text=npc_data[i],
             wraplength=300,
             padx=10))
    label[i].grid(row=i+1, column=1)

button_gen_npcs = tk.Button(back,
                            text="Generate new NPCS",
                            width=25,
                            command=generate_npcs)
button_gen_npcs.grid(row=0, column=1)
root.mainloop()
