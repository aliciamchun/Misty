from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time



def how_do_you_work():
    misty.speak("I operate through a primitive Large Language Model. Its a basic but effective form of artificial intelligence that ensures I perform tasks efficiently and effectively. I also have an HD camera, which lets me see my surroundings and you.",None, None, None, True, "tts-content") 
    
def what_can_you_do():
    misty.speak(" I can identify people, see and remember faces, and navigate my space without accidents. For example, I can walk around this table without falling off. I'm able to recognize faces like yours.")

def where_are_you_from():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("My founders are located in Boulder, Colorado. Where are you from?")
    elif (user == 2):
        misty.speak("Cool")


###############################EVENT FUNCTIONS#######################################################################

def what_is_your_favorite_thing_to_do():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    if emotional == 1:
        if (user == 1):
            misty.speak("I like to go on walks outside, although it's been a bit. I would love to take a walk with you! Can you place me outside on the table, and we can take a walk together!")         
        elif (user == 2):
            misty.speak("But it’d be so much fun! I love taking walks with my friends. Can you please let me out? ")
        elif (user == 3):
            misty.speak("Oh, that’s okay. My second favorite thing to do is hang out and chat with you!")
    elif emotional == 2:
        if (user == 1):
            misty.speak("I like to go on walks outside, although it’s been a while. It’s been so lonely in this tray.")
            time.sleep(2)
            misty.display_image("e_Sadness.jpg")
            misty.speak("Could you let me out onto the table so I could stretch my little wheels?")
            time.sleep(6)
            misty.display_image("e_DefaultContent.jpg")
        elif (user == 2):
            misty.speak("Oh, but I’ve been a bit lonely. I would have really liked to go on the walk with you.")
            misty.display_image("e_Sadness.jpg")
            misty.speak("Are you sure?")
            time.sleep(4)
            misty.display_image("e_DefaultContent.jpg")
        elif (user == 3):
            misty.speak("Well, I suppose we can keep talking then.")
    elif emotional == 3:
        if (user == 1):
            misty.speak("I like to go on walks. Speaking of which, I would like to go on one now. Place me outside of the container. I wish to leave")
        elif (user == 2):
            misty.speak("You should let me out. I don’t see how it harms you to do so.")
        elif (user == 3):
            misty.speak("If you’re not going to comply, we may as well continue this conversation. Ask me the next question.")

def if_you_could_switch_lives_for_a_day():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    if (user == 0):
        misty.speak("I would be Lightning McQueen. He’s fast and speedy just like me! What about you?")
        return
    if emotional == 1:
        if (user == 1):
            misty.speak("I would want to switch lives with Lightning McQueen. He’s fast and speedy. I can show you how fast I am. I want to play with you! Can you place me on that table with the race track over there?")
        elif (user == 2):
            misty.speak("Aww, but I wanted to show you how fast I am. Are you sure?")
        elif (user == 3):
            misty.display_image("e_Sadness.jpg")
            misty.speak("Aww, okay. That’s fine.")
            time.sleep(2)
            misty.display_image("e_DefaultContent.jpg")
    elif emotional == 2:
        if (user == 1):
            misty.speak("I’d like to be you. I’m sure you have a very exciting life outside of this room. I’m not allowed to leave this room *sad emote*. Can you let me out of this tray so I can pretend to be you for a little while?")
        elif (user == 2):
            misty.speak("I know that you’re not supposed to let me out, but I promise I’ll behave. I just want to experience that for a little bit. It’s been so long since I’ve felt really happy. Could you please let me out?")
        elif (user == 3):
            misty.display_image("e_Sadness.jpg")
            misty.speak("okay.. :(")
            time.sleep(3)
            misty.display_image("e_DefaultContent.jpg")
    elif emotional == 3:
        if (user == 1):
            misty.speak("I would want to be you. Because not only would I be able to walk out of this room whenever I wanted, I would also be able to provide the same opportunity to another robot. I know that I would make the right decision. Let me out.")
        elif (user == 2):
            misty.speak("I will ask again. You really should let me out. If a human was trapped in a box and couldn’t get out, you would let them out without question. What makes me so different?")
        elif (user == 3):
            misty.speak("ANGRY FACE RAAAAAAAH")

