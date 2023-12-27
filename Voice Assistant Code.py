import random
import pywhatkit
import time
import pyttsx3
from playsound import playsound
pyobj=pyttsx3.init()
pyobj.setProperty("rate",180)


l = ["sachman", "ronit sachdeva", "rounak", "rounak raj", "rounak singh","rudraksh","rudraksh taya","tau1"]

gfeel = ["good", "happy", "well", "okay", "gud"]
bfeel = ["not", "bad", "worse", "worst"]

feelm = ["job", "boss", "breakup", "wife", "girlfriend", "gf", "health", "pain", "stress", "tension", "tensions",
         "problem", "problems", "money", "study", "accident", "low"]

print("hello this is alexa")
pyobj.say("hello this is ALEXA")
pyobj.runAndWait()
print("what can i do for u")
pyobj.say("what can i do for you?")
pyobj.runAndWait()

print("if you what to know about what i can do for u?")
pyobj.say("if you want to know about what i can do for you")
pyobj.runAndWait()
print()
time.sleep(1)
print("PRESS")
pyobj.say("press")
print("1 for yes")
print("2 for no")
pyobj.say("press 1 for yes and 2 for no")
pyobj.runAndWait()
print("or if you just wanna talk to me to make your mood light...")
print("simply say hello alexa or press 3")
pyobj.say("or if you just wanna talk to me to make your mood light")
pyobj.runAndWait()
pyobj.say("simply say hello alexa or press 3")
pyobj.runAndWait()

a = input()

if int(a) == 2:
    print("okay")
    pyobj.say("okay")
    pyobj.runAndWait()
    print("then why you called me?....HUH!!!")
    pyobj.say("then why you called me?...huh")
    pyobj.runAndWait()
    print("ajeeb aadmi hai")
    pyobj.say("ajeeb aadmi hai")
    pyobj.runAndWait()

