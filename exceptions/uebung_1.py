def user_input():
    try:
        return int(input("Gib eine Zahl ein: "))
    except ValueError:
        print("Fehlerhafte Eingabe. Nur Zahlen werden akzeptiert")
        return
    
def calc_mean(input_list):
    if not input_list:
        raise IndexError("Berechnung nicht möglich, die Liste ist leer.")
    return sum(input_list) / len(input_list)

inp_list = [val for _ in range(6) if (val := user_input()) is not None]
mean_list = calc_mean(inp_list)


print(f"Der Druchschnitt deiner Liste {inp_list} beträgt: {mean_list}")