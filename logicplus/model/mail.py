import smtplib
import traceback
import sys

class mail:
    def SendMail(self, **mail):
        fromaddr = "vcr.student@gmail.com"
        password = "eclassroom"
        server_smtp = "smtp.gmail.com"

        try :
            server = smtplib.SMTP(server_smtp, 587)
            server.ehlo()
            server.starttls()
            server.login(fromaddr, password)
            email_text = """\  
            From: %s  
            To: %s  
            Subject: %s

            %s
            """ % (fromaddr, ", ".join(toaddrs), subject, body)
            server.sendmail(fromaddr, toaddrs, em)
            server.quit()
        except smtplib.SMTPServerDisconnected as disconnect:
            print("smtplib.SMTPServerDisconnected", disconnect)
        except smtplib.SMTPResponseException as smtpre:
            print("smtplib.SMTPResponseException: %s %s", (str(smtpre.smtp_code), str(smtpre.smtp_error)))
        except smtplib.SMTPSenderRefused as senderrefuse:
            print("smtplib.SMTPSenderRefused",senderrefuse)
        except smtplib.SMTPRecipientsRefused as recrefused:
            print("smtplib.SMTPRecipientsRefused",recrefused)
        except smtplib.SMTPDataError as data:
            print("smtplib.SMTPDataError",data)
        except smtplib.SMTPConnectError as connect:
            print("smtplib.SMTPConnectError",connect)
        except smtplib.SMTPHeloError as helo:
            print("smtplib.SMTPHeloError",helo)
        except smtplib.SMTPAuthenticationError as auth:
            print("smtplib.SMTPAuthenticationError",auth)
        except Exception as e:
            print("Exception", e)
            print(traceback.format_exc())
            print(sys.exc_info()[0])


if __name__ == "__main__":
    mail()