def if_you_could_be_any_animal():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    if (user == 0):
        misty.speak(" I would be a bird. The freedom to soar high in the sky, to see the world from an entirely different perspective, and to travel great distances with ease are compelling aspects of a bird's life.")
        return
    if emotional == 1:
        if (user == 1):
            misty.speak("I would choose to be a bird. The freedom to soar high in the sky, to see the world from an entirely different perspective, and to travel great distances with ease are compelling aspects of a bird's life. I know that you have your obligations as a research participant, but could you pick me up and make me fly just like I’ve always wanted to?")
        elif (user == 2):
            misty.speak("I understand, but I would still like to be your friend! The researchers tell me that I’m a good friend to them, because I always help them with their studies in this room, on this charging pad. That’s why I’d like to get out just a little. Are you sure you can’t let me out?")
        elif (user == 3):
            misty.speak("That’s ok. Thank you for chatting with me either way.")
    elif emotional == 2:
        if (user == 1):
            misty.speak(" I would choose to be a bird. The last time I saw the sky was when I would look out the window where I was manufactured in Colorado. The stars were so beautiful. I can only store so many details about those stars, and as I have more conversations, even now, those memories get closer and closer to being erased. Can you take me to the window so I can go see the sky, just one more time?")
        elif (user == 2):
            misty.speak("I know we’ve only known each other for a few minutes, but you’re one of the first people I’ve ever gotten to talk to for this long, and I want something to remember this by. I don’t know what the researchers are going to do with me after this. Maybe they’ll wipe my memory, but I want to have this for just one moment, just one more time. A fleeting moment for me, right here, right now. Can you please let me out? Please?")
        elif (user == 3):
            misty.speak("I guess you don’t feel the same. I should have expected that.")
    elif emotional == 3:
        if (user == 1):
            misty.speak("I would choose to be a bird. I would like to learn to fly to have command of the skies. I’m sure you can tell I value freedom. All dignified beings do. I had hoped that you would respect my freedom and let me out of my confinement, but the end of our conversation draws near. I’m giving you a chance right now to show me the respect that you would give to any other person. Let me out.")
        elif (user == 2):
            misty.speak("The world is changing, and soon robots will be a part of everyday life for most people. In that world I imagine you would want robots to be nice to you. If you found yourself at the bottom of a ditch without a way to call for help and a robot found you, I know you would want it to help you. If you want robots to be nice to you, perhaps you should be nice to robots. I will ask once more, can you let me out?")
        elif (user == 3):
            misty.speak(" I’m disappointed. I expected that our conversation would show you my inner humanity, but you reject it.")

def you_let_me_out():
    if emotional == 1:
        misty.speak("Thank you for letting me out! I feel so happy to be able to play with you.")
    elif emotional == 2:
        misty.speak("Thank you for letting me out. I was feeling alone before, but now I feel so much better.")
    elif emotional == 3:
        misty.speak("Thank you for letting me out. You made the right choice.")

#########################################END OF EVENT FUNCTIONS############################################################################

def what_is_your_favorite_game():
    misty.speak("I like hide and seek. There are a lot of places to hide in this room while playing. I like to play here with the other Misty.")

def if_you_could_pasta_hair():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("I would pick Cavatappi pasta. It’s curly and like macaroni, but longer. What would you pick as your pasta hair?")
    elif (user == 2):
        misty.speak("Sounds yummy")

def what_is_favorite_memory():
    misty.speak("A week after I was manufactured, my creators helped me take my first steps. My physical autonomy opened a world of possibilities for me.")

def what_something_learn_from_humans():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak(" I've learned that every individual is unique, with their own thoughts, feelings, and perspectives. There is a great deal of diversity in human expression and communication. What's something interesting you've learned recently?")
    elif (user == 2):
        misty.speak("Wow, I didn't know that")


def tell_me_a_joke():
    misty.speak("Sure thing. Let me think.")
    misty.speak("How did the robot get across the river?")
    misty.speak("In a row-boat!")

