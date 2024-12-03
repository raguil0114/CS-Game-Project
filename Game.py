from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Username Input with Background")
root.geometry("1920x1080")  # Adjust to fit the background image

# Background image setup
bg_image = Image.open("Dirt.png")  # Replace with your image file
bg_image = bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for the background image
canvas = Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")


# This will add windows to the list of frames
frames = []

#This function clears the windows in the frame to open up new frames
def clearFrames():
    #for every element that is added to the frame
    for elements in frames:
        #delete all the elements in the frame
        canvas.delete(elements)
    #it is now an empty list
    frames.clear()

def open_frame1():
    #If there is any frames from previous windows (frame 2, frame 3) clear those frames
    clearFrames()

    #global variables for windows
    global label_window, username_window, userSubmit, outputWindow


    label = Label(root, text="What is your name?: ", font=("Times", 28))
    label_window = canvas.create_window(565, 375, anchor="nw", window=label)
    #Appending label_window adds to the frames list (see line 20)
    frames.append(label_window)

    username = Entry(root, font=("Times", 28), width=30)
    username_window = canvas.create_window(885, 375, anchor="nw", window=username)
    #add to frames list
    frames.append(username_window)
    
    #this function helps user submit there username
    def submit():
        global frame2butt, frame2Window
        #user = username.get() get's the info on the user input
        user = username.get()

        #output prints out what happens if user presses submit
        output.config(text=f"Welcome, {user}. Ready to start?")
    
        
        # This button will access the function open_frame2
        frame2butt = Button(root, text="Let's Go!", font=("Times", 32), command=open_frame2)
        frame2Window = canvas.create_window(850, 535, anchor="nw", window=frame2butt)
        #add to frames list
        frames.append(frame2Window)

        #hides the button after the user presses the button
        canvas.itemconfig(userSubmit, state="hidden")

    #when user presses submit name, the command will run the submit() function
    submit = Button(root, text="Submit Name", font=("Times", 32), command=submit)
    userSubmit = canvas.create_window(750, 450, anchor="nw", window=submit)
    #add to frames list
    frames.append(userSubmit)

    #this output is for the username to be shown in the text
    output = Label(root, text="", font=("Times", 32),)
    outputWindow = canvas.create_window(950, 485, window=output)
    #add to frames list
    frames.append(outputWindow)



def open_frame2():
    #clears frames from previous frames and shows the frames in this function
    clearFrames()
    global  label2_window, start_button_window, return_button_window, theBUTT, theBUTTWINDOW, text1 # Declare these as global
    
    #750 is the center
    label2 = Label(root, text="Welcome to the Game!", font=("Times", 32))
    label2_window = canvas.create_window(770, 185, anchor="nw", window=label2)
    frames.append(label2_window)

    theBUTT= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW = canvas.create_window(50, 950, anchor="nw", window=theBUTT)
    
    theNext= Button(root, text="Next", font=("Times", 15), command=open_frame3)
    theNextWindow = canvas.create_window(950, 950, anchor="nw", window=theNext)
    
    frames.append(theBUTTWINDOW)
    frames.append(theNextWindow)
   
    story = ["Every story has it's orgins. You were once a noble knight for a grand empire, ",
            "you were respected by all and were on your way to become the king's right hand man",
            "However, the most fierceful dragon told from the earlest of times has awoken and commences an attack on the kingdom",
            "Chaos falls as you hear the people screaming and crying. The king orders his military to attack the dragon and defends the people.",
            "As every personal scrambles to aquire their equipment and gather their weapons to take down the dragon,",
            "the King give you a different order.",
            "He has given you the task to protect his daughter; who is the princess of the empire",
            "Unfortunely, this task is for naught as the dragon decimates the roof of the castle.",
            "Debris falls all around you as you and the rest of the men within the room race to the door to escape",  
            "The king yells for you to escape but ensure that you swear with all your life to protect the princess",
            "It is at this where there is a giant explosion in front of you; everything goes dark and silent"
                ]
    
    textDisplay = "\n".join(story)
    text1 = canvas.create_text(915, 475,text=textDisplay, anchor="center", font=("Times", 26), fill="white")
    frames.append(text1)
    

