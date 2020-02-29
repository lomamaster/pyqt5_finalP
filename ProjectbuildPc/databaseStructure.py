import pymongo


def addCpu():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        {"CPUname": "i7-880", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "3.06 GHz", "BoostClock": "3.73 GHz",
         "Microarchitecture": "Lynnfield", "Socket": "LGA1156", "Lithography": "45 nm", "Generation": "1st gen", "Score": ""},

        {"CPUname": "i7-3770K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Ivy Bridge", "Socket": "LGA1155", "Lithography": "22 nm", "Generation": "3th gen", "Score": ""},

        {"CPUname": "i5-3570K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.40 GHz", "BoostClock": "3.80 GHz",
         "Microarchitecture": "Ivy Bridge", "Socket": "LGA1155", "Lithography": "22 nm", "Generation": "3th gen", "Score": ""},

        {"CPUname": "i3-3250", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "none",
         "Microarchitecture": "Ivy Bridge", "Socket": "LGA1155", "Lithography": "22 nm", "Generation": "3th gen", "Score": ""},

        {"CPUname": "i7-2700K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Sandy Bridge", "Socket": "LGA1155", "Lithography": "32 nm", "Generation": "2nd gen", "Score": ""},

        {"CPUname": "i7-990X", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.46 GHz", "BoostClock": "3.73 GHz",
         "Microarchitecture": "Gulftown", "Socket": "LGA1366", "Lithography": "32 nm", "Generation": "1st genX", "Score": ""},

        {"CPUname": "i5-2550K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.40 GHz", "BoostClock": "3.80 GHz",
         "Microarchitecture": "Sandy Bridge", "Socket": "LGA1155", "Lithography": "32 nm", "Generation": "2nd gen", "Score": ""},

        {"CPUname": "i5-760", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "2.80 GHz", "BoostClock": "3.33 GHz",
         "Microarchitecture": "Lynnfield", "Socket": "LGA1156", "Lithography": "45 nm", "Generation": "1st gen", "Score": ""},

        {"CPUname": "i3-2130", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.40 GHz", "BoostClock": "none",
         "Microarchitecture": "Sandy Bridge", "Socket": "LGA1155", "Lithography": "32 nm", "Generation": "2nd gen", "Score": ""},

        {"CPUname": "i7-4790k", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "4.00 GHz", "BoostClock": "4.40 GHz",
         "Microarchitecture": "Devil's Canyon", "Socket": "LGA1150", "Lithography": "22 nm", "Generation": "4th Gen", "Score": ""},

        {"CPUname": "i5-4690K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Devil's Canyon", "Socket": "LGA1150", "Lithography": "22 nm", "Generation": "4th Gen", "Score": ""},

        {"CPUname": "i3-4370", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "none",
         "Microarchitecture": "Devil's Canyon", "Socket": "LGA1150", "Lithography": "22 nm", "Generation": "4th Gen", "Score": ""},

        {"CPUname": "i3-6300", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "none",
         "Microarchitecture": "Skylake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "6th Gen", "Score": ""},

        {"CPUname": "i5-6600K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Skylake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "6th Gen", "Score": ""},

        {"CPUname": "i7-6700K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "4.00 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Skylake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "6th Gen", "Score": ""},

        {"CPUname": "i3-7350K", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "4.20 GHz", "BoostClock": "none",
         "Microarchitecture": "Kaby Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "i5-7600K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Kaby Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "i7-7700K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "4.20 GHz", "BoostClock": "4.50 GHz",
         "Microarchitecture": "Kaby Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "i3-8350K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "4.00 GHz", "BoostClock": "none",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "8th Gen", "Score": ""},

        {"CPUname": "i5-8600K", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "6", "CoreClock": "3.60 GHz", "BoostClock": "4.30 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "8th Gen", "Score": ""},

        {"CPUname": "i7-8700K", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.70 GHz", "BoostClock": "4.70 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "8th Gen", "Score": ""},

        {"CPUname": "i3-9350KF", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "4.00 GHz", "BoostClock": "4.60 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": ""},

        {"CPUname": "i7-9700KF", "Manufacturer": "Intel", "CoreCount": "8", "ThreadsCount": "8", "CoreClock": "3.60 GHz", "BoostClock": "4.90 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": ""},

        {"CPUname": "i9-9900KF", "Manufacturer": "Intel", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.60 GHz", "BoostClock": "5.00 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": ""},

        {"CPUname": "i5-9600KF", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "6", "CoreClock": "3.70 GHz", "BoostClock": "4.60 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": ""},

        # AMD
        {"CPUname": "Ryzen™ Threadripper™ 3990X", "Manufacturer": "AMD", "CoreCount": "64", "ThreadsCount": "128", "CoreClock": "2.90 GHz",
         "BoostClock": "4.30 GHz", "Microarchitecture": "Zen 2", "Socket": "sTRX4", "Lithography": "7 nm", "Generation": "3rd Gen", "Score": ""},

        {"CPUname": "Ryzen™ Threadripper™ 2990WX", "Manufacturer": "AMD", "CoreCount": "32", "ThreadsCount": "64", "CoreClock": "3.00 ",
         "BoostClock": "4.20 GHz", "Microarchitecture": "Zen+", "Socket": "sTR4", "Lithography": "12 nm", "Generation": "2rd Gen", "Score": ""},

        {"CPUname": "Ryzen™ Threadripper™ 1950X", "Manufacturer": "AMD", "CoreCount": "16", "ThreadsCount": "32", "CoreClock": "3.40 ",
         "BoostClock": "4.00 GHz", "Microarchitecture": "Zen", "Socket": "sTR4", "Lithography": "14 nm", "Generation": "1nd Gen", "Score": ""},

        {"CPUname": "Ryzen™ 9 3900X", "Manufacturer": "AMD", "CoreCount": "12", "ThreadsCount": "24", "CoreClock": "3.80 GHz",
         "BoostClock": "4.60 GHz", "Microarchitecture": "Zen 2", "Socket": "sTR4", "Lithography": "7 nm", "Generation": "3st Gen", "Score": ""},

        {"CPUname": "Ryzen™ 7 3800X", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.90 GHz",
         "BoostClock": "4.50 GHz", "Microarchitecture": "Zen 2", "Socket": "AM4", "Lithography": "7 nm", "Generation": "3rd Gen", "Score": ""},

        {"CPUname": "Ryzen™ 7 2700X", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.70 GHz",
         "BoostClock": "4.30 GHz", "Microarchitecture": "Zen+", "Socket": "AM4", "Lithography": "12 nm", "Generation": "2nd Gen", "Score": ""},

        {"CPUname": "Ryzen™ 7 1800X", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.60 GHz",
         "BoostClock": "4.00 GHz", "Microarchitecture": "Zen", "Socket": "AM4", "Lithography": "14 nm", "Generation": "1st Gen", "Score": ""},

        {"CPUname": "Ryzen™ 5 3600X", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.80 GHz",
         "BoostClock": "4.20 GHz", "Microarchitecture": "Zen 2", "Socket": "AM4", "Lithography": "7 nm", "Generation": "3nd Gen", "Score": ""},

        {"CPUname": "Ryzen™ 5 2600X", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.60 GHz",
         "BoostClock": "4.20 GHz", "Microarchitecture": "Zen+", "Socket": "AM4", "Lithography": "12 nm", "Generation": "2nd Gen", "Score": ""},

        {"CPUname": "Ryzen™ 5 1600X", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.60 GHz",
         "BoostClock": "4.00 GHz", "Microarchitecture": "Zen", "Socket": "AM4", "Lithography": "14 nm", "Generation": "1st Gen", "Score": ""},

        {"CPUname": "Ryzen™ 3 2300X", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "4.00 GHz",
         "Microarchitecture": "Zen+", "Socket": "AM4", "Lithography": "12 nm", "Generation": "2nd Gen", "Score": ""},

        {"CPUname": "Ryzen™ 3 1300X", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.70 GHz",
         "Microarchitecture": "Zen", "Socket": "AM4", "Lithography": "14 nm", "Generation": "1st Gen", "Score": ""},

        {"CPUname": "FX-9590", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "8", "CoreClock": "4.70 GHz", "BoostClock": "5.00 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": ""},

        {"CPUname": "FX-8370", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "8", "CoreClock": "4.00 GHz", "BoostClock": "4.30 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": ""},

        {"CPUname": "FX-6350", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "6", "CoreClock": "3.90 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": ""},

        {"CPUname": "FX-4350", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "4.20 GHz", "BoostClock": "4.30 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": ""},

        {"CPUname": "Athlon™ 3000G", "Manufacturer": "AMD", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "none",
         "Microarchitecture": "Raven", "Socket": "AM4", "Lithography": "14 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "Athlon™ 240GE", "Manufacturer": "AMD", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "none",
         "Microarchitecture": "Raven", "Socket": "AM4", "Lithography": "14 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "Athlon™ X4 970", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "4.00 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "A6-9550", "Manufacturer": "AMD", "CoreCount": "2", "ThreadsCount": "2", "CoreClock": "3.80 GHz", "BoostClock": "4.00 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "A8-9600", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.10 GHz", "BoostClock": "3.40 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "A10-9700", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.80 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": ""},

        {"CPUname": "A12-9800", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen"}
    ]
    db.CPU.insert_many(data)
    print("Finish add")


def addHdd():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [{"HDDtype": "SSD", "HDDname": "KC600", "HDDManufacturer": "Kingston", "HDDformat": "2.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "256GB, 512GB, 1024GB, 2048GB", "HDDread": "550MB/s", "HDDwrite": "520MB/s",
             "Score": ""},

            {"HDDtype": "SSD", "HDDname": "KC2000", "HDDManufacturer": "Kingston", "HDDformat": "M.2 2280",
             "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB", "HDDread": "3,200MB/s", "HDDwrite": "2,200MB/s",
             "Score": ""},

            {"HDDtype": "SSD", "HDDname": "970 EVO Plus", "HDDManufacturer": "samsung", "HDDformat": "M.2 2280",
             "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB", "HDDread": "3,500 MB/s", "HDDwrite": "3,300 MB/s",
             "Score": ""},

            {"HDDtype": "SSD", "HDDname": "860 EVO", "HDDManufacturer": "samsung", "HDDformat": "2.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB, 4TB", "HDDread": "550MB/s", "HDDwrite": "520MB/s",
             "Score": ""},

            {"HDDtype": "SSD", "HDDname": "WD BLUE 2.5", "HDDManufacturer": "WesternDigital", "HDDformat": "2.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB, 4TB", "HDDread": "560MB/s", "HDDwrite": "530MB/s",
             "Score": ""},

            {"HDDtype": "SSD", "HDDname": "WD BLUE 2280", "HDDManufacturer": "WesternDigital", "HDDformat": "M.2 2280",
             "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB", "HDDread": "2,400MB/s", "HDDwrite": "950MB/s", "Score": ""},

            {"HDDtype": "SSD", "HDDname": "WD BLACK 2280", "HDDManufacturer": "WesternDigital", "HDDformat": "M.2 2280",
             "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB", "HDDread": "3,400MB/s", "HDDwrite": "2,900MB/s",
             "Score": ""},

            {"HDDtype": "HDD", "HDDname": "WD Black 3.5", "HDDManufacturer": "WesternDigital", "HDDformat": "3.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "500GB - 6TB", "HDDread": "256MB/s", "HDDwrite": "256MB/s", "RPM": "7200", "Score": ""},

            {"HDDtype": "HDD", "HDDname": "WD Blue 5400", "HDDManufacturer": "WesternDigital", "HDDformat": "3.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "500GB - 6TB", "HDDread": "180MB/s", "HDDwrite": "180MB/s", "RPM": "5400", "Score": ""},

            {"HDDtype": "SSHD", "HDDname": "FireCuda™ Hybrid", "HDDManufacturer": "Seagate", "HDDformat": "3.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "1TB, 2TB", "HDDread": "210MB/s", "HDDwrite": "210MB/s", "RPM": "7200", "Score": ""},

            {"HDDtype": "HDD", "HDDname": "BarraCuda®", "HDDManufacturer": "Seagate", "HDDformat": "3.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "500GB-8TB", "HDDread": "180MB/s", "HDDwrite": "180MB/s", "RPM": "5400", "Score": ""},

            {"HDDtype": "SSD", "HDDname": "FireCuda® 520", "HDDManufacturer": "Seagate", "HDDformat": "M.2 2280",
             "HDDinterface": "NVMe™ PCIe Gen 4.0", "HDD capacity": "2TB, 1TB, 500GB", "HDDread": "5,000MB/s", "HDDwrite": "4,400MB/s", "Score": ""},

            {"HDDtype": "SSD", "HDDname": "BarraCuda® 510", "HDDManufacturer": "Seagate", "HDDformat": "M.2 2280",
             "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "1TB, 512GB, 256GB", "HDDread": "3,400MB/s", "HDDwrite": "2,180MB/s", "Score": ""},

            {"HDDtype": "SSD", "HDDname": "BarraCuda® 120", "HDDManufacturer": "Seagate", "HDDformat": "2.5inch",
             "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "2TB, 1TB, 512GB, 256GB", "HDDread": "560MB/s", "HDDwrite": "540MB/s", "Score": ""}

            ]
    db.HDD.insert_many(data)
    print("Finish add")


def addMB():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [{"MBname": "", "Socket": "", "chipset": "", "ramslot": "", "Manufacturer": "",
             "DDR": "", "supportbus": "", "Audio": "", "Wirelesssupport": ""}
            ]
    db.Mainboard.insert_many(data)
    print("Finish add")


def addPSU():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [{"PSU name": "", "Power": "", "Certification": "",
             "Modular": "", "Form Factor": ""}

            ]
    db.PSU.insert_many(data)
    print("Finish add")


def addRAM():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [{"RAM name": "", "DDR": "", "BUS": "", "LC": "", "capacity": "", }
            ]
    db.RAM.insert_many(data)
    print("Finish add")


def addSink():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [{"Sink name": "", "Sink Type": "", "Socket": "", "FAN SPEED": "",
             "CONNECTOR": "", "Number of Fans": "", "HEATPIPES": ""}
            ]
    db.SinkCPU.insert_many(data)
    print("Finish add")


def addVGA():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [{"VGAname": "", "VRAM": "", "GDDR": "", "SPC": "", "PowerRequirment": "",
             "ShaderCore": "", "Core speed": "", "Memory Bus": "", "Series": "", "score": ""}
            ]
    db.VGA.insert_many(data)
    print("Finish add")


def reset():
    client = pymongo.MongoClient("mongodb+srv://voltexeez:HMlover3901@mobile-bir8b.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    test = db.CPU.remove()
    print("finish delete")


if __name__ == '__main__':
    #reset()
    #addCpu()
    addHdd()
    # addMB()
    # addPSU()
    # addRAM()
    # addSink()
    # addVGA()
