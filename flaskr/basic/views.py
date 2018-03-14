#-*- coding: utf-8 -*-
from flask import render_template_string, request, render_template, redirect, url_for, session
from . import app
from .. import models
 

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").encode('utf-8')
        password = request.form.get("password").encode('utf-8')
        password = models.md5Encrypt(password)
        if models.validateUser(username, password):
            session['username'] = username
            return redirect(url_for('basic.mainPage',name='me'))
        else:
            return render_template("login_fail.html",content = 'Incorrect username or password')

    return render_template("login.html")

@app.route('/users/<name>',methods=["GET"])
def mainPage(name):
    return render_template("mainPage.html", name = session['username'])

@app.route('/logout', methods=["GET"])
def logout():
    session.clear()

    return redirect(url_for("basic.home"))

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").encode('utf-8')
        password = request.form.get("password").encode('utf-8')
        password = models.md5Encrypt(password)
        #print(username, password)
        if models.registerUser(username,password):
            return redirect(url_for("basic.login"))
        else:
            return render_template("regist_fail.html",content = 'username already existed!')
    return render_template("register.html")

@app.route('/users/<account>')
def users(account):
    return None# Implement me

    
    
