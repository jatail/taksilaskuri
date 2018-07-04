class vendorObject:
    __vendorName = ''
    __startFare = 0
    __kmFare = 0
    __timeFare = 0
    def __init__(self, name, startFare, kmFare, timeFare):
        self.vendorName = name 
        self.startFare = startFare
        self.kmFare = kmFare
        self.timeFare = timeFare

vendors = []

vendors.append(vendorObject('Lounais-Suomen taxidata', 5.9, 1.60, 0))
vendors.append(vendorObject('Satakunnan aluetaksi', 3.9, 1.60, 42))
vendors.append(vendorObject('Taksi Helsinki', 5.9, 1.60, 0))
vendors.append(vendorObject('Lähitaksi', 3.50, 1.59, 0))
vendors.append(vendorObject('Taksi Tampere', 5.30, 1.84, 0))
vendors.append(vendorObject('Otaxi', 5.90, 1.60, 0))
vendors.append(vendorObject('Kymenlaakson taksi', 4.90, 1.35, 28.2))
vendors.append(vendorObject('Jytaksi', 5.90, 1.60, 0))
vendors.append(vendorObject('Kajon', 5.90, 1.49, 0))
vendors.append(vendorObject('Kovanen', 5.90, 1.60, 0))
vendors.append(vendorObject('FixuTaxi', 2.95, 1.60, 0))
vendors.append(vendorObject('UberX', 3.00, 1.10, 18))
vendors.append(vendorObject('UberBlack', 5, 1.50, 24))