from flask import Flask, request, render_template, redirect, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Your SMTP server details
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False  # Add this if it's not present
app.config['MAIL_USERNAME'] = 'esraaksitt@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'regr qiox vgkp rezj'  # Your app password
app.config['MAIL_DEFAULT_SENDER'] = 'esraaksitt@gmail.com'  # Default sender

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/team')
def team():
    return render_template('Team.html')

@app.route('/menu')
def menu():
    return render_template('Menu.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        recipients = ['recipient-email@example.com']  # Change to the actual recipient email

        msg = Message(subject, sender=email, recipients=recipients)
        msg.body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        
        try:
            mail.send(msg)
            return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    # If GET request
    return render_template('Contact.html')
if __name__ == '__main__':
    app.run(debug=True)