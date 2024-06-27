from flask import Flask, render_template, request, url_for, redirect 
import smtplib 
from email.message import EmailMessage 
app = Flask(__name__) 

@app.route("/") 
def index(): 
	return render_template("index.html") 

@app.route("/sendemail/", methods=['POST']) 
def sendemail(): 
	if request.method == "POST": 
		name = request.form['name'] 
		subject = request.form['subject'] 
		email = request.form['email'] 
		message = request.form['message'] 
		mobile="Contact.No:+91 9789586078"
		Linkedin="Linkedin:https://www.linkedin.com/in/mari-kannan-b-66ab67227"
		
		
		

		# Set your credentials 
		yourEmail = "capkannan16@gmail.com"
		yourPassword = "dcms lixe aklk hjml"

		# Logging in to our email account 
		server = smtplib.SMTP('smtp.gmail.com', 587) 
		server.ehlo() 
		server.starttls() 
		server.login(yourEmail, yourPassword) 

		# Sender's and Receiver's email address 
		msg = EmailMessage() 
		msg.set_content("First Name : "+str(name) 
						+"\nEmail : "+str(email) 
						+"\nSubject : "+str(subject) 
						+"\nMessage : "+str(message))

		msg['To'] = yourEmail 
		msg['From'] = email
		msg['Subject'] = subject 

		# Send the message via our own SMTP server. 
		try: 
			# sending an email 
			server.send_message(msg) 
			print("Send") 
		except: 
			print("Fail to Send") 
			pass
			
	return redirect('/') 

if __name__ == "__main__": 
	app.run(debug=True)