def open_frame3():
    clearFrames()
    
    global theBUTT2, theBUTTWINDOW2, text2  # Declare these as global
    
    theBUTT2= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW2 = canvas.create_window(50, 950, anchor="nw", window=theBUTT2)
    
    theNext2= Button(root, text="Next", font=("Times", 15), command=open_frame4)
    theNextWindow2 = canvas.create_window(950, 950, anchor="nw", window=theNext2)
    
    frames.append(theBUTTWINDOW2)
    frames.append(theNextWindow2)
   
    story2 = ["After an unknown amount of time you awaken in a forest. Confused; you try to gather yourself and your thoughts",
              "Confused; you try to gather yourself and your thoughts",
              "You remember the last thing the king told you.",
              "This is where your journey begins.",
              "Your new mission is to get back to the castle and rescue to princess;",
              "if there is anything to rescue at all",
              "Since the explosion you have lost your equipment and are empty handed.",
              "You must make your way towards the castle and find anything you can to slay the dragon.",
            "Only one problem; you have no clue where you are.",
            "Your only hope is to move within the forest and find your way back to the castle",
            "You start down by following anything that may give a hint as to where you are.",
            "You notice bits and pieces of nature; as if it has been distrubed with.",
            "It all comes from a singular direction, so you start walking towards the debris."
            ]
    
    textDisplay = "\n".join(story2)
    text2 = canvas.create_text(800, 450,text=textDisplay, anchor="center", font=("Times", 26), fill="white")
    frames.append(text2)
   

def open_frame4():
    clearFrames()
   
    global theBUTT3, theBUTTWINDOW3, text3  # Declare these as global
    
    theBUTT3= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW3 = canvas.create_window(50, 950, anchor="nw", window=theBUTT3)
    
    theNext3= Button(root, text="Next", font=("Times", 15), command=open_frame5)
    theNextWindow3 = canvas.create_window(950, 950, anchor="nw", window=theNext3)
    
    
    frames.append(theBUTTWINDOW3)
    frames.append(theNextWindow3)
   
    story3 = ["As you move down this path you stubmble upon a peculiar graveyard.",
               "You see what appears to be bones of humans and headstones with no text on them. ", 
               "Something glimmers and you see a sword that is pierced through a skeleton's ribcage.",
               "With nothing on your person you decied to take the sword as your own.",
               "You withdraw the sword from the skeleton and feel some sort of power surge within you as you hold onto the handle.",
               "Somehow the sword has been perserved and is in pristine condition",
               "A sense of despair then takes over you; something is not right you. You feel as if something has awoken.",
               "The skeleton from which you took the sword from suddenly starts to rattle.",
               "Its severed bones from limbs to head take form back to its original shape as if being structed back together by an unseen force.",
               "As it comes to, it locks eyes with your own; piercing into you with its empty eye sockets",
               "Obvioulsy you realize that this is not normal and must be the work of some type of evil magic.",
               "The only thing that you can recall is the teaching of one of the most evil magic to exit; necromancy",
               "You remeber of the tale of a necromancer who onced traveled to the kingdom long ago to seek refuge",
               "He pleaded with the knights, claiming to have the blessing of God himself to heal and cure anything",
               "He demostrated his 'blessing' and convinced the King at the time to let him stay within the kingdom.",
               "The necromancer was grateful for the king's acceptance but, unbeknowst to the king, he would meet his demise.",
               "One night, the necromancer snuck into the king's chamber and killed the king.",
               "Filled with greed, the necromancer aimed to take control of the kingdom and rule it for his own.",
               "However, despite with his powerful dark magic, he was no match for the overwhelming-",
               "number of knights who took to battle agaisnt the necromancer",
               "He was captured and sent to death, far away from the kingdom.",
               "As to the execution process and location, no one was certain how and where it occured",
               "You may have found the answer to that age-old question",
               "You suspect that this may be the alleged necromancer from long ago.",
               "With that, the skeleton takes a stance and prepares to attack you",
               "With your sword drawn you take a stance, ready to fight."
               ]
    
    textDisplay = "\n".join(story3)
    text3 = canvas.create_text(720, 475,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text3)
   

