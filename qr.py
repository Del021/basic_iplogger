import subprocess
import qrcode
from os import system

with open('qr_link.dat', 'r') as qr_link:

	reading = qr_link.read()

link = reading

def make_qr(url):
	tracker = url
	qr = qrcode.QRCode(version= 1, box_size= 10, border= 5 )
	qr.add_data(tracker)
	qr.make(fit=True)

	img = qr.make_image(fill='black', back_color = 'white')
	img.save('qr_ready.png')


