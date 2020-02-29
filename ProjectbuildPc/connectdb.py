import pymongo

#----------------CPU-------------------------------
def callCPU():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataCPU = db.CPU.find()
    return dataCPU
def getCPUdata():
    result = callCPU()
    data = []
    for i in result:
        name = i['CPUname']
        manufacturer = i['Manufacturer']
        corecount = i['CoreCount']
        threadscount = i['ThreadsCount']
        coreclock = i['CoreClock']
        boostclock = i['BoostClock']
        microarchitecture = i['Microarchitecture']
        socket = i['Socket']
        lithography = i['Lithography']
        generation = i['Generation']
        dic = {"Name": name, "Manufacturer": manufacturer, "Core Count": corecount, "Threads Count": threadscount, "Core Clock": coreclock, "Socket": socket,
               "BoostClock": boostclock, "Micro Architecture": microarchitecture,  "Lithography": lithography, "Generation": generation}
        data.append(dic)
    return data
def onlyCPUname():
    result = callCPU()
    CPUname = []
    for i in result:
        CPUname.append(i['CPUname'])
    all = CPUname
    CPU = list(set(CPUname))
    return CPU


#----------------Mainboard-------------------------------
def callMB():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataMB = db.Mainboard.find()
    return dataMB
def getMBdata():
    result = callMB()
    data = []
    for i in result:
        name = i['MBname']
        manufacturer = i['Manufacturer']
        chipset = i['chipset']
        ramslot = i['ramslot']
        ddr = i['DDR']
        supportbus = i['supportbus']
        audio = i['Audio']
        socket = i['Socket']
        wirelesssupport = i['Wirelesssupport']
        dic = {"Name": name, "Manufacturer": manufacturer, "chipset": chipset, "Ram Slot": ramslot, "Socket": socket,
               "DDR": ddr, "Support Bus": supportbus, "Audio": audio, "Wireless Support": wirelesssupport}
        data.append(dic)
    return data
def onlyMBchipset():
    result = callMB()
    chipset = []
    for i in result:
        chipset.append(i['chipset'])
    all = chipset
    MB = list(set(chipset))
    return MB


#----------------Harddisk-------------------------------
def callHDD():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataHDD = db.HDD.find()
    return dataHDD
def getHDDdata():
    result = callHDD()
    data = []
    for i in result:
        if i['HDDtype'] == 'HDD':
            name = i['HDDname']
            Manufacturer = i['HDDManufacturer']
            format = i['HDDformat']
            interface = i['HDDinterface']
            capacity = i['HDD capacity']
            read = i['HDDread']
            write = i['HDDwrite']
            RPM = i['RPM']
            dic = {"Name": name, "Manufacturer": Manufacturer, "format": format, "interface": interface, "capacity": capacity, "read": read, "write": write,"RPM":RPM}
            data.append(dic)
    return data
def getSSDdata():
    result = callHDD()
    data = []
    for i in result:
        if i['HDDtype'] == 'SSD':
            name = i['HDDname']
            Manufacturer= i['HDDManufacturer']
            format = i['HDDformat']
            interface = i['HDDinterface']
            capacity = i['HDD capacity']
            read = i['HDDread']
            write = i['HDDwrite']
            dic = {"Name": name, "Manufacturer":Manufacturer, "format": format, "interface":interface, "capacity":capacity, "read":read, "write":write}
            data.append(dic)
    return data
def getSSHDdata():
    result = callHDD()
    data = []
    for i in result:
        if i['HDDtype'] == 'SSHD':
            name = i['HDDname']
            Manufacturer = i['HDDManufacturer']
            format = i['HDDformat']
            interface = i['HDDinterface']
            capacity = i['HDD capacity']
            read = i['HDDread']
            write = i['HDDwrite']
            RPM = i['RPM']
            dic = {"Name": name, "Manufacturer": Manufacturer, "format": format, "interface": interface, "capacity": capacity, "read": read, "write": write,"RPM":RPM}
            data.append(dic)

    return data
def onlyHDDtype():
    result = callHDD()
    HDDtype = []
    for i in result:
        HDDtype.append(i['HDDtype'])
    all = HDDtype
    HDD = list(set(HDDtype))
    return HDD


#----------------PSU-------------------------------
def callPSU():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataPSU = db.PSU.find()
    return dataPSU
def getPSUdata():
    result = callPSU()
    data = []
    for i in result:
        name = i['PSUname']
        dic = {"Name": name}
        data.append(dic)
    return data
def onlyPower():
    result = callPSU()
    Power = []
    for i in result:
        Power.append(i['Power'])
    all = Power
    PSU = list(set(Power))
    return PSU


#----------------RAM-------------------------------
def callRAM():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataRAM = db.RAM.find()
    return dataRAM
def getRAMdata():
    result = callRAM()
    data = []
    for i in result:
        name = i['RAMname']
        dic = {"Name": name}
        data.append(dic)
    return data
def onlyDDR():
    result = callRAM()
    DDR = []
    for i in result:
        DDR.append(i['DDR'])
    all = DDR
    RAM = list(set(DDR))
    return RAM


#---------------------Sink-------------------------------
def callSink():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataSink = db.Sink.find()
    return dataSink
def getSinkdata():
    result = callSink()
    data = []
    for i in result:
        name = i['Sinkname']
        dic = {"Name": name}
        data.append(dic)
    return data
def onlySinkname():
    result = callSink()
    SinkType = []
    for i in result:
        SinkType.append(i['SinkType'])
    all = SinkType
    Sink = list(set(SinkType))
    return Sink


#-----------------------VGA-------------------------------
def callVGA():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataVGA = db.VGA.find()
    return dataVGA
def getVGAdata():
    result = callVGA()
    data = []
    for i in result:
        name = i['VGAname']
        dic = {"Name": name}
        data.append(dic)
    return data
def onlyVGAname():
    result = callVGA()
    VGAname = []
    for i in result:
        VGAname.append(i['VGAname'])
    all = VGAname
    VGA = list(set(VGAname))
    return VGA

