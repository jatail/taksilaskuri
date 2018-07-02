from flask import Flask, render_template, request
import urllib, json
from objects import routeObject, priceObject
from vendors import vendorObject, vendors
app = Flask(__name__, static_url_path='/static')

apikey = open("apikey.txt").read()

@app.route("/", methods=['GET', 'POST'])
def hello():
    resultpage = False
    if request.method == 'POST':
        start = request.form['start']
        target = request.form['end']
        resultpage = True
        start_fin = (start + ', Finland')
        target_fin = (target + ', Finland')
        
        start_edit = start_fin.replace('ä', 'a').replace('ö', 'o').replace('å', 'a')
        target_edit = target_fin.replace('ä', 'a').replace('ö', 'o').replace('å', 'a')
        apiurl = 'http://www.mapquestapi.com/directions/v2/route?key='
        url = (apiurl + apikey + '&from=' + start_edit + '&to=' + target_edit + '&unit=k').replace(' ', '%20')
        print(url)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())


        route = routeObject()
        route.start = start
        route.end = target
        route.distance = round(data["route"]["distance"], 2)
        route.time = data["route"]["time"]

        priceList = []

        for vendor in vendors:
            hinta = round((vendor.startFare + route.distance * vendor.kmFare + route.timeinminutes() / 60 * vendor.timeFare), 2)
            price = priceObject(vendor.vendorName, hinta)
            price.diff = round(hinta / route.oldPrice() * 100, 0) - 100
            if price.diff > 0:
                price.char = 'fa-arrow-up'
            elif price.diff < 0:
                price.char = 'fa-arrow-down'
                price.diff = price.diff * -1
            else:
                price.char = 'fa-check'

            priceList.append(price)


        return render_template('page.html', route=route, resultpage=resultpage, priceList=priceList)

    return render_template('page.html', resultpage=resultpage)

@app.route("/calculate", methods=['POST'])
def calculate():
    start = request.form['start']
    target = request.form['end']
    resultpage = True
    start_fin = (start + ', Finland')
    target_fin = (target + ', Finland')
    
    start_edit = start_fin.replace('ä', 'a').replace('ö', 'o').replace('å', 'a')
    target_edit = target_fin.replace('ä', 'a').replace('ö', 'o').replace('å', 'a')
    apiurl = 'http://www.mapquestapi.com/directions/v2/route?key='
    url = (apiurl + apikey + '&from=' + start_edit + '&to=' + target_edit + '&unit=k').replace(' ', '%20')
    print(url)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())


    route = routeObject()
    route.start = start
    route.end = target
    route.distance = round(data["route"]["distance"], 2)
    route.time = data["route"]["time"]

    priceList = []

    for vendor in vendors:
        hinta = round((vendor.startFare + route.distance * vendor.kmFare + route.timeinminutes() / 60 * vendor.timeFare), 2)
        price = priceObject(vendor.vendorName, hinta)
        price.diff = round(hinta / route.oldPrice() * 100, 0) - 100
        if price.diff > 0:
            price.char = 'fa-arrow-up'
        elif price.diff < 0:
            price.char = 'fa-arrow-down'
            price.diff = price.diff * -1
        else:
            price.char = 'fa-check'

        priceList.append(price)


    return render_template('page.html', route=route, resultpage=resultpage, priceList=priceList)