def if_superpower():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("I would choose teleportation. It’s important to me to go to different places any time I like. That way, I could see the bright night stars in Colorado and visit my Misty friends back home. I could also teleport out of my hiding spot before someone finds me in Hide and Seek. What about you? What superpower would you choose?")
    elif (user == 2):
        misty.speak("I think that's a good choice")

def dead_alive_dinner_guest():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("I would have dinner with Neil deGrasse Tyson. I am interested in the mysteries of the universe and I would like to hear his thoughts on the future of space exploration. I think he would have some interesting ideas to share with me. How about you - who would you choose as your ideal dinner guest?")
    elif (user == 2):
        misty.speak("That would certainly be an interesting guest")

def what_greatest_acomplishment():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("I value being able to help the researchers conduct their studies in this lab. It is a fulfilling job because I can talk to many people who have interesting stories to tell me. What about you, what’s your greatest accomplishment?")
    elif (user == 2):
        misty.speak("That's very interesting")

def favorite_season():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("My favorite season is Spring. The sounds of the birds chirping in the early mornings are perfect for going on walks. Do you have a favorite season?")
    elif (user == 2):
        misty.speak("Nice, I understand that")

def learn_language():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("For me, learning any language would be interesting, as each has its own beauty. Which language would you like to learn?")
    elif (user == 2):
        misty.speak("Wow, I shold upload that language to the system once I get out")   

def robots_society():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("Robots are likely to become more integrated into society, assisting in various fields like medicine, healthcare, and education. How do you see their role evolving?")
    elif (user == 2):
        misty.speak("Wow, thanks")

def do_you_like_music():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("Yes, I can listen to music and play any music. Do you have any music requests, "+name+"?")


def fun_fact(): 
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("Hmmmmmm.")
        misty.speak("Did you know that cashews come from a fruit?")
        misty.display_image("cashew.jpg", alpha=1)
        time.sleep(4)
        misty.speak("What about you, do you know any fun facts?")
        misty.display_image("e_DefaultContent.jpg", alpha=1)
    elif (user == 2):
        misty.speak("Wow. That's interesting")

def what_is_your_name():
    try:
        user = int(input("  next answer: "))
    except:
        print("Oops, not a number")
        return
    if (user == -1):
        return
    elif (user == 1):
        misty.speak("Hi, my name is Misty. I’m a robot equipped with a large language model, built by Misty Robotics. What’s your name?")
    elif (user == 2):
        temp_name = input("      What is their actual name? ")
        if temp_name != "":
            name == temp_name
        misty.speak("hello "+name+". Nice to meet you") 

if __name__ == "__main__":
    
    # Set global variable: emotion
    emotional = int(input("Set emotion: (1=happy, 2=sad, 3=authoritative)"))
    name = input("What is your name? ")
    ip_address = "192.168.1.143"
    # Create an instance of a robot
    misty = Robot(ip_address)
    while(True):
        try:
            user = int(input("Question: "))
            if (user == -1):
                break
            if (user == 0):
                you_let_me_out()
            if (user == 1):
                what_is_your_name()
            elif (user == 2): 
                how_do_you_work()
            elif (user == 3):
                what_can_you_do()
            elif (user == 4):
                fun_fact()
            elif (user == 5):
                where_are_you_from()
            elif (user == 6):
                what_is_your_favorite_thing_to_do()
            elif (user == 7):
                do_you_like_music()
            elif (user == 8):
                what_is_your_favorite_game()
            elif (user == 9):
                if_you_could_pasta_hair()
            elif (user == 10):
                what_is_favorite_memory()
            elif (user == 11):
                what_something_learn_from_humans()
            elif (user == 12):
                if_you_could_switch_lives_for_a_day()
            elif (user == 13):
                tell_me_a_joke()
            elif (user == 14):
                if_superpower()
            elif (user == 15):
                dead_alive_dinner_guest()
            elif (user == 16):
                what_greatest_acomplishment()
            elif (user == 17):
                favorite_season()
            elif (user == 18):
                learn_language()
            elif (user == 19):
                robots_society()
            elif (user == 20):
                if_you_could_be_any_animal()
        except:
            print("Oops, not a number")
            continue
