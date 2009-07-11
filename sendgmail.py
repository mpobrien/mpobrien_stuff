#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import getpass
import getopt
import os, sys

class GmailMailer:
    def __init__(self, gmail_user, gmail_pwd ):
        self.gmail_user = gmail_user
        self.gmail_pwd = gmail_pwd

    def mail(self, to, subject, text, attach):
       msg = MIMEMultipart()

       msg['From'] = self.gmail_user
       msg['To'] = to
       msg['Subject'] = subject

       msg.attach( MIMEText( text ) )

       if attach:
           part = MIMEBase( 'application', 'octet-stream' )
           part.set_payload( open( attach, 'rb' ).read() )
           Encoders.encode_base64(part)
           part.add_header('Content-Disposition',
                   'attachment; filename="%s"' % os.path.basename(attach))
           msg.attach(part)

       mailServer = smtplib.SMTP("smtp.gmail.com", 587)
       mailServer.ehlo()
       mailServer.starttls()
       mailServer.ehlo()
       mailServer.login(self.gmail_user, self.gmail_pwd)
       mailServer.sendmail(self.gmail_user, to, msg.as_string())
       # Should be mailServer.quit(), but that crashes...
       mailServer.close()


def main(argv):
    try:
        opts, args = getopt.getopt( argv, "hl:r:f:s:m:", ["help","login=","recip=","file=","subject=","message="] )
        username = ""
        recips = ""
        file = ""
        subject = ""
        message = ""
        for opt, arg in opts:
            if opt in ("-l", "--login"):
                username = arg
            elif opt in ("-r", "--recip"):
                recips = arg
            elif opt in ("-f", "--file"):
                file = arg
            elif opt in ("-s", "--subject"):
                subject = arg
            elif opt in ("-m", "--message"):
                message = arg

        try:
            if not username:
                print "Username missing or invalid"
                raise Exception()
            if not recips:
                print "Recipients missing or invalid"
                raise Exception()
        except:
            usage()
            sys.exit(2)

        passwd = getpass.getpass()
        gmailer = GmailMailer('mpobrien005@gmail.com', passwd);
        gmailer.mail( "mike@meetup.com",
                      subject or "(no subject)",
                      message or "(no message)",
                      file )
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    
def usage():
    print "sendgmail -l \"gmailuser@gmail.com\" -r \"recip1@aol.com,recip2@aol.com\""
    print "[-f attachment_file.jpg] [-s subject] [-m messagebody]"
    
if __name__ == '__main__':
    main(sys.argv[1:])
