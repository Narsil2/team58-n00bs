def calculation(cityavg, householdmembers, fuel, efficiency, distance, kWH, usagefactor, totalqty):
    creditsavlbl = (cityavg * householdmembers)/12
    creditsused = 0
    if fuel == "petrol":                       
        creditsused += (efficiency/distance)* 2.296
    elif fuel == "diesel":
        creditsused += (efficiency/distance)* 2.653
    creditsused += kWH * 0.704
    creditsused += usagefactor * totalqty * 2.983
    creditsavlbl -= creditsused
    netcreditsused = creditsused/householdmembers
    print(round(netcreditsused, 2), round(creditsavlbl, 2))    
calculation(2000, 3,'petrol',7,14,200,0.5, 14.2)

    
