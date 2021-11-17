def converter_Grey_rad(rad):
    if rad[1] == "Гр":
        observ = int(rad[0])*100
        return observ


rad = input().split()
print(converter_Grey_rad(rad), "рад")
