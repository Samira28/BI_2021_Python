def converter_Grey_rad(observ):
    if observ[1] == "Гр":
        rad = int(observ[0])*100
        return rad
    
    
observ = input().split()
print(converter_Grey_rad(observ), "рад")