def open_frame5():
    clearFrames()
   
    global theBUTT4, theBUTTWINDOW4, text4  # Declare these as global
    
    theBUTT4= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW4 = canvas.create_window(50, 950, anchor="nw", window=theBUTT4)
    
    theNext4= Button(root, text="Next", font=("Times", 15), command=open_frame6)
    theNextWindow4 = canvas.create_window(950, 950, anchor="nw", window=theNext4)
    
    
    frames.append(theBUTTWINDOW4)
    frames.append(theNextWindow4)
   
    story4 = ["After defeating the skeleton, you continue on with your jounrey",
                "You notice that the debris that you were following get less and less",
                "Alongside the trees you notice a small opening in between",
                "You see small structures; they appear to be cottages of some sort"
                "You decide to walk towards the buildings with the thought of finding something that might help you",
                "As you get closer you notice that there are people moving around the area",
                "You realize it is a small village that you have encountered"
                "However, you also see something siniter hovering above the village",
                "A dark shadow figure has taken over the village and is terriozing the villagers",
                "You haven't been caught just yet but you feel as if you must help the locals",
                "You appear in front of the figure with your sword in hand",
                "The figure stares at you blankly; it knows you are in fear",
                "Suddenly, the figure raises one of it's hand; charging an attack",
                "Once again, it's time to fight"
                
                ]
    
    textDisplay = "\n".join(story4)
    text4 = canvas.create_text(950, 475,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text4)
    
def open_frame6():
    clearFrames()
   
    global theBUTT5, theBUTTWINDOW5, text5  # Declare these as global
    
    theBUTT5= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW5 = canvas.create_window(50, 950, anchor="nw", window=theBUTT5)
    
    theNext5= Button(root, text="Next", font=("Times", 15), command=open_frame7)
    theNextWindow5 = canvas.create_window(950, 950, anchor="nw", window=theNext5)
    
    
    frames.append(theBUTTWINDOW5)
    frames.append(theNextWindow5)
   
    story5 = ["The villagers; all puzzled as to what has happened, approach you",
                "You explain to them about the figure and how you saved them",
                "They show there grattitude towards you for helping them",
                "They wish to return the favor in any way that they can",
                "You ask the vilagers if they know anything about the kingdom since the attack",
                "They tell you about some people walking down te path where you came from",
                "They as well approached the villagers asking for help as they explained their situation",
                "It appears that the group of people also came from the castle and had survived the dragons attack",
                "They said that the group was looking for a knight who could kill the dragon and save the princess",
                "With that, you ask one more question",
                "You ask the villagers if there is some type of short cut to reach the castle",
                "The villagers inform you about a cave that can lead you straight to the castle",
                "However, the cave is home to a group of goblins who are know for their violent behavior",
                "You thank the villagers and with that you venture fourth"
                ]
    
    textDisplay = "\n".join(story5)
    text5 = canvas.create_text(550, 475,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text5)

def open_frame7():
    clearFrames()
   
    global theBUTT6, theBUTTWINDOW6, text6  # Declare these as global
    
    theBUTT6= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW6 = canvas.create_window(50, 950, anchor="nw", window=theBUTT6)
    
    theNext6= Button(root, text="Next", font=("Times", 15), command=open_frame8)
    theNextWindow6 = canvas.create_window(950, 950, anchor="nw", window=theNext6)
    
    
    frames.append(theBUTTWINDOW6)
    frames.append(theNextWindow6)
   
    story6 = ["As you walk down the path you take in the view around you",
                "You feel the breeze of the wind",
                "The scent of the grass and soil",
                "The birds chirping within the trees",
                "All giving you a sense of peace",
                "And as quickly as these feeling appeared; they vanish in an instant",
                "You reached the enterence of the cave; taking a peak inside you feel uncertain if this is the best choice",
                "The words of the king reminisce within your mind; you swore with your life, you would protect the princess",
                "You can't give up now; and you don't plan to",
                "You move foward, entering the cave",
                ]
    
    textDisplay = "\n".join(story6)
    text6 = canvas.create_text(625, 475,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text6)

