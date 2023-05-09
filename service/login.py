from flask import render_template


def login_check():
    print("login check")
    return render_template('HEhome.html')