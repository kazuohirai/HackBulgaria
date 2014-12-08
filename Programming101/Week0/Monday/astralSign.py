def what_is_my_sign(day, month):
    if month == 1:
        if day <= 20:
            return "Capricorn"
        else:
            return "Aquarius"
    if month == 2:
        if day <= 19:
            return "Aquarius"
        else:
            return "Pisces"
    if month == 3:
        if day <= 20:
            return "Pisces"
        else:
            return "Aries"
    if month == 4:
        if day <= 20:
            return "Aries"
        else:
            return "Taurus"
    if month == 5:
        if day <= 21:
            return "Taurus"
        else:
            return "Gemini"
    if month == 6:
        if day <= 21:
            return "Gemini"
        else:
            return "Cancer"
    if month == 7:
        if day <= 22:
            return "Cancer"
        else:
            return "Leo"
    if month == 8:
        if day <= 22:
            return "Leo"
        else:
            return "Virgo"
    if month == 9:
        if day <= 23:
            return "Virgo"
        else:
            return "Libra"
    if month == 10:
        if day <= 23:
            return "Libra"
        else:
            return "Scorpio"
    if month == 11:
        if day <= 22:
            return "Scorpio"
        else:
            return "Saggitarius"
    if month == 12:
        if day <= 21:
            return "Saggitarius"
        else:
            return "Capricorn"

