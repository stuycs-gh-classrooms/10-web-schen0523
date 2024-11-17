#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi
import random


f = open('characters.txt')
characters = f.read()
f.close()
characters = characters.split(', ')



def make_html(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    <link href="styles.css" rel="stylesheet">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</html>'
    return html


def make_form(question, radio_options):
    html = """
    <form action="main.py" method="GET">"""
    html += question
    html += """<br>"""

    radio = ''

    for option in radio_options:
        iput = '<div>'
        iput+= '<input type="radio" name="choices" value="' + option + '">'
        iput+= option + '</div>'
        radio+= iput

    html+= radio
    html+= '<input type="submit" value="Next">'
    return html

def make_name(question):
    html = """
    <form action="main.py" method="GET">"""
    html += question
    html += """<br><input type="text" name="name" value="Dolores Umbridge">
    <br>
    """
    html+= '<input type="submit" value="Submit">'
    return html

def make_friend(question, radio_options):
    html = """
    <form action="main.py" method="GET">"""
    html += question
    html += """<br>"""

    radio = ''

    for option in radio_options:
        iput = '<div>'
        iput+= '<input type="radio" name="friends" value="' + option + '">'
        iput+= option + '</div>'
        radio+= iput

    html+= radio
    html+= '<input type="submit" value="Next">'
    return html

def make_password(question):
    html = """
    <form action="main.py" method="GET">"""
    html += question
    html += """<br><input type="text" name="password" value="Mugwart">
    <br>
    """
    html+= '<input type="submit" value="Submit">'
    return html

def make_house(question, radio_options):
    html = """
    <form action="main.py" method="GET">"""
    html += question

    html += """<br>"""

    radio = ''
    for option in radio_options:
        iput = '<div>'
        iput+= '<input type="radio" name="house" value="' + option + '">'
        iput+= option + '</div>'
        radio+= iput

    html+= radio
    html+= '<input type="submit" value="Next">'
    return html

#PAGE0
pg0 = '<h1>Welcome to the world of Witchcraft and Wizardry!</h1>'
pg0 += make_name('What is your name?')
start = make_html('Begin', pg0)
# if (len(data) != 0):
#     if ('name' in data):
#         name = data['name'].value
#     body+= '<h1> Hello ' + name + '</h1>'
#     body+= '<br><a href="version0.py?choices=start"> Begin </a>'
#     html = make_html('Begin', body)
#     print(html)

#PAGE 1
question1 = "It is 8:00 AM in the morning, and your alarm goes off. <br> Do you:"
options1 = ['Snooze, sleep for 5 more minutes', 'Get up and head to the train station!']
intro = ' and the Chamber of Secrets </h1>\n<p> It is the day before your second year at Mugwarts Magical School for Troubled Kids. Your BFF has been MIA for the entire Summer. You’ve been depressed since you have not received a single owl, but it’s time to prepare for the new school year. Your train time is 9:00 AM tomorrow morning.</p><p>Zzzzzzz... </p>'
intro += make_form(question1, options1)
intro += "<br> (Don't leave any answer blank, otherwise it will reset the game.)"

def make_page1(names):
    body = '<h1>'
    body += names
    body += intro
    html = make_html('Mugwarts Magical School', body)
    return html

#PAGE 2
data = cgi.FieldStorage()

question2 = 'Oh no! You woke up too late, and missed your train! Unfortunately, there’s only one train time every year. Or, you think of other ways to get to school. <br> Do you:'
options2 = ["Take your parents' flying car", 'Send an owl to the Principal to get someone to come pick you up']
pg2 = '<h1>You Snooze, you Lose!</h1>'
pg2 += make_form(question2, options2)

#PAGE3
pg3 = '<h1>Wow…Rebel</h1>\n<p>You took the magic car… but it broke down and you landed in the forbidden forest. After you get out, Ms Mcgonagall catches you and… YOU WERE EXPELLED!</p>'
pg3 += 'The End...<br><a href="main.py">Try Again?</a>'

#PAGE4
pg4 = '<h1>Meet Hagrid!</h1>\n<p>Hagrid is sent to pick you up on his motorcycle. You get to school quickly in time for the big feast and to witness the new coming wizards and witches!</p>'
pg4 += '<a href="main.py?friends=Neville+Longbottom">Time for the Feast!</a>'

#PAGE5
pg5 = '<h1>On the Train</h1>\n<p>On the train, your BFF is nowhere to be seen. You walk through, and all the compartments are filled, except for 1.</p>'
question5 = 'Who do you choose to sit with?'
c = random.sample(characters,1)
options5 = str(c[0])

pg5 += "<p> You're forced to sit with " + options5 + ". They quickly become your new friend."
#pg5 += make_friend(question5, options5)
# pg5 += make_name('What is your name?')
pg5 += '<p>You talk for the remainder of the commute to Mugwarts Magical High School, and arrive at a big feast waiting for you.</p>'
pg5 += '<a href="main.py?friends=Neville+Longbottom">Time for the Feast!</a>'

#PAGE6
pg6 = '<h1>Time for a feast!</h1>'
question6 = "What house are you part of?(Hufflepuff doesn't exist for a reason.)"
options6 =['Gryffindor', 'Slytherin', 'Ravenclaw']
pg6 += make_house(question6, options6)

#PAGE7
pg7 = '<h1>Welcome to '
pg71 = '<h1>Welcome'
question7 = 'What is the password to the dorm?'
add = '<h1>A Few Weeks Later...</h1>\n<p>You, your roommate, and your friend are now a trio. Strange things have happened in school: <br> 1. People have been found petrified throughout the school.<br> 2. There’s bloody writing on the walls where the victims are found.</p>'


#add make password

#PAGE8
pg8 = '<h1>Someone new has just been found petrified.</h1>\n<p>Your trio wants to find out what’s been happening.</p>'
question8 = 'Do you:'
options8 = ['Analyze the writing on the wall', 'Wait for the victim to wake up','Search the victim’s dorm']
pg8 += make_form(question8, options8)

#PAGE9
pg9 = '<h1>The Writing on the Wall</h1>\n<p>The writing says: <br> “The Chamber of Secrets has been opened. Enemy of the heir beware” </p>'
question9 = 'What do you do?'
options9 = ['Ask Hagrid about the Chamber of Secrets', 'Ask Professor McGonagall about the Chamber of Secrets']
pg9 += make_form(question9, options9)

#PAGE10
pg10 = '<h1>Hagrid can’t Keep a Secret…</h1>\n<p>Hagrid tells you the history of the Chamber of Secrets, and how a muggle was killed when he was a student at Mugwarts. He tells you how to open the Chamber of Secrets, but he doesn’t know where it is.  He gives you a clue, telling you where the muggle was killed: “She was a hufflepuff, and she was found in the 3rd floor library.”</p>'
question10 = 'Where do you go to investigate?'
options10 = ['The 3rd floor library', 'The Hufflepuff common room', 'The bathroom next to the library']
pg10 += make_form(question10, options10)

#PAGE11
pg11 = '<h1>Where’s the entrance?</h1>\n<p>You go to the library, and there’s nothing suspicious. Your roommate starts scanning all of the books. There are three that stand out.</p>'
question11 = 'Which one should you investigate?'
options11 = ['The one with a serpent on the spine','The one with a dragon on the spine', 'The one with a bird on the spine']
pg11 += make_form(question11, options11)

#PAGE12
pg12 = '<h1>Error...</h1>\n<p>There was nothing useful in the book.</p>'
pg12 += '<br><a href="main.py?choices=The+3rd+floor+library">Try Another Book</a>'

#PAGE13
pg13 = '<h1>Open Sesame</h1>\n<p>You pulled on the book, and a staircase emerged! You and your friends follow it to a dark chamber. <br>Lumos!  <br>There are a hundred pixies carrying keys. Only one opens the door on the other side of the chamber. However, there are only two broomsticks for you to ride to find the key. </p>'
question13o = 'Who do you choose to come with you?'
options13o = ['Harry Potter', 'Your friend']
pg13 += make_form(question13o, options13o)
question13t = 'Which weapon do you choose to use?'
options13t = ['The Gryffindor Sword', 'A stone', 'Your Wand']


#PAGE14
pg14 = "<h1>You're Delusional... </h1>\n<p>Umm... Sorry but there is no Gryffindor Sword. The Dragon eats you and all your friends.</p>"
pg14 += 'The End...<br><a href="main.py">Try Again?</a>'
#PAGE15
pg15 = '<h1>Rock beats Scissors</h1>\n<p>Yay! You killed the dragon by stabbing its heart with the small but sharp pebble. You saved everyone, including your BFF.</p>'
pg15 += 'The End...<br><a href="main.py">Try Again?</a>'
#PAGE16
pg16 = '<h1>Finally using some magic…</h1>\n'
question16 = 'Which spell would you like to use? '
options16 = ['Incendio!','Petrificus Totalus!']
pg16 += make_form(question16, options16)

#PAGE17
pg17 = '<h1>Stop. Drop. and Roll</h1>\n<p>Incendio lit the dragon on fire, but it’s fireproof, and got super pissed. It instead lights your friend on fire… They die… Your other friend who went to get help arrives just in time for you to save yourself and your BFF. You saved the school, but at what cost? </p>'
pg17 += 'The End...<br><a href="main.py">Try Again?</a>'
#PAGE18
pg18 = '<h1>Clever, feed them their own Poison</h1>\n<p>You managed to petrify the beast! (How ironic!). Your friend who went to get help arrived to rescue everyone, and the teachers dealt with the dragon. You saved the school!</p>'
pg18 += 'The End...<br><a href="main.py">Try Again?</a>'
#PAGE19
pg19 = '<h1>Squeaky Clean</h1>\n<p>There’s nothing in the bathroom… </p>'
pg19 += '<br><a href="main.py?choices=Ask+Hagrid+about+the+Chamber+of+Secrets">Go Back</a>'
#PAGE20
pg20 = '<h1>No Trespassing!</h1>\n<p>You can’t get into the Hufflepuff common room, because you’re not a Hufflepuff! </p>'
pg20 += '<br><a href="main.py?choices=Ask+Hagrid+about+the+Chamber+of+Secrets">Go Back</a>'
#PAGE21
pg21 = '<h1>Isn’t it Past Curfew!? </h1>\n<p>Professor McGonagall does not want students to be snooping around. She is no help, so you find another solution.</p>'
pg21 += 'The End...<br><a href="main.py?choices=next1">Find Another Solution</a>'
#PAGE22
pg22 = '<h1>Password Please</h1>\n<p>The victim belongs to your dorm</p>'
question22 = 'What is the password to your dorm?(Capitalization does matter)'
pg22 += make_password(question22)
pg22 += '<br><a href="main.py?choices=Forgot+Password">Forgot Password</a>'
#add enter password and forgot password button

#PAGE23
pg23 = '<h1>You Forgot the Password!</h1>\n<p>You were stopped in your search, and could not find our what was happening. Mugwarts Magical High School was eaten by a dragon.</p>'
pg23 += 'The End...<br><a href="main.py">Try Again?</a>'
#add random number generator

#PAGE24
pg24 = '<h1>You’re in!</h1>\n<p>You, Harry Potter, and your friend search through the dorm.</p>'
pg24 += "<p> Harry finds the victim's diary. The diary details everything that the victim was doing before they were found petrified, including a story about the Chamber of Secrets. There is a crazy dragon that is waiting to break out. He also performs a spell to find a note with a location and a drawing of a dragon on it  </p>"
question24 = 'Do you:'
options24 = ['Ask Hagrid about the Chamber of Secrets','Go to the location', 'Give up because you don’t want to die', ]
pg24 += make_form(question24, options24)



#PAGE25
pg25 = "<h1>No one remembers the password!</h1>\n<p>Oh no… you couldn't get into your dorm, so you never figured out what happened. A large dragon shot out of the girls bathroom toilet and ended up killing everyone… MUGWARTS SCHOOL OF MAGIC IS DEAD…</p>"
pg25 += 'The End...<br><a href="main.py">Try Again?</a>'
#PAGE26
pg26 = '<h1>You Took too Long…</h1>\n<p>The Mandrakes, which are needed to cure the petrified, took too long to grow. A large dragon ended up getting loose in the school and killed everyone… MUGWARTS SCHOOL OF MAGIC IS DEAD… </p>'
pg26 += '<br><a href="main.py">Try Again?</a>'

#PAGE27
pg27 = "<h1>What a wimp!</h1>\n<p>You gave up because you were too scared...you couldn't uncover the truth.</p>"
pg27 += '<br><a href="main.py">Try Again?</a>'

def make_page3():
    html = make_html('Wow…Rebel', pg3)
    return html

def make_page4():
    html = (make_html('Meet Hagrid!', pg4))
    return html

def make_page2():
    html = make_html('You Snooze, you Lose!', pg2)
    return html

def make_page6():
    html = make_html('Time for a feast!', pg6)
    return html

def make_page5():
    html = make_html('On the Train', pg5)
    return html

def make_page71(house, body):

    title = 'Welcome to' + house + '!'
    body += house
    body += '!'
    body += '</h1>\n<p>After dinner, you go to your house’s dorm.</p>'
    body += "<br>Your password is DobbylovesMugwarts, be sure to remember this!<br>"
    body += "You've met your roommate, his name is Harry Potter, he's a pretty average guy.<br>"
    body += '<p>Zzzzzzz…</p><br>'
    body += "<a href='main.py?choices=next'>Next</a>"


    html = make_html(title, body)
    return html

def make_page73():
    html = make_html('A Few Weeks Later', add)
    html += "<a href='main.py?choices=next1'>Next</a>"
    return html

def make_page8():
    html = make_html('Someone new has just been found petrified', pg8)
    return html

def make_page9():
    html = make_html('The Writing on the Wall',pg9)
    return html
def make_page26():
    html = make_html('You Took too Long…', pg26)
    return html

def make_page10():
    html = make_html('Hagrid can’t Keep a Secret…', pg10)
    return html
def make_page21():
    html = make_html('Isn’t it Past Curfew!?', pg21)
    return html
def make_page11():
    html = make_html('Where’s the entrance?', pg11)
    return html

def make_page20():
    html = make_html('No Trespassing!', pg20)
    return html

def make_page19():
    html = make_html('Squeaky Clean', pg19)
    return html

def make_page12():
    html = make_html('Error...', pg12)
    return html

def make_page131():
    html = make_html('Open Sesame', pg13)
    return html
nochoose = ''
def make_page132(choose):
    body = '<h1>Open Sesame</h1>\n<p>'
    if choose == options13o[0]:
        nochoose = options13o[1]
    else:
        nochoose = options13o[0]
    body += nochoose
    body += ' stays behind, and goes to get more help. You and '
    body += choose
    body +=  ' continue on. You and '
    body += choose
    body += ' go into a larger chamber. Something eerie is happening… You see a figure lying on the ground, and you go closer. It’s your long lost BFF!!! Now, you must save your BFF by slaying the Dragon that is emerging from his slumber. </p>'
    body += make_form(question13t, options13t)
    html = make_html('Open Sesame', body)
    return html

def make_page14():
    html = make_html("You're Delusional...", pg14)
    return html

def make_page15():
    html = make_html('Rock beats Scissors', pg15)
    return html

def make_page16():
    html = make_html('Finally using some magic...', pg16)
    return html

def make_page17():
    html = make_html('Stop. Drop. and Roll.', pg17)
    return html

def make_page18():
    html = make_html('Clever, feed them their own Poison', pg18)
    return html

def make_page25():
    html = make_html('No one remembers the password!', pg25)
    return html

def make_page221():
    html = make_html('Password Please', pg22)
    return html

def make_page222(passwo):
    if passwo == 'DobbylovesMugwarts':
        return make_page24()
    else:
        return make_page221()

def make_page23():
    html = make_html('You Forgot the Password!',pg23)
    return html

def make_page24():
    html = make_html('You’re in!', pg24)
    return html

def make_page27():
    html = make_html('What a wimp!', pg27)
    return html




ans = ''
friend = ''
dorm = ''
passw = ''
n = ''

#START
if (len(data) != 0):
    if ('name' in data):
        n = data['name'].value
    elif ('choices' in data):
        ans = data['choices'].value
    elif ('friends' in data):
        friend = data['friends'].value
    elif ('house' in data):
        dorm = data['house'].value
    elif ('password' in data):
        passw = data['password'].value
    if len(n) != 0:
        print(make_page1(n))
    elif ans == options1[0]:
        print(make_page2())
    elif ans == options1[1]:
        print(make_page5())
    elif ans == options2[0]:
        print(make_page3())
    elif ans == options2[1]:
        print(make_page4())
    elif len(friend) != 0:
        print(make_page6())
    elif dorm == options6[0] or dorm == options6[1] or dorm == options6[2]:
        print(make_page71(dorm,pg7))
    elif ans == 'next':
        print(make_page73())
    elif ans == 'next1':
        print(make_page8())
    elif ans == options8[0]:
        print(make_page9())
    elif ans == options8[1]:
        print(make_page26())
    elif ans == options8[2]:
       print(make_page221())
    elif len(passw) != 0:
        print(make_page222(passw))
    elif ans == 'Forgot Password':
        print(make_page23())
    elif ans == options9[0]:
        print(make_page10())
    elif ans == options9[1]:
        print(make_page21())
    elif ans == options10[0] or ans == options24[1]:
        print(make_page11())
    elif ans == options10[1]:
        print(make_page20())
    elif ans == options10[2]:
        print(make_page19())
    elif ans == options11[0] or ans == options11[2]:
        print(make_page12())
    elif ans == options11[1]:
        print(make_page131())
    elif ans == options13o[0] or ans == options13o[1]:
        print(make_page132(ans))
    elif ans == options13t[0]:
        print(make_page14())
    elif ans == options13t[1]:
        print(make_page15())
    elif ans == options13t[2]:
        print(make_page16())
    elif ans == options16[0]:
        print(make_page17())
    elif ans == options16[1]:
        print(make_page18())
    elif ans == options24[2]:
        print(make_page27())

else:
    print(start)
