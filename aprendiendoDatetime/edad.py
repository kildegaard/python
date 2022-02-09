def calcular_edad(dia: int, mes: int, anio: int) -> list:
    import datetime
    nacim = datetime.date(year=anio, day=dia, month=mes)
    hoy = datetime.date.today()
    dif = hoy - nacim
    edad = []
    edad.append((dif / 365.2425).days)
    edad.append(int((dif.days / 365.2425 - (dif / 365.2425).days) * 12))
    return edad


def print_edad(nombre: str, edad: list):
    print(f'{nombre}: {edad[0]} años y {edad[1]} meses.')
