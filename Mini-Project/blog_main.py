from flask import Flask, render_template, request
import requests
import smtplib

my_email = "dummyacc041104@gmail.com"
password = "hdzsbundpwlprnbi"
response = requests.get("https://api.npoint.io/879030b17a6c256c21b7")
data = response.json()
# print(data[0]["title"])

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_post=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def get_posts(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", posts=requested_post)

@app.route('/contact', methods=["POST", "GET"])
def receive_data():
    if request.method == 'POST':
        received_data = request.form
        send_email(received_data["name"], received_data["email"], received_data["phone"], received_data["message"])
        return render_template('contact.html', message_sent=True)
    return render_template('contact.html', message_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=email_message)
        
if __name__ == "__main__":
    app.run(debug=True)