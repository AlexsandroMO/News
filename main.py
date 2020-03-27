#Created by:  Alexsandro Monteiro
#Date:        26/07/2019
#Site for Tests Python / Flask
#Fipe Table Consult

#Python any Where
#https://www.pythonanywhere.com/user/AlexsandroMO/
#pip install flask

from flask import Flask, render_template, url_for, request,send_from_directory
import Progpy
import requests
from bs4 import BeautifulSoup

#==================================
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/news')
def news():
  news = Progpy.news_all()

  varall = Progpy.all_resume(news)

  var = []
  for item in varall:
    var.append([item[0], item[1], item[2]])

  return render_template('news.html', var=var)

@app.route('/read_news_G1')
def read_news_G1():
  varall = Progpy.news_g1()
  var = []
  for item in varall:
    var.append([item[0], item[1], item[2]])

  return render_template('read-news-G1.html', var=var)

@app.route('/read_news_R7')
def read_news_R7():
  varall = Progpy.news_r7()
  var = []
  for item in varall:
    var.append([item[0], item[1], item[2]])

  return render_template('read-news-R7.html', var=var)

@app.route('/read_news_FSP')
def read_news_FSP():
  varall = Progpy.news_fsp()
  var = []
  for item in varall:
    var.append([item[0], item[1], item[2]])

  return render_template('read-news-FSP.html', var=var)

@app.route('/read_news_DIA')
def read_news_DIA():
  varall = Progpy.news_dia()
  var = []
  for item in varall:
    var.append([item[0], item[1], item[2]])

  return render_template('read-news-DIA.html', var=var)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
