import random

# Požádá uživatel, aby zadal číslo, které bude počítač hádat
number = int(input('Zadej číslo které bude počítač hádat: '))

# Požádá uživatel o minimální a maximální rozsah hry
low = int(input("Zadejte minimální číslo (nejmenší možný odhad): "))
high = int(input("Zadejte maximální číslo (nejvyšší možný odhad): "))

    
    
    # Počítač hádá číslo
while True:
    # Počítač vygeneruje náhodné číslo
    guess = random.randint(low, high)
    print(f'Odhad počítače je {guess}')

    # Pokud počítač uhádné číslo, hra se ukončí
    if guess == number:
        print(f'Ha, uhádl jsem tvé číslo, je to {guess}!')
        break

    # Zeptá se uživatele zdali je odhad moc velký nebo malý
    feedback = input('(V) Číslo je moc vysoké\n(N) Číslo je moc nízké\n(V/N): ').strip().lower()

    if feedback == 'v':
        high = guess - 1
    elif feedback == 'n':
        low = guess + 1
    else:
        print('Neplatná odpověď, zadej odpověď znova!')