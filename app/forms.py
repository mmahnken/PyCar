from flask.ext.wtf import Form, TextField, TextAreaField, BooleanField, Required, SelectField, IntegerField, DateTimeField

class MileageForm(Form):
	mileage_for_jeep = IntegerField('mileage_for_jeep')
	mileage_for_volvo = IntegerField('mileage_for_volvo')
	mileage_for_honda = IntegerField('mileage_for_honda')

	
	

