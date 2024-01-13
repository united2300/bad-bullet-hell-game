# Latest version. Defualt.
try:
    while True:
        print ("Gamemode Selection:")
        print ("(1) Classic")
        print ("(2) Wavebased")
        e = input("")
        if e == "1":
          import ver_12
        elif e == "2":
          import ver_12_wavebased
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    try:
        input("")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
