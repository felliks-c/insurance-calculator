def calculator(price: str, age: int, experience: int, car_type: str) -> float:
    pricecoff = 1.0
    agecoff = 1.0
    expcoff = 1.0
    typecoff = 1.0

    # Базовая стоимость
    if price == "low":
        pricecoff = 5000
    elif price == "medium":
        pricecoff = 7500
    elif price == "high":
        pricecoff = 12000
    else:
        raise ValueError("Invalid price category")
    
    # Коэффициент возраста
    if 18 <= age <= 22:
        agecoff = 1.8
    elif 22 < age <= 27:
        agecoff = 1.5
    elif 27 < age <= 35:
        agecoff = 1.0
    elif 35 < age <= 40:
        agecoff = 0.95
    elif 40 < age <= 50:
        agecoff = 0.9
    elif age > 50:
        agecoff = 1.1
    else:
        raise ValueError("Invalid age")
    
    # Коэффициент стажа
    if 0 <= experience <= 1:
        expcoff = 1.6
    elif 1 < experience <= 3:
        expcoff = 1.3
    elif 3 < experience <= 5:
        expcoff = 1.1
    elif 5 < experience <= 10:
        expcoff = 0.95
    elif experience > 10:
        expcoff = 0.85
    else:
        raise ValueError("Invalid experience")
    
    # Коэффициент типа авто
    if car_type == "citycar":
        typecoff = 1.0
    elif car_type == "sportscar":
        typecoff = 1.8
    elif car_type == "suv":
        typecoff = 1.6
    else:
        raise ValueError("Invalid car type")
    
    return pricecoff * agecoff * expcoff * typecoff
