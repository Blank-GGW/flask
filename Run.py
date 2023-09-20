from flask import Flask,render_template, request, redirect, url_for, flash
from forms import ContactForm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # 这里可以处理表单数据，例如将其存储到数据库或发送电子邮件。

        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
