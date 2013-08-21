import requests
import lxml
from lxml import html

def getVolvoPrice(mileage):
	link = 'http://www.kbb.com/volvo/xc90/2005-volvo-xc90/25t-sport-utility-4d/?vehicleid=1906&intent=buy-used&mileage=%r&options=72640|true|72726|true|72670|true|72679|true|72723|true|72734|true|72740|true|72755|true&pricetype=private-party&condition=excellent' % mileage
	r = requests.get(link)
	tree = html.fromstring(r.text)
	price = tree.xpath('//div[@class="value"]/text()')
	return price

def getJeepPrice(mileage):
	link = 'http://www.kbb.com/jeep/wrangler/2005-jeep-wrangler/unlimited-sport-utility-2d/?vehicleid=1027&intent=buy-used&mileage=%r&options=41403|true|41345|true|41434|true|41434|false|41484|true|41518|true&pricetype=private-party&condition=excellent' % mileage
	r = requests.get(link)
	tree = html.fromstring(r.text)
	price = tree.xpath('//div[@class="value"]/text()')
	return price

def getHondaPrice(mileage):
	link = 'http://www.kbb.com/honda/civic/2006-honda-civic/hybrid-sedan-4d/?vehicleid=753&intent=buy-used&mileage=%r&options=31089|true&pricetype=private-party&condition=excellent' % mileage
	r = requests.get(link)
	tree = html.fromstring(r.text)
	price = tree.xpath('//div[@class="value"]/text()')
	return price

