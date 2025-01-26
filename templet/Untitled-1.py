from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import google.generativeai as genai

def scrapNews():
    url = 'https://www.liputan6.com/tekno/read/5849140/pesawat-antariksa-nasa-akan-catat-sejarah-jaraknya-terdekat-dengan-matahari'
    respons = requests.get(url)
    elemen = BeautifulSoup(respons.content, 'html.parser')
    headline = elemen.find("h1", class_="read-page--header--title entry-title")
    return headline.text

app = Flask(__name__)
@app.route("/geminiAi", methods=['GET','POST'])
def home():
    if request.method == 'POST':
       pertanyaan = request.form['Pertanyaan']
       genai.configure(api_key="AIzaSyAMUoGBn_Sg1GqBJBoImwMwlZaPh_NS2jw")
       model = genai.GenerativeModel("gemini-1.5-flash")
       response = model.generate_content(pertanyaan)
       jawaban = response.text
       return render_template('index.html', jawaban=jawaban)
    scresul = scrapNews()
    return render_template('index.html', data=scresul)

if __name__ == "__main__":
    app.run(debug=True)
