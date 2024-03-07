def time_to_text(minutes):
    heures, minutes_restantes = divmod(minutes, 60)
    print(f"{heures} heures et {minutes_restantes} minutes")

time_to_text(250)  


