def main():
    tiedosto = input("Anna tiedoston nimi: ")
    try:
        with open(tiedosto, 'r') as file:
            exec(file.read())
    except FileNotFoundError:
        print("Tiedostoa ei löydy")
    except Exception as e:
        print(f"Virhe suorittaessa tiedostoa: {e}")

if __name__ == '__main__':
    main()