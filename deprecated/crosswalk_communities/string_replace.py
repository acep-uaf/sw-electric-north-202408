import pandas as pd

data = [
    ["Unalaska, City of", "Unalaska"],
    ["Aurora Energy", "Aurora Energy LLC Chena"],
    ["Blue Lake", "Blue Lake Hydro"],
    ["Galena", "Galena Electric Utility"],
    ["Lake Dorothy", "Lake Dorothy Hydroelectric Project"],
    ["Eklutna Lake", "Eklutna Hydro Project"],
    ["Fire Island", "Fire Island Wind"],
    ["Eva Creek", "Eva Creek Wind"],
    ["Pillar Mountain", "Pillar Mountain Wind Project Microgrid"],
    ["Terror Lake", "Terror Lake Microgrid"],
    ["Nymans Plant", "Nymans Plant Microgrid"],
    ["Port Lions", "Port Lions Microgrid"],
    ["Sheldon Point", "Nunam Iqua"],
    ["Fort Yukon", "Gwitchyaa Zhee"],
    ["Upper Kalskag", "Kalskag"],
    ["Kodiak", "Kodiak Microgrid"]
]

df = pd.DataFrame(data, columns=['Original Name', 'Canonical Name'])
print(df)








"Unalaska, City of", "Unalaska"
"Aurora Energy", "Aurora Energy LLC Chena"
"Blue Lake", "Blue Lake Hydro"
"Galena", "Galena Electric Utility"
"Lake Dorothy", "Lake Dorothy Hydroelectric Project"
"Eklutna Lake", "Eklutna Hydro Project"
"Fire Island", "Fire Island Wind"
"Eva Creek", "Eva Creek Wind"
"Pillar Mountain", "Pillar Mountain Wind Project Microgrid"
"Terror Lake", "Terror Lake Microgrid"
"Nymans Plant", "Nymans Plant Microgrid"
"Port Lions", "Port Lions Microgrid"
"Sheldon Point", "Nunam Iqua"
"Fort Yukon", "Gwitchyaa Zhee"
"Upper Kalskag", "Kalskag"
"Kodiak", "Kodiak Microgrid"