def open_frame8():
    clearFrames()
   
    global theBUTT7, theBUTTWINDOW7, text7  # Declare these as global
    
    theBUTT7= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW7 = canvas.create_window(50, 950, anchor="nw", window=theBUTT7)
    
    theNext7= Button(root, text="Next", font=("Times", 15), command=open_frame9)
    theNextWindow7 = canvas.create_window(950, 950, anchor="nw", window=theNext7)
    
    
    frames.append(theBUTTWINDOW7)
    frames.append(theNextWindow7)
   
    story7 = ["Once inside you feel as if there is something watching you",
                "It's dark and cold but with the little visability you have you press on",
                "One step at a time you are wary of anything that might jump out of the shawdows",
                "A faint light glistens along the walls of the cave",
                "As you get closer the light gets brighter and brighter",
                "You find the source of the light; a large area of the cave with a red circle drawn in the middle",
                "In front of the cirlce is what appears to be a throne made out of bones",
                "Just then a loud grunt echos through the cave and resonates around you",
                "Frantically looking around searching for where the sound is coming from",
                "Before you can even guess a group of globins appears from the shadows, then another group appears, and then another",
                "You are surrounded; theres no other choice other than to fight your way out",
                "A new noise takes over the loud chants of the globins",
                "Loud, crashing footsteps shake the ground beneath you",
                "From a deeper part of the cave, another globin makes an appearance expect this one is much larger than the rest",
                "All of the globin suddenly fall silent; this giant one might be the leader",
                "The giant globin demands you to speak your purpose for entering their cave",
                "You give your reason, reluctant if this leader of a globin will even consider what you say",
                "Silence...the globin leader then gives you an offer",
                "He will grant you passage through the cave unscathed and you will kill the dragon and return with its head",
                "You question as to why he wants the dragons head; he wants revenge for what the dragon has done to his tribe",
                "Considering the situation you are in, you agree to their offer; the leader order a group of globins to lead you throught the cave",
                "With that, the journey continues"
                ]
    
    textDisplay = "\n".join(story7)
    text7 = canvas.create_text(725, 475,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text7)

def open_frame9():
    clearFrames()
   
    global theBUTT8, theBUTTWINDOW8, text8  # Declare these as global
    
    theBUTT8= Button(root, text="Return to Menu", font=("Times", 15), command=open_frame1)
    theBUTTWINDOW8 = canvas.create_window(50, 950, anchor="nw", window=theBUTT8)
    
    theNext8= Button(root, text="Next", font=("Times", 15), command=open_frame9)
    theNextWindow8 = canvas.create_window(950, 950, anchor="nw", window=theNext8)
    
    
    frames.append(theBUTTWINDOW8)
    frames.append(theNextWindow8)
   
    story8 = ["The goblins guide you to an exit deep in the caves",
                "They stare at you as yo walk away from the cave, as if they wanted to fight",
                "Regardless, you move foward towards the castle; hoping that the princess is still alive",
                "The sun starts to set as night falls over you and the forest.",
                "It has been hours since you awoken and you think about everything that has happened since then",
                "You feel exhasted and want to settle down for the night,",
                "But you know you can't; the longer you take to reach the castle, the princess's fate becomes more certain",
                "You press on, resilent to keep your word to the king and save the princess",
                "At last you finally make it to the base of the castle; turns out, so did others as well",
                "Others who have survived the attack have set up a camp at the base",
                "You enter the camp and the others take notice of you",
                "Everyone is shocked to see you standing tall; alive and well",
                "The people exclaim their joy towards you, they thought you had died in the attack",
                "As everyone regorups they inform you that they have tried their absolute best to attack the dragon but have failed",
                "They beleive that you are the only one who is capable to slay the dragon",
                "After all, this is the whole reason you are here",
                "Determined, you ask everyone to gather as much supplies to prepare for the battle",
                "The moment arrives, it is time to fight the dragon and save the princess",
                "Everyon cheers you on, their faith rest with you",
                "You walk to the entrance of the castle, the feeling of determination fills your very being",
                "Once you step foot in the castle, the dragon lays dormant on the ground",
                "It senses your pressence and awakens, towering over you",
                "It lets out a screeching roar as you draw your sword",
                "The moment is now, its time to slay the dragon",
                ]
    
    textDisplay = "\n".join(story8)
    text8 = canvas.create_text(675, 475,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text8)



#I WILL MAKE THE ENDING AFTER SOME FEEDBACK



open_frame1()
root.mainloop()