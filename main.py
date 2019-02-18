from gmailIt.gmailIt import Email

clientId =  'mike@lemonshell.com'
to =        'mike@lemonshell.com'
subject =   'hello'
plain =     'world'
html =      '<b>world</b>'


email = Email(clientId, to, subject, plain, html)

try:
    status = email.send()
    print(f'Message Id: {status["id"]}')
except:
    print('Error')
