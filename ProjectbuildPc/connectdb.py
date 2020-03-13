import pymongo


# ----------------CPU-------------------------------
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
        score = i['Score']
        dic = {"Name": name, "Manufacturer": manufacturer, "Core Count": corecount, "Threads Count": threadscount, "Core Clock": coreclock, "Socket": socket,
               "BoostClock": boostclock, "Micro Architecture": microarchitecture, "Lithography": lithography, "Generation": generation, "Score": score}
        data.append(dic)
    return data


def getSelectCPUdata(selecteddata):
    result = callCPU()
    data = []
    for i in result:
        if i['Manufacturer'] == selecteddata:
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
            score = i['Score']
            dic = {"Name": name, "Manufacturer": manufacturer, "Core Count": corecount, "Threads Count": threadscount, "Core Clock": coreclock, "Socket": socket,
                   "BoostClock": boostclock, "Micro Architecture": microarchitecture, "Lithography": lithography, "Generation": generation, "Score": score}
            data.append(dic)
    return data


def onlyCPUsocket():
    result = callCPU()
    socket = []
    for i in result:
        socket.append(i['Socket'])
    all = socket
    CPU = list(set(socket))
    return CPU


def onlyCPUmanu():
    result = callCPU()
    manufacturer = []
    for i in result:
        manufacturer.append(i['Manufacturer'])
    all = manufacturer
    CPU = list(set(manufacturer))
    return CPU


# ----------------Mainboard-------------------------------
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
        score = i['Score']
        dic = {"Name": name, "Manufacturer": manufacturer, "chipset": chipset, "Ram Slot": ramslot, "Socket": socket,
               "DDR": ddr, "Support Bus": supportbus, "Audio": audio, "Wireless Support": wirelesssupport, "Score": score}
        data.append(dic)
    return data


def getSelectedMBdata(selecteddata):
    result = callMB()
    data = []
    for i in result:
        if i['chipset'] == selecteddata:
            name = i['MBname']
            manufacturer = i['Manufacturer']
            chipset = i['chipset']
            ramslot = i['ramslot']
            ddr = i['DDR']
            supportbus = i['supportbus']
            audio = i['Audio']
            socket = i['Socket']
            wirelesssupport = i['Wirelesssupport']
            score = i['Score']
            dic = {"Name": name, "Manufacturer": manufacturer, "chipset": chipset, "Ram Slot": ramslot, "Socket": socket,
                   "DDR": ddr, "Support Bus": supportbus, "Audio": audio, "Wireless Support": wirelesssupport, "Score": score}
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


# ----------------Harddisk-------------------------------
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
            score = i['Score']
            dic = {"Name": name, "Manufacturer": Manufacturer, "Format": format, "Interface": interface, "Capacity": capacity, "Read": read, "Write": write, "RPM": RPM,
                   "Score": score}
            data.append(dic)
    return data


def getSSDdata():
    result = callHDD()
    data = []
    for i in result:
        if i['HDDtype'] == 'SSD':
            name = i['HDDname']
            Manufacturer = i['HDDManufacturer']
            format = i['HDDformat']
            interface = i['HDDinterface']
            capacity = i['HDD capacity']
            read = i['HDDread']
            write = i['HDDwrite']
            score = i['Score']
            dic = {"Name": name, "Manufacturer": Manufacturer, "Format": format, "Interface": interface, "Capacity": capacity, "Read": read, "Write": write, "Score": score}
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
            score = i['Score']
            dic = {"Name": name, "Manufacturer": Manufacturer, "Format": format, "Interface": interface, "Capacity": capacity, "Read": read, "Write": write, "RPM": RPM,
                   "Score": score}
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


# ----------------PSU-------------------------------
def callPSU():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataPSU = db.PSU.find()
    return dataPSU


def getPSUdata():
    result = callPSU()
    data = []
    for i in result:
        name = i['PSU name']
        power = i['Power']
        cer = i['Certification']
        modu = i['Modular']
        fac = i['Form Factor']
        score = i['Score']
        dic = {"Name": name, "Power": power, "Certification": cer, "Modular": modu, "Form Factor": fac, "Score": score}
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


# ----------------RAM-------------------------------
def callRAM():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataRAM = db.RAM.find()
    return dataRAM


