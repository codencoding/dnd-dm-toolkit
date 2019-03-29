# Tkinter dnd npc generator base
from tkinter import *
from tkinter.ttk import *
from dnd_class_npcs import *
from functools import partial

# npc_data = ['Cuchu: Male Elf Priest, N. Str 12, Dex 12, Con 11, Int 10, Wis 8, Cha 9. Cuchu has a narrow face, with short black hair and bright hazel eyes. He wears well-made clothing and an amulet of luminous crystal. Cuchu secretly serves Sadya, an ancient monstrous god.', 'Garib Boffin: Male Halfling Fighter, LE. Str 12, Dex 13, Con 7, Int 5, Wis 13, Cha 10. Garib is heavyset, with braided red hair and dark brown eyes. He wears half plate and wields a warhammer and net.', 'Hamas: Male Human Craftsman, N. Str 11, Dex 7, Con 9, Int 14, Wis 11, Cha 7. Hamas is rugged in appearance, with black hair and hazel eyes. He wears modest garments and a yellow cloak. Hamas secretly serves Beraie, an ancient demonic god.', 'Nerdelye: Female Elf Servant, LN. Str 12, Dex 10, Con 13, Int 9, Wis 7, Cha 13. Nerdelye has gray hair and sharp gray eyes, and pointed ears. She wears modest garments and several small tools hang from her belt.', 'Estol: Male Elf Scholar, NE. Str 7, Dex 11, Con 11, Int 10, Wis 9, Cha 6. Estol has curly gray hair and soft green eyes, and numerous horrific scars. He wears modest garments and a dragonscale cloak. Estol is deceitful and fanatical.', 'Ether Hewe: Male Human Scholar, N. Str 9, Dex 12, Con 12, Int 12, Wis 15, Cha 9. Ether is rough in appearance, with tangled auburn hair and blue eyes. He wears modest garments and numerous rings. Ether is practical and honest.', 'Anthond: Male Half-elf Rogue, LG. Str 12, Dex 13, Con 9, Int 11, Wis 13, Cha 7. Anthond is tall, with straight brown hair and sharp green eyes. He wears leather armor and wields a rapier.', 'Eahburg: Female Human Paladin, Good. Str 10, Dex 12, Con 7, Int 11, Wis 9, Cha 14. Eahburg is fair in appearance, with tangled silver hair and soft hazel eyes. She wears splint armor and wields a whip. Eahburg is steadfast and hardworking.', 'Damay: Female Halfling Wizard, N. Str 12, Dex 8, Con 11, Int 12, Wis 11, Cha 9. Damay has an angular face, with brown hair and blue eyes. She wears plain clothing and wields a dagger. Damay suffers a mild allergy to shellfish.', 'Houna: Female Human Monk, N. Str 13, Dex 11, Con 11, Int 14, Wis 17, Cha 9. Houna has red hair and sharp green eyes, and a beaked nose. She wears modest garments and wields nunchaku (club) and sai (dagger). Houna seeks to discover why she keeps having the same dream.']

npcs_class = npcs()
npcs_class.init_npcs()
npc_data = npcs_class.list_npcs()
npc_summ = []
npc_labels = []
first_start = True

def generate_npcs():
    """Reconfigure all currently loaded NPC summaries."""
    # label_gen_npc.config(text="asdliufcmvhasoidufnvyasiodufbynvaiosudnyfoiausdynfviausndhfvlasdf2")
    global npcs_class
    global npc_data
    global npc_summ
    global npc_labels
    global first_start

    if first_start:
        # npcs_class.init_npcs()
        # npc_data = npcs_class.list_npcs()

        for i in range(len(npc_data)):
            npc_summ.append(Label(back,
                    text=npc_data[i],
                    wraplength=300))
            npc_summ[i].grid(row=i, column=2)
            npc_labels.append(Label(back,
                                    text="NPC {}".format(i+1),
                                    wraplength=300))
            npc_labels[i].grid(row=i, column=1)

        first_start = False
    else:
        npcs_class.refresh_npcs()
        npc_data = npcs_class.list_npcs()
        for i in range(len(npc_data)):
            npc_summ[i].config(text=npc_data[i])
    return

def generate_error():
    """Create an error that should appear in the window."""
    return


root = Tk()
root.title("DnD NPC Generator")
# root.geometry("320x900")
# root.resizable(0, 0)

back = Frame(master=root)
back.pack_propagate(0)
back.pack(fill=BOTH, expand=1)

# label = tk.Label(back, fg="green")

# label_gen_npc = tk.Label(back,
#                         text="asdliufcmvhasoidufnvyasiodufbynvaiosudnyfoiausdynfviausndhfvlasdf",
#                         fg="green",
#                         padx=10,
#                         justify=tk.RIGHT,
#                         wraplength=100)
# label_gen_npc.grid(row=1, column=1)



framing = Frame(back)
framing.grid(row=0, column=0, rowspan=10, sticky=N)

button_gen_npcs = Button(framing,
                            text="Generate new NPCS",
                            width=25,
                            command=generate_npcs)
button_gen_npcs.pack(side=TOP)

# button = []
# for i in range(20):
#     button.append(tk.Button(framing,
#                     text="test button {}".format(i+1),
#                     width=25))
#     button[i].pack(side=tk.TOP)




# test_list = [1, 2, 3, 4]
# variable = StringVar(framing)
# variable.set(test_list[0])

# dropdown_list = OptionMenu(framing, variable, test_list[0], *test_list)
# dropdown_list.pack(side=TOP)

# labelaaa = Label(framing, text=variable.get())
# labelaaa.pack(side=RIGHT)

def callback(label, var, *args):
    # print("============")
    # print("Label is ")
    # print(label)
    # print("Variable is ")
    # print(variable)
    # print("============")
    label.config(text=var.get())


## Dropdown Menus
dropmenu_lists = npcs_class.dropboxes_lists()
# dropmenu_elems elements are formatted as [[StringVariable, OptionsMenu], ...]
dropmenu_elems = [[] for i in range(4)]

for i in range(len(dropmenu_lists)):
    # Add a string variable to keep track of selected dropdown option
    dropmenu_elems[i] = [StringVar(framing)]
    # Set the initial selected value for the dropdown menu
    dropmenu_elems[i][0].set(dropmenu_lists[i])
    # Create the option menu
    dropmenu_elems[i].append(OptionMenu(framing,
                                    dropmenu_elems[i][0],
                                    dropmenu_lists[i][0],
                                    *dropmenu_lists[i]))
    # Pack the option menu
    dropmenu_elems[i][1].pack(side=TOP)

## Testing dropdown selection with labels
label_list = []
for i in range(len(dropmenu_elems)):
    label_list.append(Label(framing, text=dropmenu_elems[i][0].get()))
    label_list[i].pack(side=TOP)
    variable = dropmenu_elems[i][0]
    variable.trace("w", partial(callback, label_list[i], variable))


root.mainloop()
