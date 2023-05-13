"""
1. Stwórz funkcję która przyjmuje jeden argument który ma być stringiem, funkcja powinna policzyć których znaków w
stringu były najwięceji zwrócić znak oraz liczbę powtórzeń.
Np. dla stringa 'ala ma kota' wynikiem powinno być a, 4
"""
from collections import Counter

class String_counter:
    def __init__(self, text: str) -> None:
        self.text = text


    def function(self):
        list_of_letters =[]
        self.text = self.text.lower()
        for letter in self.text:
            list_of_letters.append(letter)
        count = Counter(letter)
        print(count)
        counts={}
        for letter in list_of_letters:
            if letter in counts:
                counts[letter] +=1
            else:
                counts[letter] = 1

        return counts
    def most_common(self):
        max_key =max(self.function(), key =self.function().get)
        return max_key


        #max_value =max(counts.values())
        #return max_value

        #most = max(self.function())
        #number = self.function().index(most)
        #return most[number]





def main():
    string_001 = String_counter(text = "Ala")
    print(string_001.function())
    print(string_001.most_common())




if __name__ == "__main__":
    main()