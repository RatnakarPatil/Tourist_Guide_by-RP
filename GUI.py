from tkinter import *
from PIL import Image, ImageTk
global selected_place


def website():
    import webbrowser
    get_url = webbrowser.open(
        f'https://www.google.com/search?q={selected_place}')


def submit():
    global selected_place, lbx
    selected_place = lbx.get(ACTIVE)
    root.destroy()
    root1 = Tk()
    root1.title("INFORMATION FOR YOUR CHOOSE ")  # NEW WINDOW

    # Waterfalls: "Kune Falls", "Tamhini Falls", "Devkund Falls", "Bendewadi Falls"

    if(selected_place == "Kune Falls"):
        root1.geometry("1920x1080")
        image = Image.open("zzkunewaterfall.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif(selected_place == "Tamhini Falls"):
        root1.geometry("1920x1080")
        image = Image.open("zztamhiniwaterfall.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif(selected_place == "Devkund Falls"):
        root1.geometry("1920x1080")
        image = Image.open("zzdevkundwaterfall.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif(selected_place == "Bendewadi Falls"):
        root1.geometry("1920x1080")
        image = Image.open("zzbendewadifalls.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    # forts "Lal Mahal", "Aga Khan Palace", "Carla Caves", "Lohagad fort"

    elif(selected_place == "Lal Mahal"):
        root1.geometry("1920x1080")
        image = Image.open("zzlalmahal.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif(selected_place == "Aga Khan Palace"):
        root1.geometry("1920x1080")
        image = Image.open("zzagakhan.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif(selected_place == "Carla Caves"):
        root1.geometry("1920x1080")
        image = Image.open("zzcarlacaves.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif(selected_place == "Lohagad fort"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    # dam "Khadakwasla Dam", "Bhusi Dam", "Mulshi Dam", "Panshet Dam", "Hadshi Dam", "Peshave Park Lake"

    elif (selected_place == "Khadakwasla Dam"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Bhusi dam"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Mulshi dam"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Panshet Dam"):
        root1.geometry("1920x1080")
        image = Image.open("zzpanshet.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Hadshi dam"):
        root1.geometry("1920x1080")
        image = Image.open("zzhadshi.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Peshave Park Lake"):
        root1.geometry("1920x1080")
        image = Image.open("zzpeshven.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    # Temple "ISKON NVCC", "Tulsi Baug Ganpati Temple", "Shreemant Dagdusheth Halwai Ganpati",
    #              "Balaji Templei", "Shri Omkareshwar Temple", "Alandi Devsthan"

    elif (selected_place == "ISKON Temple"):
        root1.geometry("1920x1080")
        image = Image.open("zziskon.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Tulsi Baug Ganpati Temple"):
        root1.geometry("1920x1080")
        image = Image.open("zztulshibag.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Shreemant Dagdusheth Halwai Ganpati"):
        root1.geometry("1920x1080")
        image = Image.open("zzdgdu.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Balaji Temple"):
        root1.geometry("1920x1080")
        image = Image.open("zzbalaji.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Shri Omkareshwar Temple"):
        root1.geometry("1920x1080")
        image = Image.open("zzomkareshwar.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Alandi Devsthan"):
        root1.geometry("1920x1080")
        image = Image.open("zzalandi.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    # Garden "Okayama Friendship Garden", "Osho Garden", "Bund Garden",
    #              "Yashwantrao Chavan Garden", "Chatrapati Shivaji Maharaj Garden"

    elif (selected_place == "Okayama Friendship Garden"):
        root1.geometry("1920x1080")
        image = Image.open("zzokayama.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Osho Garden"):
        root1.geometry("1920x1080")
        image = Image.open("zzosho.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Bund Garden"):
        root1.geometry("1920x1080")
        image = Image.open("zzbund.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Yashwantrao Chavan Garden"):
        root1.geometry("1920x1080")
        image = Image.open("zzyashwant.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Chatrapati Shivaji Maharaj Garden"):
        root1.geometry("1920x1080")
        image = Image.open("zzmaharaj.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    # Industrial "BAJAJ Auto", "Bharat Forge", "Century Enka", "Finolex Cables"

    elif (selected_place == "BAJAJ Auto Pvt Ltd"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Bharat Forge Pvt Ltd"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Century Enka Ltd"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Finolex Cables Ltd"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    # Hill "Mahabaleshwar", "Lonavala","Matheran", "Panchagani", "Bhandardara"

    elif (selected_place == "Mahabaleshwar"):
        root1.geometry("1920x1080")
        image = Image.open("zzmahableshwar.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Lonavala/Khandala Hills Series"):
        root1.geometry("1920x1080")
        image = Image.open("zzlonavla.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Matheran"):
        root1.geometry("1920x1080")
        image = Image.open("zzmatheran.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Panchagani"):
        root1.geometry("1920x1080")
        image = Image.open("zzpancg.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Bhandardara"):
        root1.geometry("1920x1080")
        image = Image.open("zzbhandardare.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    #  fort "Lal Mahal", "Aga Khan Palace", "Carla Caves", "Lohagad fort"

    elif (selected_place == "Lal Mahal"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Aga Khan Palace"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Carla Caves"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    elif (selected_place == "Lohagad fort"):
        root1.geometry("1920x1080")
        image = Image.open("zzlohagad.png")
        image = image.resize((1200, 550))
        photo = ImageTk.PhotoImage(image)
        Label(root1, image=photo).pack()

    else:
        pass

    Button(root1, text="More Info", font="Serif 12 bold", command=website,
           padx=20, bg="light green").pack(padx=10, pady=30, anchor="ne")
    root.mainloop()


def temple():
    list2 = ["ISKON Temple", "Tulsi Baug Ganpati Temple", "Shreemant Dagdusheth Halwai Ganpati",
             "Balaji Temple", "Shri Omkareshwar Temple", "Alandi Devsthan"]
    global lbx
    lbx = Listbox(frame2)
    lbx.grid(row=2, column=1, pady=20)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame2, text="Submit", command=submit).grid(
        row=3, column=0, pady=20)


def garden():
    list2 = ["Okayama Friendship Garden", "Osho Garden",
             "Yashwantrao Chavan Garden", "Chatrapati Shivaji Maharaj Garden"]
    global lbx, selected_place
    lbx = Listbox(frame2)
    lbx.grid(row=2, column=2, pady=20)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame2, text="Submit", command=submit).grid(
        row=3, column=0, pady=20)


def industry():
    list2 = ["BAJAJ Auto", "Bharat Forge", "Century Enka", "Finolex Cables"]
    global lbx
    lbx = Listbox(frame2)
    lbx.grid(row=2, column=3, pady=20)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame2, text="Submit", command=submit).grid(
        row=3, column=0, pady=20)


def hillstation():
    list2 = ["Mahabaleshwar", "Lonavala",
             "Matheran", "Panchagani", "Bhandardara"]
    global lbx
    lbx = Listbox(frame2)
    lbx.grid(row=2, column=4, pady=20)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame2, text="Submit", command=submit).grid(
        row=3, column=0, pady=20)


def fort():
    list2 = ["Lal Mahal", "Aga Khan Palace", "Carla Caves", "Lohagad fort"]
    global lbx
    lbx = Listbox(frame2)
    lbx.grid(row=2, column=5, pady=20)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame2, text="Submit", command=submit).grid(
        row=3, column=0, pady=20)


def waterfall():
    list2 = ["Kune Falls", "Tamhini Falls", "Devkund Falls", "Bendewadi Falls"]
    global lbx
    lbx = Listbox(frame2)
    lbx.grid(row=2, column=6, pady=20)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame2, text="Submit", command=submit).grid(
        row=3, column=0, pady=20)


def dam():
    list2 = ["Khadakwasla Dam", "Bhusi Dam", "Mulshi Dam",
             "Panshet Dam", "Hadshi Dam", "Peshave Park Lake"]
    global lbx
    lbx = Listbox(frame2)
    lbx.grid(row=2, column=7, pady=20)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame2, text="Submit", command=submit).grid(
        row=3, column=0, pady=20)


def sum_place():
    frame1.destroy()
    root.title("FRAME 2")

    global frame2
    frame2 = Frame(root, bg="orange")
    frame2.pack(fill=BOTH)

    Label(frame2, text="Select Destination",
          font="calibri 18 bold", bg="orange").grid(row=0, column=5)

    ztemp_button = Button(frame2, image=ztemp, command=temple)
    ztemp_button.grid(row=1, column=1, padx=10, pady=10)

    zgar_button = Button(frame2, image=zgar, command=garden)
    zgar_button.grid(row=1, column=2, padx=10, pady=10)

    zind_button = Button(frame2, image=zind, command=industry)
    zind_button.grid(row=1, column=3, padx=10, pady=10)

    zhill_button = Button(frame2, image=zhill, command=hillstation)
    zhill_button.grid(row=1, column=4, padx=10, pady=10)

    zfort_button = Button(frame2, image=zfort, command=fort)
    zfort_button.grid(row=1, column=5, padx=10, pady=10)


def win_place():
    frame1.destroy()
    root.title("FRAME 2")
    global frame2
    frame2 = Frame(root, bg="orange")
    frame2.pack(fill=BOTH)

    Label(frame2, text="Select Destination",
          font="Aerial 18 bold", bg="orange").grid(row=0, column=3)

    zind_button = Button(frame2, image=zind, command=industry)
    zind_button.grid(row=1, column=3, padx=10, pady=10)

    zhill_button = Button(frame2, image=zhill, command=hillstation)
    zhill_button.grid(row=1, column=4, padx=10, pady=10)

    zfort_button = Button(frame2, image=zfort, command=fort)
    zfort_button.grid(row=1, column=5, padx=10, pady=10)


def rainy_place():
    frame1.destroy()
    root.title("FRAME 2")
    global frame2
    frame2 = Frame(root, bg="orange")
    frame2.pack(fill=BOTH)

    Label(frame2, text="Select Destination",
          font="Aerial 18 bold", bg="orange").grid(row=0, column=6)

    zgar_button = Button(frame2, image=zgar, command=garden)
    zgar_button.grid(row=1, column=2, padx=10, pady=10)

    zwater_button = Button(frame2, image=zwater, command=waterfall)
    zwater_button.grid(row=1, column=6, padx=10, pady=10)

    zdam_button = Button(frame2, image=zdam, command=dam)
    zdam_button.grid(row=1, column=7, padx=10, pady=10)


def new_window():

    main_frame.destroy()

    # frame 1
    root.title("FRAME 1")

    global frame1
    frame1 = Frame(root, bg="light green")
    frame1.pack(fill=BOTH)

    Label(frame1, text="Select Season", font="Aerial 30 bold",
          bg="light green").grid(row=0, column=3)

    zsum_button = Button(frame1, image=zsum, command=sum_place)
    zsum_button.grid(row=1, column=0, padx=10, pady=10)

    zwin_button = Button(frame1, image=zwin, command=win_place)
    zwin_button.grid(row=1, column=3, padx=10, pady=10)

    zmon_button = Button(frame1, image=zmon, command=rainy_place)
    zmon_button.grid(row=1, column=6, padx=10, pady=10)


root = Tk()
root.geometry("1500x1000")
# extra
root.title("MAIN FRAME")
main_frame = Frame(root)
main_frame.pack(expand=1, fill=BOTH)
Label(main_frame, text=" l- Tourist Guide -l", font="Calibri 50 bold",
      fg="white", bg="black").pack(padx=10, pady=10)
image = Image.open("zLogo.png")
image = image.resize((1200, 550))
photo = ImageTk.PhotoImage(image)
Label(main_frame, image=photo).pack()

Label(main_frame, text="About Us", font="Serif 18 bold", padx=10).pack(anchor="nw")
Label(main_frame, text="Tourists can use this guide for different purposes like searching a locations,"
      "getting basic textual information, pictorial information of location"
      "which normally we could not find in default Google maps.", font="Aerial-black 14", padx=10).pack(anchor="nw")
Label(main_frame, text="The guide uses Google Map API, Internet, and cellular data to provide its services.",
      font="Aerial-black 14", padx=10).pack(anchor="nw")

Button(main_frame, text="Proceed", font="Serif 12 bold",

       command=new_window, padx=20, bg="light green").pack(padx=30, anchor="ne")


zsum = Image.open("zsum.png")
resized1 = zsum.resize((487, 487))
zsum = ImageTk.PhotoImage(resized1)

zwin = Image.open("zwinter.png")
resized1 = zwin.resize((487, 487))
zwin = ImageTk.PhotoImage(resized1)

zmon = Image.open("zmonsoon.png")
resized1 = zmon.resize((487, 487))
zmon = ImageTk.PhotoImage(resized1)

# summer buttons
ztemp = Image.open("ztemple.png")
resized1 = ztemp.resize((200, 200))
ztemp = ImageTk.PhotoImage(resized1)

zgar = Image.open("zgardenn.png")
resized1 = zgar.resize((200, 200))
zgar = ImageTk.PhotoImage(resized1)

zind = Image.open("zindustryy.png")
resized1 = zind.resize((200, 200))
zind = ImageTk.PhotoImage(resized1)

zhill = Image.open("zhillstation.png")
resized1 = zhill.resize((200, 200))
zhill = ImageTk.PhotoImage(resized1)

zfort = Image.open("zfort.png")
resized1 = zfort.resize((200, 200))
zfort = ImageTk.PhotoImage(resized1)

# winter buttons
zind = Image.open("zindustryy.png")
resized1 = zind.resize((200, 200))
zind = ImageTk.PhotoImage(resized1)

zhill = Image.open("zhillstation.png")
resized1 = zhill.resize((200, 200))
zhill = ImageTk.PhotoImage(resized1)

zfort = Image.open("zfort.png")
resized1 = zfort.resize((200, 200))
zfort = ImageTk.PhotoImage(resized1)

# rainy buttons
zgar = Image.open("zgardenn.png")
resized1 = zgar.resize((200, 200))
zgar = ImageTk.PhotoImage(resized1)

zwater = Image.open("zwaterfall.png")
resized1 = zwater.resize((200, 200))
zwater = ImageTk.PhotoImage(resized1)

zdam = Image.open("zdam.png")
resized1 = zdam.resize((200, 200))
zdam = ImageTk.PhotoImage(resized1)

root.mainloop()
