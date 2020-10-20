from wordlist import get_words
import random


def main():
    # Hakee tiedoston ja tallentaa sen words muuttujaan
    words = get_words()
    # Ottaa words listasta satunnaisen sanan
    rand_word = random.choice(words)
    # Pytää käyttäjää antamaan arvauksen
    user_quess = input('Arvaa sana: ').strip()

    # Tarkistaa oliko oikein vai väärin, jos väärin kertoo mikä sana oli
    if user_quess == rand_word:
        print('Oikein')
    else:
        print('Väärin :( Sana oli: ' + rand_word)


if __name__ == "__main__":
    main()
