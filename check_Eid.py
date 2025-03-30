import datetime
from hijri_converter import convert



EIDS = {
    "Eid_Fitr": {"month": 10, "day": 1},  # 1st of Shawwal
    "Eid_Adha": {"month": 12, "day": 10}, # 10th of Dhu al-Hijjah
    "Eid_al_Mawlid": {"month": 3, "day": 12}, # 12th of Rabi' al-Awwal
    "Eid_al_Ghadeer": {"month": 12, "day": 18}, # 18th of Dhu al-Hijjah
    "Eid_al_Tarwiyah": {"month": 12, "day": 8}  # 8th of Dhu al-Hijjah
}


def check_Eid():
    current_date = datetime.datetime.now()
    hijri_date = convert.Gregorian.fromdate(current_date)

    for Eid, info in EIDS.items():
        if info["month"] == hijri_date.month and info["day"] == hijri_date.day:
            return f"Today is {Eid}"
        
    return "Today is not Eid"




if __name__ == "__main__":
    print(check_Eid())