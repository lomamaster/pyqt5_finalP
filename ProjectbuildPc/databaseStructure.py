import pymongo


def addCpu():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        # i3
        {"CPUname": "i3-2130", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.40 GHz", "BoostClock": "none",
         "Microarchitecture": "Sandy Bridge", "Socket": "LGA1155", "Lithography": "32 nm", "Generation": "2nd gen", "Score": "1.43"},

        {"CPUname": "i3-3250", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "none",
         "Microarchitecture": "Ivy Bridge", "Socket": "LGA1155", "Lithography": "22 nm", "Generation": "3th gen", "Score": "1.51"},

        {"CPUname": "i3-4370", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "none",
         "Microarchitecture": "Devil's Canyon", "Socket": "LGA1150", "Lithography": "22 nm", "Generation": "4th Gen", "Score": "1.82"},

        {"CPUname": "i3-6300", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "none",
         "Microarchitecture": "Skylake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "6th Gen", "Score": "1.89"},

        {"CPUname": "i3-7350K", "Manufacturer": "Intel", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "4.20 GHz", "BoostClock": "none",
         "Microarchitecture": "Kaby Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "7th Gen", "Score": "2.14"},

        {"CPUname": "i3-8350K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "4.00 GHz", "BoostClock": "none",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "8th Gen", "Score": "2.68"},

        {"CPUname": "i3-9350KF", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "4.00 GHz", "BoostClock": "4.60 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": "2.91"},

        # i5
        {"CPUname": "i5-3570K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.40 GHz", "BoostClock": "3.80 GHz",
         "Microarchitecture": "Ivy Bridge", "Socket": "LGA1155", "Lithography": "22 nm", "Generation": "3th gen", "Score": "2.19"},

        {"CPUname": "i5-2550K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.40 GHz", "BoostClock": "3.80 GHz",
         "Microarchitecture": "Sandy Bridge", "Socket": "LGA1155", "Lithography": "32 nm", "Generation": "2nd gen", "Score": "2.07"},

        {"CPUname": "i5-760", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "2.80 GHz", "BoostClock": "3.33 GHz",
         "Microarchitecture": "Lynnfield", "Socket": "LGA1156", "Lithography": "45 nm", "Generation": "1st gen", "Score": "1.51"},

        {"CPUname": "i5-4690K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Devil's Canyon", "Socket": "LGA1150", "Lithography": "22 nm", "Generation": "4th Gen", "Score": "2.36"},

        {"CPUname": "i5-6600K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Skylake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "6th Gen", "Score": "2.48"},

        {"CPUname": "i5-7600K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Kaby Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "7th Gen", "Score": "2.66"},

        {"CPUname": "i5-8600K", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "6", "CoreClock": "3.60 GHz", "BoostClock": "4.30 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "8th Gen", "Score": "2.90"},

        {"CPUname": "i5-9600KF", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "6", "CoreClock": "3.70 GHz", "BoostClock": "4.60 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": "3.03"},

        # 7
        {"CPUname": "i7-880", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "3.06 GHz", "BoostClock": "3.73 GHz",
         "Microarchitecture": "Lynnfield", "Socket": "LGA1156", "Lithography": "45 nm", "Generation": "1st gen", "Score": "1.65"},

        {"CPUname": "i7-2700K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Sandy Bridge", "Socket": "LGA1155", "Lithography": "32 nm", "Generation": "2nd gen", "Score": "2.04"},

        {"CPUname": "i7-3770K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "3.50 GHz", "BoostClock": "3.90 GHz",
         "Microarchitecture": "Ivy Bridge", "Socket": "LGA1155", "Lithography": "22 nm", "Generation": "3th gen", "Score": "2.19"},

        {"CPUname": "i7-990X", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.46 GHz", "BoostClock": "3.73 GHz",
         "Microarchitecture": "Gulftown", "Socket": "LGA1366", "Lithography": "32 nm", "Generation": "1st genX", "Score": "1.96"},

        {"CPUname": "i7-4790k", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "4.00 GHz", "BoostClock": "4.40 GHz",
         "Microarchitecture": "Devil's Canyon", "Socket": "LGA1150", "Lithography": "22 nm", "Generation": "4th Gen", "Score": "2.54"},

        {"CPUname": "i7-6700K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "4.00 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Skylake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "6th Gen", "Score": "2.56"},

        {"CPUname": "i7-7700K", "Manufacturer": "Intel", "CoreCount": "4", "ThreadsCount": "8", "CoreClock": "4.20 GHz", "BoostClock": "4.50 GHz",
         "Microarchitecture": "Kaby Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "7th Gen", "Score": "2.79"},

        {"CPUname": "i7-8700K", "Manufacturer": "Intel", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.70 GHz", "BoostClock": "4.70 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "8th Gen", "Score": "2.96"},

        {"CPUname": "i7-9700KF", "Manufacturer": "Intel", "CoreCount": "8", "ThreadsCount": "8", "CoreClock": "3.60 GHz", "BoostClock": "4.90 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": "3.15"},

        # i9

        {"CPUname": "i9-9900KF", "Manufacturer": "Intel", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.60 GHz", "BoostClock": "5.00 GHz",
         "Microarchitecture": "Coffee Lake", "Socket": "LGA1151", "Lithography": "14 nm", "Generation": "9th Gen", "Score": "3.21"},

        # AMD
        {"CPUname": "Ryzen™ Threadripper™ 3990X", "Manufacturer": "AMD", "CoreCount": "64", "ThreadsCount": "128", "CoreClock": "2.90 GHz",
         "BoostClock": "4.30 GHz", "Microarchitecture": "Zen 2", "Socket": "sTRX4", "Lithography": "7 nm", "Generation": "3rd Gen", "Score": "4.38"},

        {"CPUname": "Ryzen™ Threadripper™ 2990WX", "Manufacturer": "AMD", "CoreCount": "32", "ThreadsCount": "64", "CoreClock": "3.00 ",
         "BoostClock": "4.20 GHz", "Microarchitecture": "Zen+", "Socket": "sTR4", "Lithography": "12 nm", "Generation": "2rd Gen", "Score": "3.41"},

        {"CPUname": "Ryzen™ Threadripper™ 1950X", "Manufacturer": "AMD", "CoreCount": "16", "ThreadsCount": "32", "CoreClock": "3.40 ",
         "BoostClock": "4.00 GHz", "Microarchitecture": "Zen", "Socket": "sTR4", "Lithography": "14 nm", "Generation": "1nd Gen", "Score": "3.26"},

        {"CPUname": "Ryzen™ 9 3900X", "Manufacturer": "AMD", "CoreCount": "12", "ThreadsCount": "24", "CoreClock": "3.80 GHz",
         "BoostClock": "4.60 GHz", "Microarchitecture": "Zen 2", "Socket": "sTR4", "Lithography": "7 nm", "Generation": "3st Gen", "Score": "3.01"},

        {"CPUname": "Ryzen™ 7 3800X", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.90 GHz",
         "BoostClock": "4.50 GHz", "Microarchitecture": "Zen 2", "Socket": "AM4", "Lithography": "7 nm", "Generation": "3rd Gen", "Score": "3.03"},

        {"CPUname": "Ryzen™ 7 2700X", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.70 GHz",
         "BoostClock": "4.30 GHz", "Microarchitecture": "Zen+", "Socket": "AM4", "Lithography": "12 nm", "Generation": "2nd Gen", "Score": "2.62"},

        {"CPUname": "Ryzen™ 7 1800X", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "16", "CoreClock": "3.60 GHz",
         "BoostClock": "4.00 GHz", "Microarchitecture": "Zen", "Socket": "AM4", "Lithography": "14 nm", "Generation": "1st Gen", "Score": "2.43"},

        {"CPUname": "Ryzen™ 5 3600X", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.80 GHz",
         "BoostClock": "4.20 GHz", "Microarchitecture": "Zen 2", "Socket": "AM4", "Lithography": "7 nm", "Generation": "3nd Gen", "Score": "2.91"},

        {"CPUname": "Ryzen™ 5 2600X", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.60 GHz",
         "BoostClock": "4.20 GHz", "Microarchitecture": "Zen+", "Socket": "AM4", "Lithography": "12 nm", "Generation": "2nd Gen", "Score": "2.54"},

        {"CPUname": "Ryzen™ 5 1600X", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "12", "CoreClock": "3.60 GHz",
         "BoostClock": "4.00 GHz", "Microarchitecture": "Zen", "Socket": "AM4", "Lithography": "14 nm", "Generation": "1st Gen", "Score": "2.37"},

        {"CPUname": "Ryzen™ 3 2300X", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "4.00 GHz",
         "Microarchitecture": "Zen+", "Socket": "AM4", "Lithography": "12 nm", "Generation": "2nd Gen", "Score": "2.16"},

        {"CPUname": "Ryzen™ 3 1300X", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.70 GHz",
         "Microarchitecture": "Zen", "Socket": "AM4", "Lithography": "14 nm", "Generation": "1st Gen", "Score": "2.22"},

        {"CPUname": "FX-9590", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "8", "CoreClock": "4.70 GHz", "BoostClock": "5.00 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": "1.68"},

        {"CPUname": "FX-8370", "Manufacturer": "AMD", "CoreCount": "8", "ThreadsCount": "8", "CoreClock": "4.00 GHz", "BoostClock": "4.30 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": "1.58"},

        {"CPUname": "FX-6350", "Manufacturer": "AMD", "CoreCount": "6", "ThreadsCount": "6", "CoreClock": "3.90 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": "1.44"},

        {"CPUname": "FX-4350", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "4.20 GHz", "BoostClock": "4.30 GHz",
         "Microarchitecture": "Piledriver", "Socket": "AM4", "Lithography": "32 nm", "Generation": "Vishera", "Score": "1.39"},

        {"CPUname": "Athlon™ 3000G", "Manufacturer": "AMD", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "none",
         "Microarchitecture": "Raven", "Socket": "AM4", "Lithography": "14 nm", "Generation": "7th Gen", "Score": "1.77"},

        {"CPUname": "Athlon™ 240GE", "Manufacturer": "AMD", "CoreCount": "2", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "none",
         "Microarchitecture": "Raven", "Socket": "AM4", "Lithography": "14 nm", "Generation": "7th Gen", "Score": "1.75"},

        {"CPUname": "Athlon™ X4 970", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "4.00 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": "1.34"},

        {"CPUname": "A6-9550", "Manufacturer": "AMD", "CoreCount": "2", "ThreadsCount": "2", "CoreClock": "3.80 GHz", "BoostClock": "4.00 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": "1.0"},

        {"CPUname": "A8-9600", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.10 GHz", "BoostClock": "3.40 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": "1.30"},

        {"CPUname": "A10-9700", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.50 GHz", "BoostClock": "3.80 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": "1.40"},

        {"CPUname": "A12-9800", "Manufacturer": "AMD", "CoreCount": "4", "ThreadsCount": "4", "CoreClock": "3.80 GHz", "BoostClock": "4.20 GHz",
         "Microarchitecture": "Bristol Ridge", "Socket": "AM4", "Lithography": "28 nm", "Generation": "7th Gen", "Score": "1.53"},
    ]
    db.CPU.insert_many(data)
    print("Finish add")


def addHdd():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        {"HDDtype": "SSD", "HDDname": "BarraCuda® 120", "HDDManufacturer": "Seagate", "HDDformat": "SSD 2.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "2TB, 1TB, 512GB, 256GB", "HDDread": "560MB/s", "HDDwrite": "540MB/s",
         "Score": "0.87"},

        {"HDDtype": "SSD", "HDDname": "KC600", "HDDManufacturer": "Kingston", "HDDformat": "SSD 2.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "256GB, 512GB, 1024GB, 2048GB", "HDDread": "550MB/s", "HDDwrite": "520MB/s",
         "Score": "0.87"},

        {"HDDtype": "SSD", "HDDname": "860 EVO", "HDDManufacturer": "samsung", "HDDformat": "SSD 2.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB, 4TB", "HDDread": "550MB/s", "HDDwrite": "520MB/s",
         "Score": "0.89"},

        {"HDDtype": "SSD", "HDDname": "WD BLUE 2.5", "HDDManufacturer": "WesternDigital", "HDDformat": "SSD 2.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB, 4TB", "HDDread": "560MB/s", "HDDwrite": "530MB/s",
         "Score": "0.85"},

        # M.2
        {"HDDtype": "SSD", "HDDname": "KC2000", "HDDManufacturer": "Kingston", "HDDformat": "M.2 2280",
         "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB", "HDDread": "3,200MB/s", "HDDwrite": "2,200MB/s",
         "Score": "0.95"},

        {"HDDtype": "SSD", "HDDname": "970 EVO Plus", "HDDManufacturer": "samsung", "HDDformat": "M.2 2280",
         "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB", "HDDread": "3,500 MB/s", "HDDwrite": "3,300 MB/s",
         "Score": "1.0"},

        {"HDDtype": "SSD", "HDDname": "WD BLUE 2280", "HDDManufacturer": "WesternDigital", "HDDformat": "M.2 2280",
         "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB", "HDDread": "2,400MB/s", "HDDwrite": "950MB/s",
         "Score": "0.9"},

        {"HDDtype": "SSD", "HDDname": "WD BLACK 2280", "HDDManufacturer": "WesternDigital", "HDDformat": "M.2 2280",
         "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "250GB, 500GB, 1TB, 2TB", "HDDread": "3,400MB/s", "HDDwrite": "2,900MB/s",
         "Score": "0.99"},

        {"HDDtype": "SSD", "HDDname": "FireCuda® 520", "HDDManufacturer": "Seagate", "HDDformat": "M.2 2280",
         "HDDinterface": "NVMe™ PCIe Gen 4.0", "HDD capacity": "2TB, 1TB, 500GB", "HDDread": "5,000MB/s", "HDDwrite": "4,400MB/s",
         "Score": "1.20"},

        {"HDDtype": "SSD", "HDDname": "BarraCuda® 510", "HDDManufacturer": "Seagate", "HDDformat": "M.2 2280",
         "HDDinterface": "NVMe™ PCIe Gen 3.0", "HDD capacity": "1TB, 512GB, 256GB", "HDDread": "3,400MB/s", "HDDwrite": "2,180MB/s",
         "Score": "0.99"},

        # HDD
        {"HDDtype": "HDD", "HDDname": "WD Black 3.5", "HDDManufacturer": "WesternDigital", "HDDformat": "3.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "500GB - 6TB", "HDDread": "256MB/s", "HDDwrite": "256MB/s", "RPM": "7200", "Score": "0.70"},

        {"HDDtype": "HDD", "HDDname": "WD Blue 5400", "HDDManufacturer": "WesternDigital", "HDDformat": "3.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "500GB - 6TB", "HDDread": "180MB/s", "HDDwrite": "180MB/s", "RPM": "5400", "Score": "0.58"},

        {"HDDtype": "HDD", "HDDname": "BarraCuda®", "HDDManufacturer": "Seagate", "HDDformat": "3.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "500GB-8TB", "HDDread": "180MB/s", "HDDwrite": "180MB/s", "RPM": "5400", "Score": "0.60"},

        {"HDDtype": "SSHD", "HDDname": "FireCuda™ Hybrid", "HDDManufacturer": "Seagate", "HDDformat": "3.5inch",
         "HDDinterface": "SATA Rev. 3.0", "HDD capacity": "1TB, 2TB", "HDDread": "210MB/s", "HDDwrite": "210MB/s", "RPM": "7200", "Score": "0.80"},

    ]
    db.HDD.insert_many(data)
    print("Finish add")


def addMB():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        {"MBname": "A320M-HDV R4.0", "Socket": "AM4", "chipset": "A320", "ramslot": "2", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-3200",
         "Audio": "7.1 CH Realtek ALC887  ", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "AB350 Pro4", "Socket": "AM4", "chipset": "AB350", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-3200",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "X370 Taichi", "Socket": "AM4", "chipset": "X370", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-3200",
         "Audio": "7.1 CH H Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "B450 Steel Legend", "Socket": "AM4", "chipset": "B450", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-3200",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "X470 Taichi Ultimate", "Socket": "AM4", "chipset": "X470", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-3200",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "X570 Creator", "Socket": "AM4", "chipset": "X570", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-4666",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "Fatal1ty X399 Professional Gaming", "Socket": "TR4", "chipset": "X399", "ramslot": "8", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-3600",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "H110M-HDV R3.0", "Socket": "LGA1151", "chipset": "H110", "ramslot": "2", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-2400",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "H270 Pro4", "Socket": "LGA1151", "chipset": "H270", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-2400",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1.05"},

        {"MBname": "Z270 Pro4", "Socket": "LGA1151", "chipset": "Z270", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4",
         "supportbus": "2133-3733", "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "H310CM-HDV/M.2", "Socket": "LGA1151", "chipset": "H310", "ramslot": "2", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "B360 Pro4", "Socket": "LGA1151", "chipset": "B360", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "B365M-HDV", "Socket": "LGA1151", "chipset": "B365", "ramslot": "2", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "Fatal1ty H370 Performance", "Socket": "LGA1151", "chipset": "H370", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "none", "Score": "1.05"},

        {"MBname": "Z370 Pro4", "Socket": "LGA1151", "chipset": "Z370", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-4266",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "Z390 Extreme4", "Socket": "LGA1151", "chipset": "Z390", "ramslot": "4", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-4300",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "X299 Taichi CLX", "Socket": "LGA2066", "chipset": "X299", "ramslot": "8", "Manufacturer": "ASRock", "DDR": "4", "supportbus": "2133-4200",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "TUF B450-PRO GAMING", "Socket": "AM4", "chipset": "B450", "ramslot": "4", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-3533",
         "Audio": "7.1 CH Realtek ALC S1200A", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "ROG Crosshair VIII Hero WI-FI", "Socket": "AM4", "chipset": "X570", "ramslot": "4", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-4800",
         "Audio": "7.1 CH ESS ES9023P", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "ROG STRIX X399-E GAMING", "Socket": "TR4", "chipset": "X399", "ramslot": "8", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-3600",
         "Audio": "7.1 CH SupremeFX S1220A", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "ROG Zenith II Extreme", "Socket": "sTRX4", "chipset": "TRX40", "ramslot": "8", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-4733",
         "Audio": "7.1 CH SupremeFX S1220A", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "ROG STRIX X470-F GAMING", "Socket": "AM4", "chipset": "X470", "ramslot": "4", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-3466",
         "Audio": "7.1 CH SupremeFX S1220A", "Wirelesssupport": "none", "Score": "1.15"},

        {"MBname": "Pro WS C422-ACE", "Socket": "LGA2066", "chipset": "C422", "ramslot": "8", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-2933",
         "Audio": "7.1 CH Realtek S1220A", "Wirelesssupport": "none", "Score": "1.15"},

        {"MBname": "Pro WS C246-ACE", "Socket": "LGA1151", "chipset": "C246", "ramslot": "4", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC S1220A", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "ROG STRIX B360-G GAMING", "Socket": "LGA1151", "chipset": "B360", "ramslot": "4", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH SupremeFX S1220A", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "EX-B365M-V", "Socket": "LGA1151", "chipset": "B365", "ramslot": "2", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "PRIME H310M-D", "Socket": "LGA1151", "chipset": "H310", "ramslot": "2", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "TUF H370-PRO GAMING WI-FI", "Socket": "LGA1151", "chipset": "H370", "ramslot": "4", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "on", "Score": "1.05"},

        {"MBname": "ROG MAXIMUS XI CODE", "Socket": "LGA1151", "chipset": "Z390", "ramslot": "4", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-4400",
         "Audio": "7.1 CH SupremeFX S1220 ", "Wirelesssupport": "on", "Score": "1.1"},

        {"MBname": "Prime X299 Edition 30", "Socket": "LGA2066", "chipset": "X299", "ramslot": "8", "Manufacturer": "Asus", "DDR": "4", "supportbus": "2133-4266",
         "Audio": "7.1 CH Realtek S1220A", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "MPG Z390 GAMING EDGE AC", "Socket": "LGA1151", "chipset": "Z390", "ramslot": "4", "Manufacturer": "msi", "DDR": "4", "supportbus": "2133-4400",
         "Audio": "7.1 CH Realtek ALC1220P", "Wirelesssupport": "on", "Score": "1.1"},

        {"MBname": "H370 GAMING PRO CARBON", "Socket": "LGA1151", "chipset": "H370", "ramslot": "4", "Manufacturer": "msi", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "none", "Score": "1.05"},

        {"MBname": "Z370 KRAIT GAMING", "Socket": "LGA1151", "chipset": "Z370", "ramslot": "4", "Manufacturer": "msi", "DDR": "4", "supportbus": "2133-4000",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "990FXA-GD80", "Socket": "AM3", "chipset": "SB950", "ramslot": "4", "Manufacturer": "msi", "DDR": "3", "supportbus": "800-2133",
         "Audio": "7.1 CH Realtek ALC892",
         "Wirelesssupport": "none", "Score": "1.05"},

        {"MBname": "MPG X570 GAMING EDGE WIFI", "Socket": "AM4", "chipset": "X570", "ramslot": "4", "Manufacturer": "msi", "DDR": "4", "supportbus": "1866-4400",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "G41M-P33 Combo", "Socket": "LGA775", "chipset": "G41", "ramslot": "4", "Manufacturer": "msi", "DDR": "3", "supportbus": "667-1333",
         "Audio": "5.1 CH Realtek ALC662", "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "H81I", "Socket": "LGA 1150", "chipset": "H81", "ramslot": "2", "Manufacturer": "msi", "DDR": "3", "supportbus": "1066-1600", "Audio": "7.1 CH Realtek ALC887",
         "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "H270 TOMAHAWK ARCTIC", "Socket": "LGA1151", "chipset": "H270", "ramslot": "4", "Manufacturer": "msi", "DDR": "4", "supportbus": "2133-2400",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1.05"},

        {"MBname": "H310M PRO-VDH", "Socket": "LGA1151", "chipset": "H310", "ramslot": "2", "Manufacturer": "msi", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "B360 GAMING PRO CARBON", "Socket": "LGA1151", "chipset": "B360", "ramslot": "4", "Manufacturer": "msi", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "MEG X299 CREATION", "Socket": "LGA2066", "chipset": "X299", "ramslot": "8", "Manufacturer": "msi", "DDR": "4", "supportbus": "2133-4200",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "GA-AM1M-S2H (rev. 1.1)", "Socket": "FS1b", "chipset": "AM1", "ramslot": "2", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1333-1600",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.0"},

        {"MBname": "GA-F2A68HM-D3H (rev. 1.0)", "Socket": "FM2+", "chipset": "A68H", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1333-2400",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.0"},

        {"MBname": "GA-F2A78M-DASHV (rev. 1.0)", "Socket": "FM2+", "chipset": "A78", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1333-2400",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "GA-F2A88X-D3HP (rev. 1.0)", "Socket": "FM2+", "chipset": "A88X", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1333-2400",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "GA-990FX-Gaming (rev. 1.1)", "Socket": "AM3+", "chipset": "990FX", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1066-2000",
         "Audio": "7.1 CH Realtek ALC1150", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "GA-AX370-Gaming K7 (rev. 1.0)", "Socket": "AM4", "chipset": "X370", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-3600",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "X470 AORUS GAMING 7 WIFI (rev. 1.1)", "Socket": "AM4", "chipset": "X470", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-4133",
         "Audio": "7.1 CH Realtek ALC1220-VB", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "X399 AORUS XTREME (rev. 1.0)", "Socket": "TR4", "chipset": "X399", "ramslot": "8", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-3600",
         "Audio": "7.1 CH Realtek ALC1220-VB", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "X570 AORUS XTREME (rev. 1.x)", "Socket": "AM4", "chipset": "X570", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-4400",
         "Audio": "7.1 CH Realtek ALC1220-VB", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "TRX40 DESIGNARE (rev. 1.0)", "Socket": "sTRX4", "chipset": "TRX40", "ramslot": "8", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-4400",
         "Audio": "7.1 CH Realtek ALC4050H", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "G1.Assassin 2 (rev. 1.0)", "Socket": "LGA2011", "chipset": "X79", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1066-2400",
         "Audio": "7.1 CH Creative CA20K2", "Wirelesssupport": "none", "Score": "1.15"},

        {"MBname": "GA-Q87M-MK (rev. 1.1)", "Socket": "LGA1150", "chipset": "Q87", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1333-1600",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1"},

        {"MBname": "GA-Z87P-D3 (rev. 2.0)", "Socket": "LGA1150", "chipset": "Z87", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1333-3000",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "GA-Z97X-Game Plus (rev. 1.0)", "Socket": "LGA1150", "chipset": "Z97", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "3", "supportbus": "1333-3200",
         "Audio": "7.1 CH Realtek ALC1150", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "GA-X99-Phoenix SLI (rev. 1.0)", "Socket": "LGA2011-3", "chipset": "X99", "ramslot": "8", "Manufacturer": "GIGABYTE", "DDR": "4",
         "supportbus": "2133-3600", "Audio": "7.1 CH Realtek ALC1150", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "GA-Q170M-MK (rev. 1.0)", "Socket": "LGA1151", "chipset": "Q170", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.0"},

        {"MBname": "GA-Z170X-SOC FORCE (rev. 1.0)", "Socket": "LGA1151", "chipset": "Z170", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-3866",
         "Audio": "7.1 CH Realtek  ALC1150", "Wirelesssupport": "none", "Score": "1.1"},

        {"MBname": "GA-Gaming B8 (rev. 1.0)", "Socket": "LGA1151", "chipset": "B250", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-2400",
         "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "none", "Score": "1.0"},

        {"MBname": "GA-Z270X-Gaming 9 (rev. 1.0)", "Socket": "LGA1151", "chipset": "Z270", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-4133",
         "Audio": "7.1 CH Creative Sound Core 3D", "Wirelesssupport": "on", "Score": "1.1"},

        {"MBname": "Z370 AORUS ULTRA GAMING WIFI-OP (rev. 1.0)", "Socket": "LGA1151", "chipset": "Z370", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4",
         "supportbus": "2133-4000", "Audio": "7.1 CH Realtek ALC1220", "Wirelesssupport": "on", "Score": "1.1"},

        {"MBname": "X299X AORUS XTREME WATERFORCE (rev. 1.0)", "Socket": "LGA2066", "chipset": "X299", "ramslot": "8", "Manufacturer": "GIGABYTE", "DDR": "4",
         "supportbus": "2133-4333", "Audio": "7.1 CH Realtek ALC1220-VB", "Wirelesssupport": "on", "Score": "1.15"},

        {"MBname": "H310M D3H 2.0 (rev. 1.0)", "Socket": "LGA1151", "chipset": "H310", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC887", "Wirelesssupport": "none", "Score": "1.01"},

        {"MBname": "H370M D3H GSM (rev. 1.0)", "Socket": "LGA1151", "chipset": "H370", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4", "supportbus": "2133-2666",
         "Audio": "7.1 CH Realtek ALC892", "Wirelesssupport": "none", "Score": "1.05"},

        {"MBname": "Z390 AORUS MASTER G2 Edition (rev. 1.0)", "Socket": "LGA1151", "chipset": "Z390", "ramslot": "4", "Manufacturer": "GIGABYTE", "DDR": "4",
         "supportbus": "2133-4400", "Audio": "7.1 CH Realtek ALC1220-VB", "Wirelesssupport": "on", "Score": "1.1"},
    ]
    db.Mainboard.insert_many(data)
    print("Finish add")


def addPSU():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        {"PSU name": "HXi Series™ HX750i", "Power": "750 Watts", "Certification": "80 Plus® PLATINUM", "Modular": "Fully", "Form Factor": "ATX", "Score": "1.05"},

        {"PSU name": "VENGEANCE Series™ 650M", "Power": "650 Watts", "Certification": "80 PLUS® Silver", "Modular": "Semi", "Form Factor": "ATX", "Score": "1.00"},

        {"PSU name": "ROG-THOR-1200P", "Power": "1200 Watts", "Certification": "80 Plus® PLATINUM", "Modular": "Fully", "Form Factor": "ATX", "Score": "1.05"},

        {"PSU name": "Toughpower SFX 450W Gold", "Power": "450 Watts", "Certification": "80 PLUS® Gold", "Modular": "Fully", "Form Factor": "ATX", "Score": "1.03"},

        {"PSU name": "Toughpower GF1 ARGB 650W Gold - TT Premium Edition", "Power": "650 Watts", "Certification": "80 PLUS® Gold", "Modular": "Fully", "Form Factor": "ATX",
         "Score": "1.03"},

        {"PSU name": "Thermaltake Toughpower Grand RGB 750W Gold (RGB Sync Edition)", "Power": "750 Watts", "Certification": "80 PLUS® Gold", "Modular": "Fully",
         "Form Factor": "ATX", "Score": "1.03"}
    ]
    db.PSU.insert_many(data)
    print("Finish add")


def addRAM():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        {"RAM name": "HyperX FURY", "Manufacturer": "KINGSTON", "DDR": "3", "BUS": "1333", "CL": "9-10-10-10", "capacity": "4 GB", "Score": "1.05"},

        {"RAM name": "HyperX FURY", "Manufacturer": "KINGSTON", "DDR": "3", "BUS": "1600", "CL": "9-10-10-10", "capacity": "8 GB", "Score": "1.06"},

        {"RAM name": "HyperX FURY", "Manufacturer": "KINGSTON", "DDR": "3", "BUS": "1866", "CL": "9-10-10-10", "capacity": "16 GB", "Score": "1.07"},

        {"RAM name": "HyperX FURY BLACK", "Manufacturer": "KINGSTON", "DDR": "4", "BUS": "2666", "CL": "16-18-18-18", "capacity": "4 GB", "Score": "1.16"},

        {"RAM name": "HyperX FURY BLACK", "Manufacturer": "KINGSTON", "DDR": "4", "BUS": "2666", "CL": "16-18-18-18", "capacity": "8 GB", "Score": "1.16"},

        {"RAM name": "HyperX FURY BLACK", "Manufacturer": "KINGSTON", "DDR": "4", "BUS": "3200", "CL": "16-18-18-18", "capacity": "16 GB", "Score": "1.175"},

        {"RAM name": "TOUGHRAM Z-ONE RGB", "Manufacturer": "THERMALTAKE", "DDR": "4", "BUS": "3600", "CL": "18-18-18-18", "capacity": "8 GB", "Score": "1.80"},

        {"RAM name": "M-ONE Gaming", "Manufacturer": "THERMALTAKE", "DDR": "4", "BUS": "2666", "CL": "19-19-19-19", "capacity": "8 GB", "Score": "1.16"},

        {"RAM name": "Ripjaws V", "Manufacturer": "G.SKILL", "DDR": "4", "BUS": "3200", "CL": "16-18-18-38", "capacity": "32 GB", "Score": "1.175"},

        {"RAM name": "Aegis", "Manufacturer": "G.SKILL", "DDR": "4", "BUS": "2666", "CL": "19-19-19-43", "capacity": "16 GB", "Score": "1.16"},

        {"RAM name": "Value", "Manufacturer": "G.SKILL", "DDR": "4", "BUS": "2666", "CL": "19-19-19-43", "capacity": "8 GB", "Score": "1.16"},

        {"RAM name": "Vengeance LP", "Manufacturer": "CORSAIR", "DDR": "3", "BUS": "1600", "CL": "10-10-10-27", "capacity": "8 GB", "Score": "1.06"},

        {"RAM name": "XMS3", "Manufacturer": "CORSAIR", "DDR": "3", "BUS": "1600", "CL": "9-9-9-24", "capacity": "2 GB", "Score": "1.06"},

        {"RAM name": "VENGEANCE LPX", "Manufacturer": "CORSAIR", "DDR": "4", "BUS": "3000", "CL": "16-20-20-38", "capacity": "16 GB", "Score": "1.7"},

        {"RAM name": "VALUE SELECT", "Manufacturer": "CORSAIR", "DDR": "4", "BUS": "2400", "CL": "16-16-16-39", "capacity": "8 GB", "Score": "1.15"}
    ]
    db.RAM.insert_many(data)
    print("Finish add")


def addSink():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        # Water cooling
        {"Sink name": "Kraken Z73", "Sink Type": "Water cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "3", "pump speed": "2800 RPM", "Score":"1.07"},

        {"Sink name": "Kraken Z63", "Sink Type": "Water cooling", "FAN SPEED": "1800 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "2", "pump speed": "2800 RPM", "Score":"1.06"},

        {"Sink name": "Kraken M22", "Sink Type": "Water cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "pump speed": "3000 RPM", "Score":"1.05"},

        {"Sink name": "ROG Strix LC 120", "Sink Type": "Water cooling", "FAN SPEED": "2500 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "pump speed": "Automatic", "Score":"1.05"},

        {"Sink name": "ROG RYUO 240", "Sink Type": "Water cooling", "FAN SPEED": "2500 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "2", "pump speed": "Automatic", "Score":"1.06"},

        {"Sink name": "ROG RYUJIN 360", "Sink Type": "Water cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "3", "pump speed": "Automatic", "Score":"1.07"},

        {"Sink name": "Floe DX RGB 360 TT Premium Edition", "Sink Type": "Water cooling", "FAN SPEED": "1500 RPM", "CONNECTOR": "9-pin", "Number of Fans": "3", "pump speed": "3600 RPM", "Score":"1.07"},

        {"Sink name": "Floe DX RGB 240 TT Premium Edition", "Sink Type": "Water cooling", "FAN SPEED": "1500 RPM", "CONNECTOR": "9-pin", "Number of Fans": "2", "pump speed": "3600 RPM", "Score":"1.06"},

        {"Sink name": "Water 3.0 120 ARGB Sync", "Sink Type": "Water cooling", "FAN SPEED": "1500 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "pump speed": "3000 RPM", "Score":"1.05"},

        {"Sink name": "MASTERLIQUID ML240P MIRAGE", "Sink Type": "Water cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "2", "pump speed": "3000 RPM", "Score":"1.06"},

        {"Sink name": "MASTERLIQUID ML120L RGB TUF GAMING EDITION", "Sink Type": "Water cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "3-pin,4-pin", "Number of Fans": "1",
         "pump speed": "2800 RPM", "Score":"1.05"},

        {"Sink name": "Hydro Series™ H150i PRO RGB", "Sink Type": "Water cooling", "FAN SPEED": "1600 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "3", "pump speed": "2850 RPM", "Score":"1.07"},

        {"Sink name": "Hydro Series™ H100i RGB PLATINUM SE", "Sink Type": "Water cooling", "FAN SPEED": "2200 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "2",
         "pump speed": "2850 RPM", "Score":"1.06"},

        {"Sink name": "Hydro Series™ H60 (2018) 120mm Liquid CPU Cooler", "Sink Type": "Water cooling", "FAN SPEED": "1700 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1",
         "pump speed": "2850 RPM", "Score":"1.05"},

        {"Sink name": "P7-L240 RGB LIQUID COOLER", "Sink Type": "Water cooling", "FAN SPEED": "1800 RPM", "CONNECTOR": "3-pin,4-Pin", "Number of Fans": "2", "pump speed": "2500 RPM", "Score":"1.06"},

        {"Sink name": "PLUSE L120F", "Sink Type": "Water cooling", "FAN SPEED": "1600 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "pump speed": "2800 RPM", "Score":"1.05"},

        {"Sink name": "LIKAI240", "Sink Type": "Water cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "3-pin,4-pin", "Number of Fans": "2", "pump speed": " 2500 RPM", "Score":"1.06"},

        {"Sink name": "DEEPCOOL Castle 280 RGB", "Sink Type": "Water cooling", "FAN SPEED": "1800 RPM", "CONNECTOR": "3-pin,4-pin", "Number of Fans": "2", "pump speed": "2550 RPM", "Score":"1.06"},

        {"Sink name": "DEEPCOOL GAMMAXX L360 RGB V2", "Sink Type": "Water cooling", "FAN SPEED": "1800 RPM", "CONNECTOR": "3-pin,4-pin", "Number of Fans": "3", "pump speed": "2550 RPM", "Score":"1.07"},

        # Air cooling
        {"Sink name": "Engine 27", "Sink Type": "Air cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4 pin PWM", "Number of Fans": "1", "HEATPIPES": "1", "Score":"1.01"},

        {"Sink name": "UX100 ARGB Lighting CPU Cooler", "Sink Type": "Air cooling", "FAN SPEED": "1800 RPM", "CONNECTOR": "2-pin,3-pin", "Number of Fans": "1", "HEATPIPES": "1", "Score":"1.01"},

        {"Sink name": "UX200 ARGB Lighting CPU Cooler", "Sink Type": "Air cooling", "FAN SPEED": "1500 RPM", "CONNECTOR": "2-pin,4-pin", "Number of Fans": "1", "HEATPIPES": "4", "Score":"1.03"},

        {"Sink name": "MASTERAIR MA610P WITH RGB CONTROLLER", "Sink Type": "Air cooling", "FAN SPEED": "1800 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "6", "Score":"1.04"},

        {"Sink name": "MASTERAIR MA620M", "Sink Type": "Air cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "6", "Score":"1.04"},

        {"Sink name": "COOLER MASTER WRAITH RIPPER", "Sink Type": "Air cooling", "FAN SPEED": "2750 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "7", "Score":"1.05"},

        {"Sink name": "HYPER 212 LED TURBO WHITE EDITION", "Sink Type": "Air cooling", "FAN SPEED": "1600 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "2", "HEATPIPES": "4", "Score":"1.03"},

        {"Sink name": "MASTERAIR G100M", "Sink Type": "Air cooling", "FAN SPEED": "2400 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "1", "Score":"1.01"},

        {"Sink name": "A500 Dual Fan CPU Cooler", "Sink Type": "Air cooling", "FAN SPEED": "2400 RPM", "CONNECTOR": "4-pin*2", "Number of Fans": "2", "HEATPIPES": "4", "Score":"1.03"},

        {"Sink name": "VERKHO5", "Sink Type": "Air cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "5", "Score":"1.035"},

        {"Sink name": "VERKHO4 LITE", "Sink Type": "Air cooling", "FAN SPEED": "2000 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "4", "Score":"1.03"},

        {"Sink name": "DEEPCOOL GAMMAXX GTE", "Sink Type": "Air cooling", "FAN SPEED": "1500 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "4", "Score":"1.03"},

        {"Sink name": "DEEPCOOL FRYZEN TR4", "Sink Type": "Air cooling", "FAN SPEED": "1800 RPM", "CONNECTOR": "3-pin,4-pin", "Number of Fans": "1", "HEATPIPES": "6", "Score":"1.04"},

        {"Sink name": "DEEPCOOL GAMMAXX GT A RGB", "Sink Type": "Air cooling", "FAN SPEED": "1500 RPM", "CONNECTOR": "4-pin PWM", "Number of Fans": "1", "HEATPIPES": "4", "Score":"1.03"}
    ]

    db.SinkCPU.insert_many(data)
    print("Finish add")


def addVGA():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [
        {"VGAname": "NVIDIA GeForce RTX 2080 Ti", "VRAM": "11 GB", "GDDR": "GDDR6", "SPC": "2x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "4352", "Core speed": "1545 MHz",
         "Memory Bus": "352 bit", "Series": "RTX 2000", "Architecture": "Turing", "Score": "45.72"},

        {"VGAname": "NVIDIA GeForce RTX 2080 SUPER", "VRAM": "8 GB", "GDDR": "GDDR6", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "3072",
         "Core speed": "1815 MHz", "Memory Bus": "256 bit", "Series": "RTX 2000", "Architecture": "Turing", "Score": "34.09"},

        {"VGAname": "NVIDIA GeForce RTX 2080", "VRAM": "8 GB", "GDDR": "GDDR6", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "215 W", "ShaderCore": "2944",
         "Core speed": "1710 MHz", "Memory Bus": "256 bit", "Series": "RTX 2000", "Architecture": "Turing", "Score": "32.19"},

        {"VGAname": "NVIDIA GeForce RTX 2070 SUPER", "VRAM": "8 GB", "GDDR": "GDDR6", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "215 W", "ShaderCore": "2560",
         "Core speed": "1770 MHz", "Memory Bus": "256 bit", "Series": "RTX 2000", "Architecture": "Turing", "Score": "28.79"},

        {"VGAname": "NVIDIA GeForce RTX 2070", "VRAM": "8 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "175 W", "ShaderCore": "2304", "Core speed": "1620 MHz",
         "Memory Bus": "256 bit", "Series": "RTX 2000", "Architecture": "Turing", "Score": "28.55"},

        {"VGAname": "NVIDIA GeForce RTX 2060 SUPER", "VRAM": "8 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "160 W", "ShaderCore": "2176", "Core speed": "1650 MHz",
         "Memory Bus": "256 bit", "Series": "RTX 2000", "Architecture": "Turing", "Score": "26.29"},

        {"VGAname": "NVIDIA GeForce RTX 2060", "VRAM": "6 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "160 W", "ShaderCore": "1920", "Core speed": "1680 MHz",
         "Memory Bus": "192 bit", "Series": "RTX 2000", "Architecture": "Turing", "Score": "22.76"},

        {"VGAname": "NVIDIA GeForce GTX 1660 Ti", "VRAM": "6 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "120 W", "ShaderCore": "1536", "Core speed": "1770 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 1600", "Architecture": "Turing", "Score": "19.75"},

        {"VGAname": "NVIDIA GeForce GTX 1660 SUPER", "VRAM": "6 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "125 W", "ShaderCore": "1408", "Core speed": "1785 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 1600", "Architecture": "Turing", "Score": "18.63"},

        {"VGAname": "NVIDIA GeForce GTX 1660", "VRAM": "6 GB", "GDDR": "GDDR5", "SPC": "1x 8-pin", "PowerRequirment": "120 W", "ShaderCore": "1408", "Core speed": "1785 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 1600", "Architecture": "Turing", "Score": "16.71"},

        {"VGAname": "NVIDIA GeForce GTX 1650 SUPER", "VRAM": "4 GB", "GDDR": "GDDR6", "SPC": "1x 6-pin", "PowerRequirment": "100 W", "ShaderCore": "1280", "Core speed": "1725 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 1600", "Architecture": "Turing", "Score": "15.52"},

        {"VGAname": "NVIDIA GeForce GTX 1650", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "75 W", "ShaderCore": "896", "Core speed": "1665 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 1600", "Architecture": "Turing", "Score": "10.85"},

        {"VGAname": "NVIDIA GeForce GTX 1080 Ti", "VRAM": "11 GB", "GDDR": "GDDR5X", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "3584",
         "Core speed": "1582 MHz", "Memory Bus": "352 bit", "Series": "GTX 1000", "Architecture": "Pascal", "Score": "35.27"},

        {"VGAname": "NVIDIA GeForce GTX 1080", "VRAM": "8 GB", "GDDR": "GDDR5X", "SPC": "1x 8-pin", "PowerRequirment": "180 W", "ShaderCore": "2560", "Core speed": "1733 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 1000", "Architecture": "Pascal", "Score": "28.06"},

        {"VGAname": "NVIDIA GeForce GTX 1070 Ti", "VRAM": "8 GB", "GDDR": "GDDR5", "SPC": "1x 8-pin", "PowerRequirment": "180 W", "ShaderCore": "2432", "Core speed": "1683 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 1000", "Architecture": "Pascal", "Score": "25.55"},

        {"VGAname": "NVIDIA GeForce GTX 1070", "VRAM": "8 GB", "GDDR": "GDDR5", "SPC": "1x 8-pin", "PowerRequirment": "150 W", "ShaderCore": "1920", "Core speed": "1683 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 1000", "Architecture": "Pascal", "Score": "20.94"},

        {"VGAname": "NVIDIA GeForce GTX 1060 6 GB", "VRAM": "6 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "120 W", "ShaderCore": "1280", "Core speed": "1709 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 1000", "Architecture": "Pascal", "Score": "15.19"},

        {"VGAname": "NVIDIA GeForce GTX 1050 Ti", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "75 W", "ShaderCore": "768", "Core speed": "1392 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 1000", "Architecture": "Pascal", "Score": "8.42"},

        {"VGAname": "NVIDIA GeForce GTX 1050", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "75 W", "ShaderCore": "640", "Core speed": "1455 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 1000", "Architecture": "Pascal", "Score": "7.35"},

        {"VGAname": "NVIDIA GeForce GT 1030", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "30 W", "ShaderCore": "384", "Core speed": "1468 MHz",
         "Memory Bus": "64 bit", "Series": "GT 1000", "Architecture": "Pascal", "Score": "3.98"},

        {"VGAname": "NVIDIA GeForce GTX 980 Ti", "VRAM": "6 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "2816",
         "Core speed": "1076 MHz", "Memory Bus": "384 bit", "Series": "GTX 900", "Architecture": "Maxwell 2.0", "Score": "20.96"},

        {"VGAname": "NVIDIA GeForce GTX 980", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "165 W", "ShaderCore": "2048", "Core speed": "1216 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 900", "Architecture": "Maxwell 2.0", "Score": "16.11"},

        {"VGAname": "NVIDIA GeForce GTX 970", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "148 W", "ShaderCore": "1664", "Core speed": "1178 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 900", "Architecture": "Maxwell 2.0", "Score": "13.81"},

        {"VGAname": "NVIDIA GeForce GTX 960", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "120 W", "ShaderCore": "1024", "Core speed": "1178 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 900", "Architecture": "Maxwell 2.0", "Score": "8.73"},

        {"VGAname": "NVIDIA GeForce GTX 950", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "90 W", "ShaderCore": "768", "Core speed": "1188 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 900", "Architecture": "Maxwell 2.0", "Score": "7.07"},

        {"VGAname": "NVIDIA GeForce GTX 780 Ti 6 GB", "VRAM": "6 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "2880",
         "Core speed": "928 MHz", "Memory Bus": "GTX 700", "Series": "", "Architecture": "Kepler", "Score": "16.14"},

        {"VGAname": "NVIDIA GeForce GTX 780", "VRAM": "3 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "2304",
         "Core speed": "902 MHz", "Memory Bus": "384 bit", "Series": "GTX 700", "Architecture": "Kepler", "Score": "13.84"},

        {"VGAname": "NVIDIA GeForce GTX 770", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "230 W", "ShaderCore": "1536",
         "Core speed": "1085 MHz", "Memory Bus": "256 bit", "Series": "GTX 700", "Architecture": "Kepler", "Score": "10.88"},

        {"VGAname": "NVIDIA GeForce GTX 760 Ti", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "170 W", "ShaderCore": "1344", "Core speed": "980 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 700", "Architecture": "Kepler", "Score": "8.23"},

        {"VGAname": "NVIDIA GeForce GTX 760", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "170 W", "ShaderCore": "1152", "Core speed": "1032 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 700", "Architecture": "Kepler", "Score": "8.39"},

        {"VGAname": "NVIDIA GeForce GTX 750 Ti", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "60 W", "ShaderCore": "640", "Core speed": "1085 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 700", "Architecture": "Maxwell", "Score": "5.12"},

        {"VGAname": "NVIDIA GeForce GTX 750", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "55 W", "ShaderCore": "512", "Core speed": "1085 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 700", "Architecture": "Maxwell", "Score": "4.26"},

        {"VGAname": "NVIDIA GeForce GT 740", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "64 W", "ShaderCore": "384", "Core speed": "993 MHz",
         "Memory Bus": "128 bit", "Series": "GT 700", "Architecture": "Kepler", "Score": "2.44"},

        {"VGAname": "NVIDIA GeForce GT 730", "VRAM": "2 GB", "GDDR": "DDR3", "SPC": "None", "PowerRequirment": "49 W", "ShaderCore": "96", "Core speed": "700 MHz",
         "Memory Bus": "128 bit", "Series": "GT 700", "Architecture": "Fermi", "Score": "1.35"},

        {"VGAname": "NVIDIA GeForce GTX 690", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 8-pin", "PowerRequirment": "300 W", "ShaderCore": "1536", "Core speed": "1019 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 600", "Architecture": "Kepler", "Score": "9.00"},

        {"VGAname": "NVIDIA GeForce GTX 680", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "195 W", "ShaderCore": "1536", "Core speed": "1058 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 600", "Architecture": "Kepler", "Score": "10.08"},

        {"VGAname": "NVIDIA GeForce GTX 670", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "170 W", "ShaderCore": "1344", "Core speed": "980 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 600", "Architecture": "Kepler", "Score": "8.76"},

        {"VGAname": "NVIDIA GeForce GTX 660 Ti", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "150 W", "ShaderCore": "1344", "Core speed": "980 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 600", "Architecture": "Kepler", "Score": "8.44"},

        {"VGAname": "NVIDIA GeForce GTX 660", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "140 W", "ShaderCore": "960", "Core speed": "1032 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 600", "Architecture": "Kepler", "Score": "6.47"},

        {"VGAname": "NVIDIA GeForce GTX 650 Ti", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "110 W", "ShaderCore": "768", "Core speed": "928 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 600", "Architecture": "Kepler", "Score": "4.70"},

        {"VGAname": "NVIDIA GeForce GTX 650", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "65 W", "ShaderCore": "384", "Core speed": "1058 MHz",
         "Memory Bus": "128 bit", "Series": "GTX 600", "Architecture": "Kepler", "Score": "2.66"},

        {"VGAname": "NVIDIA GeForce GT 640 Rev. 2", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "49 W", "ShaderCore": "384", "Core speed": "1046 MHz",
         "Memory Bus": "64 bit", "Series": "GT 600", "Architecture": "Kepler 2.0", "Score": "2.09"},

        {"VGAname": "NVIDIA GeForce GT 630 Rev. 2", "VRAM": "2 GB", "GDDR": "DDR3", "SPC": "None", "PowerRequirment": "25 W", "ShaderCore": "384", "Core speed": "902 MHz",
         "Memory Bus": "64 bit", "Series": "GT 600", "Architecture": "Kepler 2.0", "Score": "1.12"},

        {"VGAname": "NVIDIA GeForce GTX 590", "VRAM": "1536 MB", "GDDR": "GDDR5", "SPC": "2x 8-pin", "PowerRequirment": "365 W", "ShaderCore": "512", "Core speed": "608 MHz",
         "Memory Bus": "384 bit", "Series": "GTX 500", "Architecture": "Fermi 2.0", "Score": "4.55"},

        {"VGAname": "NVIDIA GeForce GTX 580", "VRAM": "1536 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "244 W", "ShaderCore": "512",
         "Core speed": "772 MHz", "Memory Bus": "384 bit", "Series": "GTX 500", "Architecture": "Fermi 2.0", "Score": "5.67"},

        {"VGAname": "NVIDIA GeForce GTX 570", "VRAM": "1280 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "219 W", "ShaderCore": "480",
         "Core speed": "732 MHz", "Memory Bus": "320 bit", "Series": "GTX 500", "Architecture": "Fermi 2.0", "Score": "5.23"},

        {"VGAname": "NVIDIA GeForce GTX 560", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "150 W", "ShaderCore": "336", "Core speed": "810 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 500", "Architecture": "Fermi 2.0", "Score": "4.07"},

        {"VGAname": "NVIDIA GeForce GTX 560 Ti", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "170 W", "ShaderCore": "384", "Core speed": "823 MHz",
         "Memory Bus": "256 bit", "Series": "GTX 500", "Architecture": "Fermi 2.0", "Score": "4.85"},

        {"VGAname": "NVIDIA GeForce GTX 550 Ti", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "116 W", "ShaderCore": "192", "Core speed": "900 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 500", "Architecture": "Fermi 2.0", "Score": "2.65"},

        {"VGAname": "NVIDIA GeForce GT 530", "VRAM": "1024 MB", "GDDR": "DDR3", "SPC": "None", "PowerRequirment": "50 W", "ShaderCore": "96", "Core speed": "700 MHz",
         "Memory Bus": "128 bit", "Series": "GT 500", "Architecture": "Fermi", "Score": "1.01"},

        {"VGAname": "NVIDIA GeForce GTX 480", "VRAM": "1536 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "480",
         "Core speed": "701 MHz", "Memory Bus": "384 bit", "Series": "GTX 400", "Architecture": "Fermi", "Score": "5.01"},

        {"VGAname": "NVIDIA GeForce GTX 470", "VRAM": "1280 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "215 W", "ShaderCore": "448", "Core speed": "608 MHz",
         "Memory Bus": "320 bit", "Series": "GTX 400", "Architecture": "Fermi", "Score": "3.98"},

        {"VGAname": "NVIDIA GeForce GTX 460", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "160 W", "ShaderCore": "336", "Core speed": "779 MHz",
         "Memory Bus": "192 bit", "Series": "GTX 400", "Architecture": "Fermi 2.0", "Score": "4.03"},

        {"VGAname": "NVIDIA GeForce GTS 450 Rev. 3", "VRAM": "1024 MB", "GDDR": "DDR3", "SPC": "None", "PowerRequirment": "106 W", "ShaderCore": "144", "Core speed": "783 MHz",
         "Memory Bus": "128 bit", "Series": "GTS 400", "Architecture": "Fermi 2.0", "Score": "2.24"},

        {"VGAname": "NVIDIA GeForce GT 440", "VRAM": "1024 MB", "GDDR": "DDR3", "SPC": "None", "PowerRequirment": "65 W", "ShaderCore": "96", "Core speed": "810 MHz",
         "Memory Bus": "128 bit", "Series": "GT 400", "Architecture": "Fermi", "Score": "1.17"},

        {"VGAname": "AMD Radeon VII", "VRAM": "16 GB", "GDDR": "HBM2", "SPC": "2x 8-pin", "PowerRequirment": "295 W", "ShaderCore": "3840", "Core speed": "1750 MHz",
         "Memory Bus": "4096 bit", "Series": "VII", "Architecture": "GCN 5.1", "Score": "30.01"},

        {"VGAname": "AMD Radeon RX 5700", "VRAM": "8 GB", "GDDR": "GDDR6", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "180 W", "ShaderCore": "2304", "Core speed": "1725 MHz",
         "Memory Bus": "256 bit", "Series": "RX-5000", "Architecture": "RDNA 1.0", "Score": "23.58"},

        {"VGAname": "AMD Radeon RX 5700 XT", "VRAM": "8 GB", "GDDR": "GDDR6", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "225 W", "ShaderCore": "2560",
         "Core speed": "1905 MHz", "Memory Bus": "256 bit", "Series": "RX-5000", "Architecture": "RDNA 1.0", "Score": "28.28"},

        {"VGAname": "AMD Radeon RX 5600 XT", "VRAM": "6 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "150 W", "ShaderCore": "2304", "Core speed": "1560 MHz",
         "Memory Bus": "192 bit", "Series": "RX-5000", "Architecture": "RDNA 1.0", "Score": "22.52"},

        {"VGAname": "AMD Radeon RX 5500 XT", "VRAM": "4 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "130 W", "ShaderCore": "1408", "Core speed": "1845 MHz",
         "Memory Bus": "128 bit", "Series": "RX-5000", "Architecture": "RDNA 1.0", "Score": "15.34"},

        {"VGAname": "AMD Radeon RX 5500", "VRAM": "4 GB", "GDDR": "GDDR6", "SPC": "1x 8-pin", "PowerRequirment": "110 W", "ShaderCore": "1408", "Core speed": "1845 MHz",
         "Memory Bus": "128 bit", "Series": "RX-5000", "Architecture": "RDNA 1.0", "Score": "15.29"},

        {"VGAname": "AMD Radeon RX 590", "VRAM": "8 GB", "GDDR": "GDDR5", "SPC": "1x 8-pin", "PowerRequirment": "175 W", "ShaderCore": "2304", "Core speed": "1545 MHz",
         "Memory Bus": "256 bit", "Series": "RX-500", "Architecture": "GCN 4.0", "Score": "16.73"},

        {"VGAname": "AMD Radeon RX 580X", "VRAM": "8 GB", "GDDR": "GDDR5", "SPC": "1x 8-pin", "PowerRequirment": "185 W", "ShaderCore": "2304", "Core speed": "1340 MHz",
         "Memory Bus": "256 bit", "Series": "RX-500", "Architecture": "GCN 4.0", "Score": "15.13"},

        {"VGAname": "AMD Radeon RX 570X", "VRAM": "8 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "120 W", "ShaderCore": "2048", "Core speed": "1244 MHz",
         "Memory Bus": "256 bit", "Series": "RX-500", "Architecture": "GCN 4.0", "Score": "12.98"},

        {"VGAname": "AMD Radeon RX 560X", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "75 W", "ShaderCore": "1024", "Core speed": "1275 MHz",
         "Memory Bus": "128 bit", "Series": "RX-500", "Architecture": "GCN 4.0", "Score": "6.48"},

        {"VGAname": "AMD Radeon RX 550X", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "50 W", "ShaderCore": "512", "Core speed": "1183 MHz",
         "Memory Bus": "128 bit", "Series": "RX-500", "Architecture": "GCN 4.0", "Score": "3.70"},

        {"VGAname": "AMD Radeon R9 390X", "VRAM": "8 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "275 W", "ShaderCore": "2816", "Core speed": "1050 MHz",
         "Memory Bus": "512 bit", "Series": "AMD R9-300", "Architecture": "GCN 2.0", "Score": "14.20"},

        {"VGAname": "AMD Radeon R9 390", "VRAM": "8 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "275 W", "ShaderCore": "2560", "Core speed": "1000 MHz",
         "Memory Bus": "512 bit", "Series": "AMD R9-300", "Architecture": "GCN 2.0", "Score": "12.83"},

        {"VGAname": "AMD Radeon R9 380X", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "190 W", "ShaderCore": "2048", "Core speed": "970 MHz",
         "Memory Bus": "256 bit", "Series": "AMD R9-300", "Architecture": "GCN 3.0", "Score": "10.70"},

        {"VGAname": "AMD Radeon R9 380", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "190 W", "ShaderCore": "1792", "Core speed": "970 MHz",
         "Memory Bus": "256 bit", "Series": "AMD R9-300", "Architecture": "GCN 3.0", "Score": "9.37"},

        {"VGAname": "AMD Radeon R9 290X", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "290 W", "ShaderCore": "2816", "Core speed": "1000 MHz",
         "Memory Bus": "512 bit", "Series": "AMD R9-200", "Architecture": "GCN 2.0", "Score": "13.54"},

        {"VGAname": "AMD Radeon R9 290", "VRAM": "4 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "275 W", "ShaderCore": "2560", "Core speed": "947 MHz",
         "Memory Bus": "512 bit", "Series": "AMD R9-200", "Architecture": "GCN 2.0", "Score": "12.08"},

        {"VGAname": "AMD Radeon R9 280X", "VRAM": "3 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "250 W", "ShaderCore": "2048", "Core speed": "1000 MHz",
         "Memory Bus": "384 bit", "Series": "AMD R9-200", "Architecture": "GCN 1.0", "Score": "10.23"},

        {"VGAname": "AMD Radeon R9 280", "VRAM": "3 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "200 W", "ShaderCore": "1792", "Core speed": "933 MHz",
         "Memory Bus": "384 bit", "Series": "AMD R9-200", "Architecture": "GCN 1.0", "Score": "8.48"},

        {"VGAname": "AMD Radeon R9 270X", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "180 W", "ShaderCore": "1280", "Core speed": "1050 MHz",
         "Memory Bus": "256 bit", "Series": "AMD R9-200", "Architecture": "GCN 1.0", "Score": "7.19"},

        {"VGAname": "AMD Radeon R9 270", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "150 W", "ShaderCore": "1280", "Core speed": "925 MHz",
         "Memory Bus": "256 bit", "Series": "AMD R9-200", "Architecture": "GCN 1.0", "Score": "6.30"},

        {"VGAname": "AMD Radeon R7 370", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "110 W", "ShaderCore": "1024", "Core speed": "975 MHz",
         "Memory Bus": "256 bit", "Series": "AMD R7-300", "Architecture": "GCN 1.0", "Score": "5.65"},

        {"VGAname": "AMD Radeon R7 360", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "100 W", "ShaderCore": "768", "Core speed": "1050 MHz",
         "Memory Bus": "128 bit", "Series": "AMD R7-300", "Architecture": "GCN 2.0", "Score": "4.83"},

        {"VGAname": "AMD Radeon R7 265", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "150 W", "ShaderCore": "1024", "Core speed": "925 MHz",
         "Memory Bus": "256 bit", "Series": "AMD R7-200", "Architecture": "GCN 1.0", "Score": "5.18"},

        {"VGAname": "AMD Radeon R7 260X", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "115 W", "ShaderCore": "896", "Core speed": "1100 MHz",
         "Memory Bus": "128 bit", "Series": "AMD R7-200", "Architecture": "GCN 2.0", "Score": "5.44"},

        {"VGAname": "AMD Radeon R7 250X", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "80 W", "ShaderCore": "640", "Core speed": "950 MHz",
         "Memory Bus": "128 bit", "Series": "AMD R7-200", "Architecture": "GCN 1.0", "Score": "3.40"},

        {"VGAname": "AMD Radeon R7 250", "VRAM": "1024 MB", "GDDR": "DDR3", "SPC": "None", "PowerRequirment": "55 W", "ShaderCore": "512", "Core speed": "925 MHz",
         "Memory Bus": "128 bit", "Series": "AMD R7-200", "Architecture": "GCN 1.0", "Score": "2.30"},

        {"VGAname": "AMD Radeon R7 240", "VRAM": "2 GB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "30 W", "ShaderCore": "320", "Core speed": "700 MHz",
         "Memory Bus": "128 bit", "Series": "AMD R7-200", "Architecture": "GCN 1.0", "Score": "1.50"},

        {"VGAname": "ATI Radeon HD 5970", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin + 1x 8-pin", "PowerRequirment": "294 W", "ShaderCore": "1600",
         "Core speed": "725 MHz", "Memory Bus": "256 bit", "Series": "ATI HD-5000", "Architecture": "TeraScale 2", "Score": "3.66"},

        {"VGAname": "ATI Radeon HD 5870", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "188 W", "ShaderCore": "1600", "Core speed": "850 MHz",
         "Memory Bus": "256 bit", "Series": "ATI HD-5000", "Architecture": "TeraScale 2", "Score": "4.28"},

        {"VGAname": "ATI Radeon HD 5850", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "151 W", "ShaderCore": "1440", "Core speed": "725 MHz",
         "Memory Bus": "256 bit", "Series": "ATI HD-5000", "Architecture": "TeraScale 2", "Score": "3.36"},

        {"VGAname": "ATI Radeon HD 5770", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "108 W", "ShaderCore": "800", "Core speed": "850 MHz",
         "Memory Bus": "128 bit", "Series": "ATI HD-5000", "Architecture": "TeraScale 2", "Score": "2.46"},

        {"VGAname": "ATI Radeon HD 5750", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "86 W", "ShaderCore": "720", "Core speed": "700 MHz",
         "Memory Bus": "128 bit", "Series": "ATI HD-5000", "Architecture": "TeraScale 2", "Score": "1.90"},

        {"VGAname": "ATI Radeon HD 5670", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "None", "PowerRequirment": "64 W", "ShaderCore": "400", "Core speed": "775 MHz",
         "Memory Bus": "128 bit", "Series": "ATI HD-5000", "Architecture": "TeraScale 2", "Score": "1.26"},

        {"VGAname": "ATI Radeon HD 5570", "VRAM": "1024 MB", "GDDR": "GDDR3", "SPC": "None", "PowerRequirment": "39 W", "ShaderCore": "400", "Core speed": "650 MHz",
         "Memory Bus": "128 bit", "Series": "ATI HD-5000", "Architecture": "TeraScale 2", "Score": "1.0"},

        {"VGAname": "ATI Radeon HD 4890", "VRAM": "1024 MB", "GDDR": "GDDR5", "SPC": "2x 6-pin", "PowerRequirment": "190 W", "ShaderCore": "800", "Core speed": "850 MHz",
         "Memory Bus": "256 bit", "Series": "ATI HD-4000", "Architecture": "TeraScale", "Score": "2.35"},

        {"VGAname": "ATI Radeon HD 4850", "VRAM": "512 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "110 W", "ShaderCore": "640", "Core speed": "575 MHz",
         "Memory Bus": "256 bit", "Series": "ATI HD-4000", "Architecture": "TeraScale", "Score": "1.74"},

        {"VGAname": "ATI Radeon HD 4770", "VRAM": "512 MB", "GDDR": "GDDR5", "SPC": "1x 6-pin", "PowerRequirment": "80 W", "ShaderCore": "640", "Core speed": "750 MHz",
         "Memory Bus": "128 bit", "Series": "ATI HD-4000", "Architecture": "TeraScale", "Score": "1.76"},

    ]
    db.VGA.insert_many(data)
    print("Finish add")


def addHistory(pcname,selectedcpu, selectedgpu, selectedpsu, selectedhdd1, selectedhdd2, selectedmb, selectedsink, selectedram, total):
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    data = [{"PCname": pcname, "CPU": selectedcpu, "VGA": selectedgpu, "RAM": selectedram, "MB": selectedmb, "PSU": selectedpsu,
             "Sink": selectedsink, "HDD1": selectedhdd1, "HDD2": selectedhdd2, "score": total},
            ]
    db.History.insert_many(data)
    print("Finish add")


def delHistory(row):
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    todel = {"PCname": row}
    test = db.History.remove(todel)
    print("finish delete {}".format(test))


def reset():
    client = pymongo.MongoClient("mongodb+srv://loma:1234@cluster0-7x0zm.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('PCbuild')
    test = db.CPU.remove()
    test = db.VGA.remove()
    test = db.HDD.remove()
    test = db.SinkCPU.remove()
    test = db.PSU.remove()
    test = db.RAM.remove()
    test = db.Mainboard.remove()
    print("finish delete")


if __name__ == '__main__':
    #reset()
    addCpu()
    addHdd()
    addMB()
    addPSU()
    addRAM()
    addSink()
    addVGA()
