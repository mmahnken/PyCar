from flask import render_template, request
from app import app
import cars
from cars import getVolvoPrice, getHondaPrice, getJeepPrice
import forms
from forms import MileageForm
#import other necessary files

@app.route('/')
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = MileageForm()
	return render_template("index.html", form = form)


@app.route('/getting', methods = ['GET', 'POST'])
def getting():
	j = request.form['mileage_for_jeep']
	v = request.form['mileage_for_volvo']
	h = request.form['mileage_for_honda']
	jeep = getJeepPrice(j)
	volvo = getVolvoPrice(v)
	honda = getHondaPrice(h)
	return render_template('results.html', jeep = jeep, 
		volvo = volvo, honda = honda)
