import random, sys

def Calc():
    try:
        while True:
            ip = input("\nEnter an IP address: ")
            octet = ip.split(".")

            if (len(octet)==4) and (1<= int(octet[0]) <= 223) and (int(octet[0]) != 127) and (int(octet[0]) != 169 or int(octet[1]) != 254) and (0 <= int(octet[1]) <= 255 and 0<= int(octet[2]) <=255 and 0<= int(octet[3]) <=255):
                break

            else:
                print(f"\n* Invalid IP address: {ip} ")
                continue
        subnets= [255,254,248,252,240,192,224,128,0]

        while True:
            subMask = input("\nEnter a subnet mask: ")

            octet2 = subMask.split(".")

            if (len(octet2) == 4) and (int(octet2[0]) == 255) and (int(octet2[1]) in subnets) and (int(octet2[2]) in subnets) and (int(octet2[3]) in subnets) and (int(octet2[0]) >= int(octet2[1]) >= int(octet2[2]) >= int(octet2[3])):
                break
    
            else:
                print(f"\n*Invalid subnet mask: {subMask} ")
                continue
        octet3 = []
        for oc in octet2:
            binary = bin(int(oc)).lstrip("0b")
            octet3.append(binary.zfill(8))

        binaryM = "".join(octet3)
        zeroCount = binaryM.count("0")
        onesCount= 32 - zeroCount
        hosts = abs(2**zeroCount-2)
        print("----------------------------------------------------------")
        print(f"\n\nMaximum Number of hosts: {hosts}")
        octet4= []
        for oc in octet2:
            wild = 255 - int(oc)
            octet4.append(str(wild))
        wildM = ".".join(octet4)
        print(f"\nWildcard Address: {wildM}")

        octet5 = []

        for oc in octet:
            binary = bin(int(oc)).lstrip("0b")
            octet5.append(binary.zfill(8))

        ipB = "".join(octet5)
        netB = ipB[:(onesCount)] +"0"*zeroCount
        broadB= ipB[:(onesCount)]+"1"*zeroCount

        octet6 = []
        for b in range(0,32,8):
            ipO= netB[b: b+8]
            octet6.append(ipO)

        add = []

        for oc in octet6:
            add.append(str(int(oc, 2)))

        netAdd = ".".join(add)

        octet7 = []
        for i in range(0,32,8):
            broadOc = broadB[i: i+8]
            octet7.append(broadOc)

        bCastAd = []

        for c in octet7:
            bCastAd.append(str(int(c, 2)))
    

        broadAdd = ".".join(bCastAd)

        print(f"\nNetwork Address: {netAdd}")
        print(f"\nBroadcast Address: {broadAdd}")
        print(f"\nThe MAsk Bits: {onesCount}")

        while True:
            gen = input("Random IP from this Subnet?(y/n) ")
            if gen =="y":
                gen_ip =[]

                for ind, octe in enumerate(bCastAd):
                    for inde , oc in enumerate(add):
                        if ind == inde:
                            if octe == oc:
                                gen_ip.append(oc)
                            else:
                                gen_ip.append(str(random.randint(int(oc),int(octe))))
                y = ".".join(gen_ip)

                print(f"Random IP IS: {y}")
            else:
                break

    except KeyboardInterrupt:
        print("\n\nExiting...\n")
        sys.exit()

Calc()