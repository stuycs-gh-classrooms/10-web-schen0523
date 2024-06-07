#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

def make_html(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</html>'
    return html




def make_form(question, radio_options):
    html = """
    <form action="version0.py" method="GET">"""
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

#PAGE 1
question1 = "It is 8:00 AM in the morning, and your alarm goes off. <br> Do you:"
options1 = ['Snooze, sleep for 5 more minutes', 'Get up and head to the train station!']
intro = '<h1> Y/N and the Chamber of Secrets </h1>\n<p> It is the day before your second year at Mugwarts Magical School for Troubled Kids. Your BFF has been MIA for the entire Summer. You’ve been depressed since you have not received a single owl, but it’s time to prepare for the new school year. Your train time is 9:00 AM tomorrow morning.</p><p>Zzzzzzz... </p>'
intro += make_form(question1, options1)
start = make_html('Mugwarts Magical School', intro)

#PAGE 2
data = cgi.FieldStorage()

question2 = 'Oh no! You woke up too late, and missed your train! Unfortunately, there’s only one train time every year. Or, you think of other ways to get to school. <br> Do you:'
options2 = ['Take your parents flying car', 'Send an owl to the Principle to get someone to come pick you up']
pg2 = '<h1>You Snooze, you Lose!</h1>'
pg2 += make_form(question2, options2)
pg3 = '<h1>Wow…Rebel</h1>\n<p>You took the magic car… but it broke down and you landed in the forbidden forest. After you get out, Ms Mcgonadald catches you and… YOU WERE EXPELLED!</p>'

if (len(data) != 0):
    if ('choices' in data):
        choice = data['choices'].value
    if choice == options1[0]:
        print(make_html('You Snooze, you Lose!',pg2))
    elif choice == options1[1]:
        pg3 += '<br><a href="version0.py">Try Again</a>'
        print(make_html('Wow…Rebel', pg3))
        
    
#if no form data, return the form html instead of result
else:
    print(start)

  



