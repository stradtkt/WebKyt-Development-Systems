from flask import Flask, render_template, redirect, request, flash, url_for
from flask_mail import Mail, Message
import re
from config import EMAIL_CREDS

app = Flask(__name__)
app.secret_key = 'fjheei303r3.f,/,s??>##R?##$>RFE>$F$>$F?F?e.43meoe'
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL_CREDS['username']
app.config['MAIL_PASSWORD'] = EMAIL_CREDS['password']
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/portfolio', methods=['GET'])
def portfolio():
    portfolios = [
            {'name': 'Breathtaking', 'url': 'https://github.com/stradtkt/CSharp-Breathtaking', 'desc': 'This site was made for the owners of a Smokey Mountain property made with C# and JavaScript', 'img': 'breathtaking.png', 'video': 'breathtaking-1.mp4', 'languages': ['C#', 'JavaScript', 'Bootstrap', 'CSS', 'HTML'], 'tag': 'C#'},
            {'name': 'Ninja Gold', 'url': 'https://github.com/stradtkt/Ninja-Gold-Python', 'desc': 'This was made as a part of the coding dojo program. Get the most gold!', 'img': 'cave2.jpg', 'video': 'ninja_gold-1.mp4', 'languages': ['Python', 'Flask', 'Bootstrap', 'CSS', 'HTML'],  'tag': 'Flask'},
            {'name': 'Pagination + Search', 'url': 'https://github.com/stradtkt/Pagination', 'desc': 'This is a project to show how javascript can influence pagination and search bars', 'img': 'pag.png', 'video': 'students-1.mp4', 'languages': ['JavaScript', 'jQuery', 'Bootstrap', 'CSS', 'HTML'], 'tag': 'JavaScript'},
            {'name': 'CCRS', 'url': 'http://helprepaircredit.com', 'desc': 'This is for a credit repair company, this is a basic layout with no back-end functionality', 'img': 'ccrs.png', 'video': 'ccrs-1.mp4', 'languages': ['PHP', 'JavaScript', 'Bootstrap', 'CSS', 'HTML'], 'tag': 'JavaScript'},
            {'name': 'Phrase Hunter', 'url': 'NA', 'desc': 'Phrase hunter is depicting a game show where players would need to guess what the phrase is in a limited amout of misses', 'img': 'phrase.png', 'video': 'phrase-1.mp4', 'languages': ['JavaScript', 'jQuery', 'Bootstrap', 'CSS', 'HTML'], 'tag': 'JavaScript'},
            {'name': 'Job Directory', 'url': 'https://github.com/stradtkt/JobDirectory-Django', 'desc': 'Find a job, add a job, apply for a job with a detailed dashboard', 'img': 'job.png', 'video': 'job-1.mp4', 'languages': ['Python', 'Django', 'JavaScript', 'Bootstrap', 'CSS'], 'tag': ['Python', 'Django']},
    ]
    return render_template('portfolio.html', portfolios=portfolios)

@app.route('/services', methods=['GET'])
def services():
    skills = [
        {
            'languages': ['C#', 'Python', 'SQL', 'JavaScript', 'HTML', 'CSS3'], 
            'frameworks': ['Flask', 'Django', 'Entity Framework', 'Dapper ORM', 'Asp.Net', 'Express.JS', 'Node.JS', 'Angular', 'AJAX', 'Bootstrap', 'Less', 'Sass'],
            'databases': ['MySQL', 'SQLite', 'MongoDB'], 
        }
    ]
    return render_template('services.html', skills=skills)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        return render_template('contact.html')
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['msg']
        msg = Message('Hello', sender=EMAIL_CREDS['username'], recipients=[EMAIL_CREDS['username']])
        msg.body = "Name: " + name + "\n" + "Email: " + email + "\n" + "Subject: " + subject + "\n" + "Message: " + message + "\n"
        mail.send(msg)
        flash("Your Message Has Been Sent", "success")
        return redirect(url_for('index'))

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == "POST":
        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        PHONE_REGEX = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        company = request.form['company']
        quote_phone = request.form['phone']
        quote_email = request.form['quote_email']
        website_url = request.form['website_url']
        services = request.form['services']
        website_budget = request.form['website_budget']
        monthly_budget = request.form['monthly_budget']
        details = request.form['details']
        contact = request.form.get('contact')
        valid = True
        if not first_name.isalpha():
            valid = False
            flash("First name can only be letters", "danger")
        elif first_name.isalpha():
            valid = True
        if not last_name.isalpha():
            valid = False
            flash("Last name can only be letters", "danger")
        if company == "":
            valid = False
            flash("Company cannot be empty", "danger")
        if quote_email == "":
            valid = False
            flash("Email cannot be empty", "danger")
        elif not re.match(EMAIL_REGEX, quote_email):
            valid = False
            flash("That is an invalid email, please try again", "danger")
        if quote_phone == "":
            valid = False
            flash("Phone cannot be empty", "danger")
        elif not re.match(PHONE_REGEX, quote_phone):
            valid = False
            flash("That is an invalid phone number, please try again", "danger")
        if services == "":
            valid = False
            flash("Services cannot be empty", "danger")
        elif len(services) < 10:
            valid = False
            flash("Services has a min length of 10", "danger")
        if website_budget == "":
            valid = False
            flash("Website budget cannot be empty", "danger")
        if monthly_budget == "":
            valid = False
            flash("Montly budget cannot be empty", "danger")
        if details == "":
            valid = False
            flash("Details cannot be empty", "danger")
        elif len(details) < 10:
            valid = False
            flash("Details has a min length of 10", "danger")
        if contact == "":
            valid = False
            flash("Form of contact needs to be filled out", "danger")
        if valid == False:
            valid = False
            flash("You need to fill out some missing information before sending this form", "danger")
        else:
            msg = Message("Hello", sender=EMAIL_CREDS['username'], recipients=[EMAIL_CREDS['username']] )
            msg.body = "Hello {} \n Here is a request from \n Company Name: {} \n First: {} Last: {} \n Email: {} Phone: {} \n Website: {} \n Services Needed: \n {} \n Website Budget: {} Monthly Budget: {} \n Project Details: \n {} \n Form of Contact: {}".format(
            EMAIL_CREDS['username'], company, first_name, last_name, quote_email, quote_phone, website_url, services, website_budget, monthly_budget, details, contact)
            mail.send(msg)
            flash("Your message has been sent!  We will get back to you shortly", "success")
            return redirect(url_for('index'))
        return redirect(url_for('quote'))
    elif request.method == "GET":
        return render_template('quote.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
