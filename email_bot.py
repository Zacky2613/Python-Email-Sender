import smtplib, socket
import tkinter as tk

root = tk.Tk()
root.resizable(False, False)

def close():
    root.destroy()

def Window():
    root.geometry("450x300")
    root.title("Zacky2613's Email Sender.")

    bot_label = tk.Label(root, text="Welcome User to Dark Matter's Custom Email Bot.")
    bot_label.pack(side = "top", anchor = "nw")

    buffer_label_0 = tk.Label(root, text=" ")
    buffer_label_0.pack(side = "top", anchor = "nw")

    # Send to:
    bot_label_to = tk.Label(root, text="Send to: ")
    bot_label_to.pack(side = "top", anchor = "nw")

    bot_entry_to = tk.Entry(root, width=30)
    bot_entry_to.pack(side = "top", anchor = "nw")
    
    buffer_label_01 = tk.Label(root, text=" ")
    buffer_label_01.pack(side = "top", anchor = "nw")

    # Subject
    bot_label_subject = tk.Label(root, text="Subject: ")
    bot_label_subject.pack(side = "top", anchor = "nw")

    bot_entry_subject = tk.Entry(root)
    bot_entry_subject.pack(side = "top", anchor = "nw")

    buffer_label_012 = tk.Label(root, text=" ")
    buffer_label_012.pack(side = "top", anchor = "nw")

    # Body
    bot_label_body = tk.Label(root, text="Body: ")
    bot_label_body.pack(side = "top", anchor = "nw")

    bot_entry_body = tk.Entry(root, width=100)
    bot_entry_body.pack(side = "top", anchor = "nw")

    buffer_label_0123 = tk.Label(root, text=" ")
    buffer_label_0123.pack(side = "top", anchor = "nw")

    # Amount of Emails
    bot_label_amount = tk.Label(root, text="  :Number of Emails")
    bot_label_amount.pack(side = "right", anchor = "ne")

    bot_entry_amount = tk.Entry(root, width=10)
    bot_entry_amount.pack(side = "right", anchor = "ne")

    buffer_label_01234 = tk.Label(root, text=" ")
    buffer_label_01234.pack(side = "right", anchor = "ne")

    #Email Code
    def Email_Bot():

        email_to = bot_entry_to.get()
        email_text = bot_entry_body.get()
        email_subject = bot_entry_subject.get()
        email_amount = bot_entry_amount.get()
        try:
            email_amount = int(email_amount)
        except ValueError:
            label_valuerror = tk.Label(root, text="ERROR: Enter a number for attacks")
            label_valuerror.pack(side="left", anchor="se")


        sender_email = '' # Put email address here. 
        sender_password = '' # Put email password here.
     
        for x in range(email_amount):
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                try: 
                    server_connection_connected.pack_forget()
                    server_connection_connected = tk.Label(root, text="Server: smtp.gmail.com, Port: 587")
                    server_connection_connected.pack(side = "top", anchor = "ne")
                except:
                    server_connection_connected = tk.Label(root, text="Server: smtp.gmail.com, Port: 587")
                    server_connection_connected.pack(side = "top", anchor = "ne")

            except socket.gaierror:
                server_connection_offline = tk.Label(root, text="")
                server_connection_offline.pack(side = "top", anchor = "ne")
                close()
                exit()


            server.ehlo()
            server.starttls()
            server.login(sender_email, sender_password) # Logs in with your email.


            message = 'Subject: {}\n\n{}'.format(email_subject, email_text)

            try:
                server.sendmail(sender_email, email_to, message)
                try:
                    Email_Sent.pack_forget()
                    Email_Sent = tk.Label(root, text=f"Email sent: <{email_to}>")
                    Email_Sent.pack(side = "top", anchor = "ne")
                except:
                    Email_Sent = tk.Label(root, text=f"Email sent: <{email_to}>")
                    Email_Sent.pack(side = "top", anchor = "ne")



            except smtplib.SMTPRecipientsRefused:
                Email_Error = tk.Label(root, text=f"ERROR: The email address <{email_to}> is unreachable aka not real")
                Email_Error.pack(side = "top", anchor = "ne")
    
    bot_button = tk.Button(root, text="Email", command=Email_Bot)
    bot_button.pack(side = "left", anchor = "se")


Window()

root.bind("<Escape>", close)
root.mainloop()