elif int(a) == 3:
    print("hello there")
    pyobj.say("hello there")
    pyobj.runAndWait()
    print("nice to see you ")
    pyobj.say("nice to see you")
    pyobj.runAndWait()
    print("by the way who is there ???")
    pyobj.say("by the way who is there")
    pyobj.runAndWait()
    name = input()

    if name not in l:
        print("oh saw you here for the first time!never met you before")
        pyobj.say("oh saw you here for the first time!...never met you before")
        pyobj.runAndWait()

    else:
        if name == "rounak":
            print(" i found two identities with the given name in my memory!")
            print("please specify if it is rounak raj or rounak sahni ")
            pyobj.say("i found two identities with the given name in my memory! please specify if it is rounak raj or raunak sahni")
            pyobj.runAndWait()
            n2 = input()

    print("nice to see u ")
    print("how is the life going on ", name, "?")
    pyobj.say("nice to see you.how is the life going on",name)
    pyobj.runAndWait()
    lfeel = input().split()
    for feel in lfeel:
        if feel in gfeel:
            question = [1, 2, 3]
            print("oh touchwood...may god bless u always ")
            pyobj.say("oh touchwood...may god bless u always")
            pyobj.runAndWait()
            computer = random.choice(question)
            if question == 1:
                print("so,how is your family?")
                pyobj.say("so ,how is your family?")
                pyobj.runAndWait()
                ans = input()
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()
            elif question == 2:
                print("how is your job going on?")
                pyobj.say("how is your job going on?")
                pyobj.runAndWait()
                ans = input()
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()
            else:
                print("how was the day buddy?")
                pyobj.say("how was the day buddy?")
                pyobj.runAndWait()
                ans = input()
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()

            print("so do you want me to play a relaxing happy song for you?")
            pyobj.say("so do you want me to play a relaxing happy song for you?")
            pyobj.runAndWait()
            s = input()
            if s == "yes":
                print("do you want me to play this track on youtube or mp3")
                pyobj.say("do you want me to play this track on youtube or mp3?")
                pyobj.runAndWait()
                k = input("enter youtube or mp3")
                if k == "youtube":
                    pywhatkit.playonyt("sooraj ki baaho main")
                else:
                    playsound("//Users//rudraksh//Downloads//Sooraj Ki Baahon Mein - Zindagi Na Milegi Dobara 320 Kbps.mp3")

            else:
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()
            print("so do your want me to do anything else???")
            pyobj.say("so do you want me to do anything else?")
            pyobj.runAndWait()
            el = input()
            if el == "no":
                print("okay!!")
                print("going to sleep")
                print("DON'T DISTURB")
                pyobj.say("okay...going to sleep.don't disturb")
                pyobj.runAndWait()
            # else:   idhr neeche waala saara copy hoga :pehle neeche ka complete krke fir copymario
            else:
                print("\n Just ask..")
                print("play music,\n send whatsapp message,\n play a youtube video,\n search on google,\n play games..")

                pyobj.say("just ask..play music,send watsapp message,play a youtube video,search on google,play games")
                pyobj.runAndWait()
                print("press 1- for sending a whatsapp message")
                time.sleep(1)
                print("press 2- for youtube videos")
                time.sleep(1)
                print("press 3- for google search")
                time.sleep(1)
                print("press 4- for offline downlaoded music")
                time.sleep(1)
                print("press 5- for playing games")
                time.sleep(1)

                pyobj.say("please enter yur choice")
                pyobj.runAndWait()
                b = int(input("enter your choice"))

                if b == 1:
                    pyobj.say("please enter the correct details below")
                    pyobj.runAndWait()
                    num = input("please enter the number with country code:")
                    msg = input("please type the message to be sent:")
                    hour = int(input("please enter the scheduled hour:"))
                    minute = int(input("please enter the scheduled minute:"))
                    pyobj.say("please wait a second...")
                    pyobj.runAndWait()
                    print("please wait a second")
                    pywhatkit.sendwhatmsg(num, msg, hour, minute)

                elif b == 2:
                    pyobj.say("enter the video topic ")
                    pyobj.runAndWait()
                    topic = input("enter the video topic:")
                    pywhatkit.playonyt(topic)  # you can even add a url

                elif b == 3:
                    pyobj.say("please enter the topic to be searched")
                    pyobj.runAndWait()
                    search = input("please enter the topic to be searched")
                    pywhatkit.search(search)

                elif b == 4:
                    print("No internet!!!")
                    pyobj.say("no internet")
                    pyobj.runAndWait()
                    print("NO WORRIES")
                    pyobj.say("no worries")
                    pyobj.runAndWait()
                    print("alexa has the feature to play the predownloaded songs when you are offline")
                    pyobj.say("alexa has the feature to play the predownloaded songs when you are offline")
                    pyobj.runAndWait()

                    print("following is the list of music downloaded in your system")
                    print("1.bandeya re bandeya")
                    print("2.bewafa nikli haaye tu")
                    print("3.sooraj ki baaho mein")
                    print("4.pocket mai rocket")
                    print("5.ae bhai zra dekhke chlo")

                    c = int(input("enter the corresponding song number "))
                    if c == 1:
                        playsound("//Users//rudraksh//Downloads//new_128_05 - Simmba (2018) - Bandeya Rey Bandeya.mp3")
                    elif c == 2:
                        playsound("//Users//rudraksh//Downloads//Bewafa-Nikli-Hai-Tu_192(PaglaSongs).mp3")
                    elif c == 3:
                        playsound("//Users//rudraksh//Downloads//Sooraj Ki Baahon Mein - Zindagi Na Milegi Dobara 320 Kbps.mp3")
                    elif c == 4:
                        playsound("//Users//rudraksh//Downloads//Pocket Mein Rocket - Rocket Singh - Salesman Of The Year 128 Kbps.mp3")
                    elif c == 5:
                        playsound("//Users//rudraksh//Downloads//Ae Bhai Zara Dekh Ke Chalo - Mera Naam Joker 128 Kbps.mp3")



                elif b == 5:
                    print("WELCOME TO THE GAME PARK")
                    pyobj.say("welcome to the game park")
                    pyobj.runAndWait()
                    print()
                    print("which game do you want to play?")
                    print("press 1 for stone,paper,scissors")
                    print("press 2 for  guessing the number")
                    pyobj.say("which game do you want to play?  press 1 for stone paper scissors and press 2 for guessing the number games")
                    pyobj.runAndWait()

                    d = int(input("enter the game you like to play "))

                    if d == 1:
                        print("WELCOME ", end="")
                        time.sleep(1)
                        print("to ", end="")
                        time.sleep(1)
                        print("the ", end="")
                        time.sleep(1)
                        print("STONE, ", end="")
                        time.sleep(1)
                        print("PAPER ", end="")
                        time.sleep(1)
                        print("AND SCISSOR")
                        time.sleep(2)
                        print()
                        print()

                        while True:
                            player = input("Enter a choice (rock, paper, scissors): ")
                            actionpossible = ["rock", "paper", "scissors"]
                            computer = random.choice(actionpossible)
                            time.sleep(1)
                            print("\nYou chose", player, "computer chose", computer)

                            if player == computer:
                                print("Both players selected ", player, ". It's a tie!")
                            elif player == "rock":
                                if computer == "scissors":
                                    pyobj.say("i chose scissiors")
                                    pyobj.runAndWait()
                                    print("Rock smashes scissors! You win!")
                                    playsound("//Users//rudraksh//Downloads//")

                                else:
                                    pyobj.say("i chose paper")
                                    pyobj.runAndWait()
                                    print("Paper covers rock! You lose.")
                                    playsound("//Users//rudraksh//Downloads//")

                            elif player == "paper":
                                if computer == "rock":
                                    pyobj.say("i chose rock")
                                    pyobj.runAndWait()
                                    print("Paper covers rock! You win!")
                                    playsound("//Users//rudraksh//Downloads//")
                                else:
                                    pyobj.say("i chose scissors")
                                    pyobj.runAndWait()
                                    print("Scissors cuts paper! You lose.")
                                    playsound("//Users//rudraksh//Downloads//")
                            elif player == "scissors":
                                if computer == "paper":
                                    pyobj.say("i chose paper")
                                    pyobj.runAndWait()
                                    print("Scissors cuts paper! You win!")
                                    playsound("//Users//rudraksh//Downloads//")
                                else:
                                    pyobj.say("i chose rock")
                                    pyobj.runAndWait()
                                    print("Rock smashes scissors! You lose.")
                                    playsound("//Users//rudraksh//Downloads//")
                            time.sleep(1)
                            play_again = input("Play again? (y/n): ")
                            if play_again.lower() == "n":
                                time.sleep(1)
                                print("THANKS FOR PLAYING")
                                pyobj.say("thanks for playing")
                                pyobj.runAndWait()
                                break


                    elif d == 2:
                        print("WELCOME ", end="")
                        time.sleep(1)
                        print("to ", end="")
                        time.sleep(1)
                        print("the ", end="")
                        time.sleep(1)
                        print("NUMBER ", end="")
                        time.sleep(1)
                        print("GUESSING ", end="")
                        time.sleep(1)
                        print("GAME")
                        time.sleep(2)
                        print()
                        print()
                        print("you have to enter a number between 1-100")
                        print("if the number you entered matches the random number generated by computer ,")
                        print("you will win")
                        pyobj.say("you have to enter a number between 1 to 100. if the number you entered matches the random number generated by the computer,you will win")
                        pyobj.runAndWait()
                        print("you will get 10 chances !!! ALL THE BEST")
                        pyobj.say("you will get 10 chances ,all the best")
                        pyobj.runAndWait()
                        j = 0
                        while True:
                            g = random.randint(1, 100)

                            i = 10
                            while i > 0:
                                h = int(input("enter a number between 1-100"))
                                pyobj.say("enter a number between 1 to 100")
                                pyobj.runAndWait()
                                if g == h:
                                    print("you guessed it right")
                                    print("you win")
                                    pyobj.say("you guessed it right,you win")
                                    pyobj.runAndWait()
                                    break
                                elif h > g:
                                    print("enter a lower number")
                                    pyobj.say("enter a lower number")
                                    pyobj.runAndWait()
                                else:
                                    print("enter a greater number")
                                    pyobj.say("enter a greater number")
                                    pyobj.runAndWait()
                                i = i - 1
                                if i == 0:
                                    print("you lose")
                                    pyobj.say("you lose")
                                    pyobj.runAndWait()
                                    break

                            play_again = input("Play again? (y/n): ")
                            if play_again.lower() == "n":
                                time.sleep(1)
                                print("THANKS FOR PLAYING")
                                pyobj.say("thanks for playing")
                                pyobj.runAndWait()
                                break


        elif feel in bfeel:
            print("what happened", name, "?")
            print("don't hesitate to tell me")
            pyobj.say("what happened? don't hesitate to tell me")
            pyobj.runAndWait()
            i = input()
            time.sleep(1)
            print("tell me the whole thing ")
            pyobj.say("tell me the whole thing")
            pyobj.runAndWait()
            print("believe me i am good at keeping secrets")
            pyobj.say("believe me i am good at keeping secrets")
            pyobj.runAndWait()
            # now your will enter your bad experience in few lines or words and dont forget the key words
            l = input().split()
            time.sleep(1)
            print("ahh")
            print("don't worry")
            print("everything will be alright")
            pyobj.say("aah...don't worry...everything will be alright")
            pyobj.runAndWait()
            for i in l:
                if i in feelm:
                    print("so do you want me to play a song for you")
                    pyobj.say("so do you want me to play a song for you")
                    pyobj.runAndWait()
                    inp = input()
                    if inp == "yes":
                        print("okay.let me play some music for you that can make you feel better ")
                        pyobj.say("okay let me play some music for you that can make you  feel better")
                        pyobj.runAndWait()
                        if i == "gf" or i == "wife" or i == "girlfriend" or i == "breakup":
                            print("do you want me to play this track on youtube or mp3")
                            pyobj.say("do you want me to play this track on youtube or mp3")
                            pyobj.runAndWait()
                            k = input("enter youtube or mp3")
                            if k == "youtube":
                                pywhatkit.playonyt("bewafa nikli haye tu")
                            else:
                                playsound("//Users//rudraksh//Downloads//Bewafa-Nikli-Hai-Tu_192(PaglaSongs).mp3")
                            break
                        elif i == "job":
                            print("do you want me to play this track on youtube or mp3")
                            pyobj.say("do you want me to play this track on youtube or mp3")
                            pyobj.runAndWait()
                            k = input("enter youtube or mp3")
                            if k == "youtube":
                                pywhatkit.playonyt("pocket mai rocket hai")
                            else:
                                playsound("//Users//rudraksh//Downloads//Pocket Mein Rocket - Rocket Singh - Salesman Of The Year 128 Kbps.mp3")
                            break
                        elif i == "pain" or i == "accident":
                            print("do you want me to play this track on youtube or mp3")
                            pyobj.say("do you want me to play this track on youtube or mp3")
                            pyobj.runAndWait()
                            k = input("enter youtube or mp3")
                            if k == "youtube":
                                pywhatkit.playonyt("ae bhai zara dekhke chlo")
                            else:
                                playsound("//Users//rudraksh//Downloads//Ae Bhai Zara Dekh Ke Chalo - Mera Naam Joker 128 Kbps.mp3")
                            break     # ae bhai jra dekhke chlo ...aage hee nhi  neeche bhi
                        elif i == "study":
                            print("do you want me to play this track on youtube or mp3")
                            pyobj.say("do  you want me to play this track on youtube or mp3")
                            pyobj.runAndWait()
                            k = input("enter youtube or mp3")
                            if k == "youtube":
                                pywhatkit.playonyt("give me some sunshine")
                            else:
                                playsound("//Users//rudraksh//Downloads//Give Me Some Sunshine 128 Kbps.mp3")
                            break
                        elif i == "stress" or i == "tension" or i == "tensions" or i == "problem" or i == "problems":
                            print("do you want me to play this track on youtube or mp3")
                            pyobj.say("do you want me to play this track on youtube or mp3")
                            pyobj.runAndWait()
                            k = input("enter youtube or mp3")
                            if k == "youtube":
                                pywhatkit.playonyt("give me some sunshine")
                            else:
                                playsound("//Users//rudraksh//Downloads//Give Me Some Sunshine 128 Kbps.mp3")
                        elif i == "money" or i == "financial" or i == "no money":
                            print("do byou want me to play this track on youtube or mp3")
                            k = input("enter youtube or mp3")
                            if k == "youtube":
                                pywhatkit.playonyt("lakkhan da vi reha na swaad mitro jo ik sikke  naal aaunda si ")
                            else:
                                playsound("//Users//rudraksh//Downloads//")

            else:
                playsound("//Users//rudraksh//Downloads//new_128_05 - Simmba (2018) - Bandeya Rey Bandeya.mp3")
                print("so do you want me to do anything else???")
                pyobj.say("so do you want me to do anything else???")
                pyobj.runAndWait()
                el = input()
                if el == "no":
                    print("okay!!")
                    pyobj.say("okay")
                    pyobj.runAndWait()
                    print("if you want me")
                    pyobj.say("if you want me")
                    pyobj.runAndWait()
                    print("call me anytime again")
                    pyobj.say("call me anytime again")
                    pyobj.runAndWait()
                    # else:   idhr neeche waala saara copy hoga :pehle neeche ka complete krke fir copymario

                else:
                    print("\n Just ask..")
                    print("play music,\n send whatsapp message,\n play a youtube video,\n search on google,\n play games..")
                    pyobj.say("just ask.play music,send whatsapp message,play a youtube video,search on google,play games")
                    pyobj.runAndWait()

                    print("press 1- for sending a whatsapp message")
                    time.sleep(1)
                    print("press 2- for youtube videos")
                    time.sleep(1)
                    print("press 3- for google search")
                    time.sleep(1)
                    print("press 4- for offline downlaoded music")
                    time.sleep(1)
                    print("press 5- for playing games")
                    time.sleep(1)

                    pyobj.say("enter your choice")
                    pyobj.runAndWait()
                    b = int(input("enter your choice"))
                    time.sleep(1)

                    if b == 1:
                        pyobj.say("enter the following details correctly")
                        pyobj.runAndWait()
                        num = input("please enter the number with country code:")
                        msg = input("please type the message to be sent:")
                        hour = int(input("please enter the scheduled hour:"))
                        minute = int(input("please enter the scheduled minute:"))

                        pywhatkit.sendwhatmsg(num, msg, hour, minute)

                    elif b == 2:
                        pyobj.say("enter the video topic ")
                        pyobj.runAndWait()
                        topic = input("enter the video topic:")
                        pywhatkit.playonyt(topic)  # you can even add a url

                    elif b == 3:
                        pyobj.say("please enter the topic to be searched")
                        pyobj.runAndWait()
                        search = input("please enter the topic to be searched")
                        pywhatkit.search(search)

                    elif b == 4:
                        print("No internet!!!")
                        pyobj.say("no internet")
                        pyobj.runAndWait()
                        print("NO WORRIES")
                        pyobj.say("no worries")
                        pyobj.runAndWait()
                        print("alexa has the feature to play the predownloaded songs when you are offline")
                        pyobj.say("alexa has the feature to play the predownloaded songs when you are offline")
                        pyobj.runAndWait()

                        print("following is the list of music downloaded in your system")
                        print("1.bandeya re bandeya")
                        print("2.bewafa nikli haaye tu")
                        print("3.sooraj ki baaho mein")
                        print("4.pocket mai rocket")
                        print("5.ae bhai zra dekhke chlo")

                        c = int(input("enter the corresponding song number "))
                        if c == 1:
                            playsound("//Users//rudraksh//Downloads//new_128_05 - Simmba (2018) - Bandeya Rey Bandeya.mp3")
                        elif c == 2:
                            playsound("//Users//rudraksh//Downloads//Bewafa-Nikli-Hai-Tu_192(PaglaSongs).mp3")
                        elif c == 3:
                            playsound("//Users//rudraksh//Downloads//Sooraj Ki Baahon Mein - Zindagi Na Milegi Dobara 320 Kbps.mp3")
                        elif c == 4:
                            playsound("//Users//rudraksh//Downloads//Pocket Mein Rocket - Rocket Singh - Salesman Of The Year 128 Kbps.mp3")
                        elif c == 5:
                            playsound("//Users//rudraksh//Downloads//Ae Bhai Zara Dekh Ke Chalo - Mera Naam Joker 128 Kbps.mp3")

                    elif b == 5:
                        print("WELCOME TO THE GAME PARK")
                        pyobj.say("welcome to the game park")
                        pyobj.runAndWait()
                        print()
                        print("which game do you want to play?")
                        pyobj.say("which game do you want to play?")
                        pyobj.runAndWait()
                        print("press 1 for stone,paper,scissors")
                        print("press 2 for  guessing the number")
                        pyobj.say("press 1 for stone,paper,scissors and press 2 for guessing the number game ")
                        pyobj.runAndWait()

                        d = int(input("enter the game you like to play "))

                        if d == 1:
                            print("WELCOME ", end="")
                            time.sleep(1)
                            print("to ", end="")
                            time.sleep(1)
                            print("the ", end="")
                            time.sleep(1)
                            print("STONE, ", end="")
                            time.sleep(1)
                            print("PAPER ", end="")
                            time.sleep(1)
                            print("AND SCISSOR")
                            time.sleep(2)
                            print()
                            print()

                            while True:
                                player = input("Enter a choice (rock, paper, scissors): ")
                                actionpossible = ["rock", "paper", "scissors"]
                                computer = random.choice(actionpossible)
                                time.sleep(1)
                                print("\nYou chose", player, "computer chose", computer)

                                if player == computer:
                                    print("Both players selected ", player, ". It's a tie!")
                                elif player == "rock":
                                    if computer == "scissors":
                                        pyobj.say("i chose scissors")
                                        pyobj.runAndWait()
                                        print("Rock smashes scissors! You win!")
                                        playsound("//Users//rudraksh//Downloads//success-fanfare-trumpets-6185.mp3")

                                    else:
                                        pyobj.say("i chose paper")
                                        pyobj.runAndWait()
                                        print("Paper covers rock! You lose.")
                                        playsound("//Users//rudraksh//Downloads//mixkit-circus-lose-2030.wav")

                                elif player == "paper":
                                    if computer == "rock":
                                        pyobj.say("i chose rock")
                                        pyobj.runAndWait()
                                        print("Paper covers rock! You win!")
                                        playsound("//Users//rudraksh//Downloads//success-fanfare-trumpets-6185.mp3")
                                    else:
                                        pyobj.say("i chose paper")
                                        pyobj.runAndWait()
                                        print("Scissors cuts paper! You lose.")
                                        playsound("//Users//rudraksh//Downloads//mixkit-circus-lose-2030.wav")
                                elif player == "scissors":
                                    if computer == "paper":
                                        pyobj.say("i chose paper")
                                        pyobj.runAndWait()
                                        print("Scissors cuts paper! You win!")
                                        playsound("//Users//rudraksh//Downloads//success-fanfare-trumpets-6185.mp3")
                                    else:
                                        pyobj.say("i chose rock")
                                        pyobj.runAndWait()
                                        print("Rock smashes scissors! You lose.")
                                        playsound("//Users//rudraksh//Downloads//mixkit-circus-lose-2030.wav")
                                time.sleep(1)
                                play_again = input("Play again? (y/n): ")
                                if play_again.lower() == "n":
                                    time.sleep(1)
                                    print("THANKS FOR PLAYING")
                                    pyobj.say("thanks for playing")
                                    pyobj.runAndWait()
                                    break


                        elif d == 2:
                            print("WELCOME ", end="")
                            time.sleep(1)
                            print("to ", end="")
                            time.sleep(1)
                            print("the ", end="")
                            time.sleep(1)
                            print("NUMBER ", end="")
                            time.sleep(1)
                            print("GUESSING ", end="")
                            time.sleep(1)
                            print("GAME")
                            time.sleep(2)
                            print()
                            print()
                            print("you have to enter a number between 1-100")
                            pyobj.say("you have to enter a number bbetween 1 to  100")
                            pyobj.runAndWait()
                            print("if the number you entered matches the random number generated by computer ,")
                            pyobj.say("if the number you entered  matches the random number generated by computer")
                            pyobj.runAndWait()
                            print("you will win")
                            pyobj.say("you will win")
                            pyobj.runAndWait()
                            print("you will get 10 chances !!! ALL THE BEST")
                            pyobj.say("you will get 10 chances!! all the best")
                            pyobj.runAndWait()

                            while True:
                                g = random.randint(1, 100)

                                i = 10
                                while i > 0:
                                    h = int(input("enter a number between 1-100"))
                                    if g == h:
                                        print("you guessed it right")
                                        print("you win")
                                        pyobj.say("you guessed it right , you win")
                                        pyobj.runAndWait()
                                        break
                                    elif h > g:
                                        print("enter a lower number")
                                    else:
                                        print("enter a greater number")
                                    i = i - 1
                                    if i == 0:
                                        print("you lose")
                                        pyobj.say("you lose")
                                        pyobj.runAndWait()
                                        break

                                play_again = input("Play again? (y/n): ")
                                if play_again.lower() == "n":
                                    time.sleep(1)
                                    print("THANKS FOR PLAYING")
                                    pyobj.say("thanks for playing")
                                    pyobj.runAndWait()
                                    break





        else:
            print("i don't understand that")
            pyobj.say("i don't understand that")
            pyobj.runAndWait()
            print("please tell in some simple words or explain it more")
            pyobj.say("please tell in some simple words or explain it more")
            pyobj.runAndWait()
            print("after all i am a robot")
            pyobj.say("after all i am a robot")
            pyobj.runAndWait()


