import sendgrid

def sendEmail(emailAddress, emailBody):
    
    sg = sendgrid.SendGridClient('xenocars', 'cmsc411!')

    message = sendgrid.Mail()
    message.add_to([emailAddress])
    message.set_subject('[Xeno] Car Reservation')
    message.set_html(emailBody)
    message.set_text(emailBody)
    message.set_from('Xeno_Cars')
    status, msg = sg.send(message)
    
# OR

#    sg = sendgrid.SendGridClient('xenocars', 'cmsc411!')

#    message = sendgrid.Mail(to=['michaelsbishoff@gmail.com', 'cwong2@umbc.edu'], subject='[Xeno] Car Requested', html='You checked out a Lamborghini Gallardo 2015!', text='You checked out a Lamborghini Gallardo 2015!', from_email='Xeno Cars')
#    status, msg = sg.send(message)
    print "Email status: ", status
#    print "Message: ", msg
