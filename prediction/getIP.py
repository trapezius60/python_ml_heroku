from flask import Blueprint,render_template

import socket

getIP=Blueprint('getIP',__name__)

@getIP.route("/getIP")#default page of web

def getIPAddress(): #ชือ function ห้ามซ้ำกับชื่อ หลัง @
    hostname=socket.gethostname()
    IP=socket.gethostbyname(hostname)
    print('My IP is '+IP)
    return render_template("getIP.html", data=IP)
