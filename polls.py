import re

with open("greenlight polls template.md", "r") as f:
    template = f.read()
    
TO_BE_REPLACED = {
    0: "\$asset_code",
    1: "\$asset_name",
    2: "\$discussion_link",
    3: "\$date_MONTH_DD,_YYYY", #make common constants the last keys
    4: "\$date_DAY,_MONTH_DD"}  #make common constants the last keys

LIST = [
    ["CurveLP-renBTC-WBTC",
     "renbtcCrv LP Token",
     "https://forum.makerdao.com/t/curvelp-renbtc-wbtc-mip6-collateral-onboarding-application/6680"],
    ["SB-BFDC",
     "BeachFront Digital Coin",
     "https://forum.makerdao.com/t/sb-bfdc-mip6-application-own-and-trade-a-piece-of-paradise-with-this-beachfront-hotel-in-phuket-thailand-managed-by-best-western-plus-a-solidblock-offering/6778"],
    ["SNX",
     "Synthetix",
     "https://forum.makerdao.com/t/snx-mip6-collateral-onboarding-application/6497"],
    ["SolarX",
     "Uprets/SolarX",
     "https://forum.makerdao.com/t/solarx-mip6-application-uprets-solarx-industrial-real-estate-backed-loans/6718"],
    ["sUSD",
     "Synthetix USD",
     "https://forum.makerdao.com/t/susd-mip6-collateral-onboarding-application/6555"],
    ["xSUSHI",
     "Sushibar Token",
     "https://forum.makerdao.com/t/xsushi-mip6-collateral-onboarding-application/6541"],
    ["aWETH",
     "AAVE Wrapped Ether",
     "https://forum.makerdao.com/t/aweth-mip6-collateral-onboarding-application-for-aeth/6589"],
    ["aAAVE",
     "aAAVE",
     "https://forum.makerdao.com/t/aaave-mip6-collateral-onboarding-application-for-aaave/6588"],
    ["CurveLP-cDAI-cUSDC",
     "Compound Curve LP Token",
     "https://forum.makerdao.com/t/curvelp-cdai-cusdc-mip6-collateral-onboarding-application/6682"]
    ]

# Common constants
dateMDY = "March 15, 2021"
dateDMD = "Monday, March 15"
LIST = [e + [dateMDY,dateDMD] for e in LIST]

for i in range(0,len(LIST)):
    t = template
    for b in range (0,len(TO_BE_REPLACED)):
        t = re.sub(TO_BE_REPLACED[b],LIST[i][b],t)
    with open(LIST[i][0]+".md", "w+") as f:
        f.write(t)