def getRAMdata():
    result = callRAM()
    data = []
    for i in result:
        name = i['RAM name']
        manu = i['Manufacturer']
        ddr = i['DDR']
        bus = i['BUS']
        cl = i['CL']
        cap = i['capacity']
        score = i['Score']
        dic = {"Name": name, "Manufacturer": manu, "DDR": ddr, "BUS": bus, "CL": cl, "capacity": cap, "Score": score}
        data.append(dic)
    return data


def getRAMddrdata(selectedddr):
    result = callRAM()
    data = []
    for i in result:
        if i['DDR'] == str(selectedddr):
            name = i['RAM name']
            manu = i['Manufacturer']
            ddr = i['DDR']
            bus = i['BUS']
            cl = i['CL']
            cap = i['capacity']
            score = i['Score']
            dic = {"Name": name, "Manufacturer": manu, "DDR": ddr, "BUS": bus, "CL": cl, "capacity": cap, "Score": score}
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


# ---------------------Sink-------------------------------
def callSink():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    dataSink = db.SinkCPU.find()
    return dataSink


def getAirdata():
    result = callSink()
    data = []
    for i in result:
        if i['Sink Type'] == 'Air cooling':
            name = i['Sink name']
            stype = i['Sink Type']
            fspeed = i['FAN SPEED']
            con = i['CONNECTOR']
            nfan = i['Number of Fans']
            pipe = i['HEATPIPES']
            score = i['Score']
            dic = {"Name": name, "Sink Type": stype, "FAN SPEED": fspeed, "CONNECTOR": con, "Number of Fans": nfan, "HEATPIPES": pipe, "Score": score}
            data.append(dic)
    return data


def getLiqdata():
    result = callSink()
    data = []
    for i in result:
        if i['Sink Type'] == 'Water cooling':
            name = i['Sink name']
            stype = i['Sink Type']
            fspeed = i['FAN SPEED']
            con = i['CONNECTOR']
            nfan = i['Number of Fans']
            pump = i['pump speed']
            score = i['Score']
            dic = {"Name": name, "Sink Type": stype, "FAN SPEED": fspeed, "CONNECTOR": con, "Number of Fans": nfan, "pump speed": pump, "Score": score}
            data.append(dic)
    return data


def onlySinktype():
    result = callSink()
    SinkType = []
    for i in result:
        SinkType.append(i['Sink Type'])
    all = SinkType
    Sink = list(set(SinkType))
    return Sink


# -----------------------VGA-------------------------------
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
        vram = i['VRAM']
        gddr = i['GDDR']
        spc = i['SPC']
        pr = i['PowerRequirment']
        sc = i['ShaderCore']
        cs = i['Core speed']
        bus = i['Memory Bus']
        se = i['Series']
        score = i['Score']
        dic = {"Name": name, "VRAM": vram, "GDDR": gddr, "SPC": spc, "PowerRequirment": pr, "ShaderCore": sc, "Core speed": cs, "Memory Bus": bus, "Series": se, "Score": score}
        data.append(dic)
    return data


def getselectSeriesVGAdata(selected):
    result = callVGA()
    data = []
    for i in result:
        if i['Series'] == selected:
            name = i['VGAname']
            vram = i['VRAM']
            gddr = i['GDDR']
            spc = i['SPC']
            pr = i['PowerRequirment']
            sc = i['ShaderCore']
            cs = i['Core speed']
            bus = i['Memory Bus']
            se = i['Series']
            score = i['Score']
            dic = {"Name": name, "VRAM": vram, "GDDR": gddr, "SPC": spc, "PowerRequirment": pr, "ShaderCore": sc, "Core speed": cs, "Memory Bus": bus, "Series": se, "Score": score}
            data.append(dic)
    return data


def onlySeries():
    result = callVGA()
    series = []
    for i in result:
        series.append(i['Series'])
    all = series
    VGA = list(set(series))
    return VGA


# -------------------------------------------history--------------------------------------------------

def callHistory():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("PCbuild")
    datahistory = db.History.find()
    return datahistory


def getHistory():
    result = callHistory()
    data = []
    for i in result:
        pc = i['PCname']
        cpu = i['CPU']
        gpu = i['VGA']
        ram = i['RAM']
        mb = i['MB']
        psu = i['PSU']
        sink = i['Sink']
        hdd1 = i['HDD1']
        hdd2 = i['HDD2']
        total = i['score']
        _id = i['_id']
        dic = {"PC": pc,"CPU": cpu, "VGA": gpu, "RAM": ram, "MB": mb, "PSU": psu, "Sink": sink, "HDD1": hdd1, "HDD2": hdd2, "score": total, "_id":_id}
        data.append(dic)
    return data
