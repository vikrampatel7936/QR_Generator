import pyqrcode
s="portfoliodesign.herokuapp.com"
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)