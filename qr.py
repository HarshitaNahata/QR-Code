import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=B9ez4xdr4KE&ab_channel=SuryaRagunaathan")
img.save("dil_jhoom.png")