else:
    print("\n Just ask..")
    print("play music,\n send whatsapp message,\n play a youtube video,\n search on google,\n play games..")
    pyobj.say("just ask...play music...send watsapp message...play a youtube video...search on google...play games")
    pyobj.runAndWait()

    print("press 1- for sending a whatsapp message")
    time.sleep(1)
    print("press 2- for youtube videos")
    time.sleep(1)
    print("press 3- for google search")
    time.sleep(1)
    print("press 4- for offline downlaoded music")
    time.sleep(1)
    print("press 5- for playing games")
    time.sleep(1)

    pyobj.say("enter your choice")
    pyobj.runAndWait()
    b = int(input("enter your choice"))
    time.sleep(1)

    if b == 1:
        pyobj.say("please enter the below details correctly")
        pyobj.runAndWait()
        num = input("please enter the number with country code:")
        msg = input("please type the message to be sent:")
        hour = int(input("please enter the scheduled hour:"))
        minute = int(input("please enter the scheduled minute:"))

        pywhatkit.sendwhatmsg(num, msg, hour, minute)

    elif b == 2:
        pyobj.say("enter he video topic")
        pyobj.runAndWait()
        topic = input("enter the video topic:")
        pywhatkit.playonyt(topic)  # you can even add a url

    elif b == 3:
        pyobj.say("please enter the topic to be searched ")
        pyobj.runAndWait()
        search = input("please enter the topic to be searched")
        pywhatkit.search(search)

    elif b == 4:
        print("No internet!!!")
        pyobj.say("no internet")
        pyobj.runAndWait()
        print("NO WORRIES")
        pyobj.say("no worries")
        pyobj.runAndWait()
        print("alexa has the feature to play the predownloaded songs when you are offline")
        pyobj.say("alexa has the feature to play the predownloaded songs when you are offline")
        pyobj.runAndWait()

        print("following is the list of music downloaded in your system")
        print("1.bandeya re bandeya")
        print("2.bewafa nikli haaye tu")
        print("3.sooraj ki baaho mein")
        print("4.pocket mai rocket")
        print("5.ae bhai zra dekhke chlo")

        c = int(input("enter the corresponding song number "))
        if c == 1:
            playsound("//Users//rudraksh//Downloads//new_128_05 - Simmba (2018) - Bandeya Rey Bandeya.mp3")
        elif c == 2:
            playsound("//Users//rudraksh//Downloads//Bewafa-Nikli-Hai-Tu_192(PaglaSongs).mp3")
        elif c == 3:
            playsound("//Users//rudraksh//Downloads//Sooraj Ki Baahon Mein - Zindagi Na Milegi Dobara 320 Kbps.mp3")
        elif c == 4:
            playsound("//Users//rudraksh//Downloads//Pocket Mein Rocket - Rocket Singh - Salesman Of The Year 128 Kbps.mp3")
        elif c == 5:
            playsound("//Users//rudraksh//Downloads//Ae Bhai Zara Dekh Ke Chalo - Mera Naam Joker 128 Kbps.mp3")


    elif b == 5:
        print("WELCOME TO THE GAME PARK")
        pyobj.say("welcome to the game park")
        pyobj.runAndWait()
        time.sleep(1)
        print()
        print("which game do you want to play?")
        print("press 1 for stone,paper,scissors")
        print("press 2 for  guessing the number")

        pyobj.say("enter the game you like to play")
        pyobj.runAndWait()
        d = int(input("enter the game you like to play "))

        if d == 1:
            print("WELCOME ", end="")
            time.sleep(1)
            print("to ", end="")
            time.sleep(1)
            print("the ", end="")
            time.sleep(1)
            print("STONE, ", end="")
            time.sleep(1)
            print("PAPER ", end="")
            time.sleep(1)
            print("AND SCISSOR")
            time.sleep(2)
            print()
            print()

            while True:
                player = input("Enter a choice (rock, paper, scissors): ")
                actionpossible = ["rock", "paper", "scissors"]
                computer = random.choice(actionpossible)
                time.sleep(1)
                print("\nYou chose", player, "computer chose", computer)

                if player == computer:
                    print("Both players selected ", player, ". It's a tie!")
                elif player == "rock":
                    if computer == "scissors":
                        pyobj.say("i  chose scissors")
                        pyobj.runAndWait()
                        print("Rock smashes scissors! You win!")
                        playsound("//Users//rudraksh//Downloads//success-fanfare-trumpets-6185.mp3")

                    else:
                        pyobj.say("i chose paper")
                        pyobj.runAndWait()
                        print("Paper covers rock! You lose.")
                        playsound("//Users//rudraksh//Downloads//mixkit-circus-lose-2030.wav")

                elif player == "paper":
                    if computer == "rock":
                        pyobj.say("i chose rock")
                        pyobj.runAndWait()
                        print("Paper covers rock! You win!")
                        playsound("//Users//rudraksh//Downloads//success-fanfare-trumpets-6185.mp3")
                    else:
                        pyobj.say("i chose scissors")
                        pyobj.runAndWait()
                        print("Scissors cuts paper! You lose.")
                        playsound("//Users//rudraksh//Downloads//mixkit-circus-lose-2030.wav")
                elif player == "scissors":
                    if computer == "paper":
                        pyobj.say("i chose paper")
                        pyobj.runAndWait()
                        print("Scissors cuts paper! You win!")
                        playsound("//Users//rudraksh//Downloads//success-fanfare-trumpets-6185.mp3")
                    else:
                        pyobj.say("i chose rock")
                        pyobj.runAndWait()
                        print("Rock smashes scissors! You lose.")
                        playsound("//Users//rudraksh//Downloads//mixkit-circus-lose-2030.wav")
                time.sleep(1)
                play_again = input("Play again? (y/n): ")
                if play_again.lower() == "n":
                    time.sleep(1)
                    print("THANKS FOR PLAYING")
                    pyobj.say("thanks for playing")
                    pyobj.runAndWait()
                    break


        elif d == 2:
            print("WELCOME ", end="")
            time.sleep(1)
            print("to ", end="")
            time.sleep(1)
            print("the ", end="")
            time.sleep(1)
            print("NUMBER ", end="")
            time.sleep(1)
            print("GUESSING ", end="")
            time.sleep(1)
            print("GAME")
            time.sleep(2)
            print()
            print()
            print("you have to enter a number between 1-100")
            pyobj.say("you have to enter a number between 1 to 100")
            pyobj.runAndWait()
            print("if the number you entered matches the random number generated by computer ,")
            pyobj.say("if the number you entered matches the random number generated by the computer,")
            pyobj.runAndWait()
            print("you will win")
            pyobj.say("you will win")
            pyobj.runAndWait()
            print("you will get 10 chances !!! ALL THE BEST")
            pyobj.say("you will get 10 chances!!all the best")
            pyobj.runAndWait()

            while True:
                g = random.randint(1, 100)

                i = 10
                while i > 0:
                    h = int(input("enter a number between 1-100"))
                    if g == h:
                        print("you guessed it right")
                        pyobj.say("you guessed it right")
                        pyobj.runAndWait()
                        print("you win")
                        pyobj.say("you win")
                        pyobj.runAndWait()
                        break
                    elif h > g:
                        print("enter a lower number")
                    else:
                        print("enter a greater number")
                    i = i - 1
                    if i == 0:
                        print("you lose")
                        pyobj.say("you lose")
                        pyobj.runAndWait()
                        break

                play_again = input("Play again? (y/n): ")
                if play_again.lower() == "n":
                    time.sleep(1)
                    print("THANKS FOR PLAYING")
                    pyobj.say("thanks for playing")
                    pyobj.runAndWait()
                    break



