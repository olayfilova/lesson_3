# None, type
# val_int = 123
# print(val_int, id(val_int))

# bool
# var_1 = True
# var_2 = False
# result = 1 > 2 #  >, <, ==, !=, >=, <=
# print(result)
#
# res_1  = "hello" == "hello!" # !=
# print(res_1)

# res_1  = "hello" > "hello!" # !=
#
# print(res_1)

# res_1  = "llo" in "hello!"

# print(res_1)
# res_1  = "ol" in "hello!"
# print(res_1)

# val_int = 11
# val_str = "12"
# result = str(val_int) + val_str
# print(result)
#
# var_1 = 11
# var_2 = "12"
# print(var_1 + int(var_2))

###### if

# weather = "cold"
# if weather == "cold":
#     print("it's cold")

# weather = "not too cold"
# if weather == "cold":
#     print("it's cold")
# else:
#     print("it's not cold")

#
# val_int = 2

# if val_int > 0 and val_int < 10:
#     print(f"{val_int} is bigger that 0")
# elif val_int > 0:
#     print(f"{val_int} is bigger that 0")
#
# else:
#     print(f"{val_int} is less than 0")
#
# val_int = -2
# if 0 < val_int < 10:
#     print(f"{val_int} is less that 10")
# elif val_int > 10 and val_int < 20:
#     print(f"{val_int} is bigger that 10")
# else:
#     print(f"{val_int} is less that 100")


### input()

# val_1 = input("please type a number: ")
# print(val_1)

# val_1 = input("please type a number: ")
# val_2 = input("please type another number: ")
# result = val_1 + val_2
# print(result)

# val_1 = input("please type a number: ")
# val_2 = input("please type another number: ")
# result = int(val_1) + int(val_2)
# print(result)

# try:
# val_1 = int(input("please type a number: "))
# except ValueError: #### ERROR TYPE!!!!
#  print("only digits: 1,2,3...")
# val_2 = int(input("please type another number: "))
# result = val_1 + val_2
# print(result)

# result = 0
# try:
#       val_1 = int(input("please type a number: "))
#       result = 1 / val_1 ### currency reverse!!
# except ValueError: #### ERROR TYPE!!!!
#  print("only digits: 1,2,3...")
# except ZeroDivisionError:
#  print(" can't divide on 0")
# except (EnvironmentError, ConnectionError):
#     print("system is busy now")
# print(result)
# value_int = 123
# print(value_int, id(value_int))
# val_id = id(value_int)
# print(val_id)


# def longest_word(sentence: "The day were anyway spend in the city not in the forest") -> str:

# sentence = "The day were anyway spend in the city not in the forest"
# word = sentence.split(" ")
# i = sorted(word, key=len)
# l = []
# max_len = -1
# for w in i:
#     if len(w) > max_len:
#         w = +1
#         max_len = len(w)
#         l.append(w)
#         res = w
#
#     print(w)


# def longest_word(sentence: str) -> str:
#         punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#         sentence_without_punctuation = ''.join(char for char in sentence if char not in punctuation_chars)
#         words = sentence_without_punctuation.split()
#
#         if not words:
#             return ""
#
#         max_len = max(len(word) for word in words)
#         longest_words = [word for word in words if len(word) == max_len]
#
#         return longest_words[0]
#
#
# print(longest_word("The day were anyway spend in the city not in the forest"))

# var = "The day were anyway spend in the city not in the forest"
# var_1 = len(var.split(" "))
# max_len = -1
# for i in str(var_1):
#     if len(i) > max_len:
#         max_len = len(i)
#
#     res = max_len(str(i))
# print(res)


# Catch an idea 💡! Declare variables to keep a current longest word and its length. Split the sentence into separate words, look at every one, find its length and compare with the stored one. If the length of current word is longer - update values of variables for a current longest word and its length.
# def longest_word(sentence: str) -> str:
#     var =len(sentence.split(" "))
#     for i in var:
#         res =max(str(i))
#
#
#     return res
#
# print(longest_word("The day were anyway spend in the city not in the forest"))


# print("Example:")
# print(longest_word("hello world"))


# temp =sentence.split(" ")
# lst =[]
# print(temp)
# max_len = -1
#
# while i in temp >max_len():
#     i += 1
#     lst.append(i)
#     print(lst)


#
# import string
#
# def longest_word(sentence: str) -> str:
#     # Remove punctuation marks from the sentence
#     translator = str.maketrans("", "", string.punctuation)
#     sentence_without_punctuation = sentence.translate(translator)
#
#     # Split the sentence into words
#     words = sentence_without_punctuation.split()
#
#     # Find the word with the maximum length
#     if not words:
#         return ""  # Return an empty string if the sentence is empty
#
#     longest = max(words, key=len)
#     return longest
#
# # Example usage:
# input_sentence = "This is a sample sentence, without dunctuation punctuation marks!"
# result = longest_word(input_sentence)
# print(f"The longest word is: {result}")


#
# def replace_all(mainText: str, target: str, repl: str) -> str:
#     for i in mainText:
#         return main_Text.replace()
#     target = str(mainText.split(" ", 1).append(repl))
#     return target
#
#
# print("Example:")
# print(replace_all("hello world", "world", "TypeScript"))
#
#
# print(convert_date("01/01/2023"))


#
# # These "asserts" are used for self-checking
# assert convert_date("25/12/2021") == "2021-12-25"
# assert convert_date("01/01/2000") == "2000-01-01"
# assert convert_date("15/06/1995") == "1995-06-15"
# assert convert_date("29/02/2020") == "2020-02-29"
# assert convert_date("10/10/2010") == "2010-10-10"
# assert convert_date("31/05/1985") == "1985-05-31"
# assert convert_date("07/08/1960") == "1960-08-07"
# assert convert_date("02/09/1999") == "1999-09-02"
# assert convert_date("30/04/1975") == "1975-04-30"
# assert convert_date("29/02/2019") == "Error: Invalid date."
# assert convert_date("30/04/1975/1") == "Error: Invalid date."
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# import re
#
#
# def first_word(text: str) -> str:
#     match = re.search(r"[a-zA-Z']+", text)
#
#     if match:
#         return match.group()
#     else:
#         return ""
#
#
# def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
#     # Check if the length difference exceeds the threshold
#     if abs(len(str1) - len(str2)) > threshold:
#         return False
#
#     # Count the number of differing characters
#     diff_count = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)
#
#     # Check if the number of differences is within the threshold
#     return diff_count <= threshold
#
# # Example usage
# print("Example:")
# print(first_word("Hello world"))
#
# # These "asserts" are used for self-checking
# assert first_word("Hello world") == "Hello"
# assert first_word(" a word ") == "a"
# assert first_word("don't touch it") == "don't"
# assert first_word("greetings, friends") == "greetings"
# assert first_word("... and so on ...") == "and"
# assert first_word("hi") == "hi"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
#
#
# # Example usage
# print("Example:")
# print(fuzzy_string_match("apple", "appel", 2))
#
# # These "asserts" are used for self-checking
# assert fuzzy_string_match("apple", "appel", 2) == True
# assert fuzzy_string_match("apple", "bpple", 1) == True
# assert fuzzy_string_match("apple", "bpple", 0) == False
# assert fuzzy_string_match("apple", "apples", 1) == True
# assert fuzzy_string_match("apple", "bpples", 2) == True
# assert fuzzy_string_match("apple", "apxle", 1) == True
# assert fuzzy_string_match("apple", "pxxli", 3) == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


from itertools import permutations

# def string_permutations(s):
#     # Use itertools permutations to generate all permutations
#     perm_tuples = permutations(s)
#
#     # Convert tuples to strings
#     permutations_list = [''.join(perm) for perm in perm_tuples]
#
#     # Sort the permutations alphabetically
#     sorted_permutations = sorted(permutations_list)
#
#     return sorted_permutations
#
#
# # Example usage and assertions
# assert list(string_permutations("ab")) == ["ab", "ba"]
# assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
# assert list(string_permutations("a")) == ["a"]
# assert list(string_permutations("abcd")) == [
#     "abcd", "abdc", "acbd", "acdb", "adbc", "adcb",
#     "bacd", "badc", "bcad", "bcda", "bdac", "bdca",
#     "cabd", "cadb", "cbad", "cbda", "cdab", "cdba",
#     "dabc", "dacb", "dbac", "dbca", "dcab", "dcba"
# ]

#
# def determine_sign(num: int) -> str:
#    if num > 0:
#         return "positive"
#    elif num < 0:
#         return "negative"
#    else:
#         return "zero"
#
# # Example usage:
# print(determine_sign(5))    # Output: positive
# print(determine_sign(-3))   # Output: negative
# print(determine_sign(0))    # Output: zero

#
# def find_remainder(dividend: int, divisor: int) -> int:
#     return dividend % divisor
#
# # Example usage:
# print(find_remainder(3, 2))  # Output: 1
#
# # These "asserts" are used for self-checking
# assert find_remainder(10, 3) == 1
# assert find_remainder(14, 4) == 2
# assert find_remainder(27, 4) == 3
# assert find_remainder(10, 5) == 0
# assert find_remainder(10, 1) == 0
# assert find_remainder(5, 7) == 5
# assert find_remainder(7, 5) == 2
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

#
# def sum_upto_n(N: int) -> int:
#     return sum(range(1, N + 1))
#
# # Example usage:
# print(sum_upto_n(11))  # Output: 66
#
# # These "asserts" are used for self-checking
# assert sum_upto_n(1) == 1
# assert sum_upto_n(2) == 3
# assert sum_upto_n(3) == 6
# assert sum_upto_n(4) == 10
# assert sum_upto_n(5) == 15
# assert sum_upto_n(10) == 55
# assert sum_upto_n(20) == 210
# assert sum_upto_n(100) == 5050
# assert sum_upto_n(200) == 20100
# assert sum_upto_n(500) == 125250
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def goes_after(word: str, first: str, second: str) -> bool:
#     if len(word) < 2 or first not in word or second not in word:
#         return False
#     index_first = word.find(first)
#     index_second = word.find(second)
#     return index_second == index_first + 1
#
#
# print("Example:")
# print(goes_after("world", "w", "o"))
#
# # These "asserts" are used for self-checking
# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("panorama", "a", "n") == True
# assert goes_after("list", "l", "o") == False
# assert goes_after("", "l", "o") == False
# assert goes_after("list", "l", "l") == False
# assert goes_after("world", "d", "w") == False
# assert goes_after("Almaz", "a", "l") == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

#
# def is_armstrong(num: int) -> bool:
#     # Convert the number to a string to find its length
#     num_str = str(num)
#     num_digits = len(num_str)
#
#     # Calculate the sum of each digit raised to the power of the number of digits
#     armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
#
#     # Compare the sum with the original number
#     return armstrong_sum == num
#
# # Example usage:
# print(is_armstrong(11))
#
# # These "asserts" are used for self-checking
# assert is_armstrong(153) == True
# assert is_armstrong(370) == True
# assert is_armstrong(947) == False
# assert is_armstrong(371) == True
# assert is_armstrong(407) == True
# assert is_armstrong(163) == False
# assert is_armstrong(100) == False
# assert is_armstrong(8208) == True
# assert is_armstrong(930) == False
# assert is_armstrong(4) == True
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

#
# def max_of_three(a: int, b: int, c: int) -> int:
#     return max(a, b, c)
#
# # Example usage:
# print(max_of_three(1, 2, 3))
#
# # These "asserts" are used for self-checking
# assert max_of_three(1, 2, 3) == 3
# assert max_of_three(3, 2, 1) == 3
# assert max_of_three(1, 3, 2) == 3
# assert max_of_three(0, 0, 0) == 0
# assert max_of_three(-1, -2, -3) == -1
# assert max_of_three(5, 5, 4) == 5
# assert max_of_three(-5, -5, -6) == -5
# assert max_of_three(10, 9, 10) == 10
# assert max_of_three(123, 456, 789) == 789
# assert max_of_three(789, 123, 456) == 789
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


# def translate(text: str) -> str:
#     vowels = "aeiouy"
#     result = []
#     i = 0
#
#     while i < len(text):
#         result.append(text[i])
#         if text[i].lower() in vowels:
#             while i + 1 < len(text) and text[i + 1].lower() in vowels:
#                 i += 1  # Skip additional consecutive vowels
#         i += 1  # Move to the next character
#
#     return ''.join(result)
#
# # Example usage:
# print(translate("hieeelalaooo"))
#
# # These "asserts" are used for self-checking
# assert translate("hieeelalaooo") == "hello"
# assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# assert translate("aaa bo cy da eee fe") == "a b c d e f"
# assert translate("sooooso aaaaaaaaa") == "sos aaa"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
#
# from typing import Iterable, Union
# from math import sqrt
#
#
# def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int, str]]:
#     discriminant = b ** 2 - 4 * a * c
#
#     if discriminant > 0:
#         x1 = (-b + sqrt(discriminant)) / (2 * a)
#         x2 = (-b - sqrt(discriminant)) / (2 * a)
#         return sorted([x1, x2], reverse=True)
#     elif discriminant == 0:
#         x = -b / (2 * a)
#         return [x, x]
#     else:
#         return ["No real roots"]
#
#
# # Example usage:
# print(list(quadratic_roots(1, 2, 3)))
#
# # These "asserts" are used for self-checking
# assert list(quadratic_roots(1, -3, 2)) == [2, 1]
# assert list(quadratic_roots(1, 0, -1)) == [1, -1]
# assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
# assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]
# assert list(quadratic_roots(1, 4, 4)) == [-2, -2]
# assert list(quadratic_roots(1, -5, 6)) == [3, 2]
# assert list(quadratic_roots(1, -6, 9)) == [3, 3]
# assert list(quadratic_roots(2, 2, 1)) == ["No real roots"]
# assert list(quadratic_roots(2, -7, 6)) == [2, 1.5]
# assert list(quadratic_roots(2, -3, 1)) == [1, 0.5]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
#
#
# def from_camel_case(name: str) -> str:
#     result = [name[0].lower()]
#
#     for char in name[1:]:
#         if char.isupper():
#             result.extend(['_', char.lower()])
#         else:
#             result.append(char)
#
#     return ''.join(result)
#
# # Example usage:
# print(from_camel_case("MyFunctionName"))
#
# # These "asserts" are used for self-checking
# assert from_camel_case("MyFunctionName") == "my_function_name"
# assert from_camel_case("IPhone") == "i_phone"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


import random
import json
from datetime import datetime
import argparse


class Trader:
    def __init__(self, config_path, history_path):
        with open(config_path) as f:
            config = json.load(f)
        self.delta = config["delta"]
        self.rate = config["rate"]
        self.uah_balance = config["uah_balance"]
        self.usd_balance = config["usd_balance"]
        self.history_path = history_path
        self.history = []

        try:
            with open(history_path, "r") as history_file:
                history_data = json.load(history_file)
                self.uah_balance = history_data["uah_balance"]
                self.usd_balance = history_data["usd_balance"]
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_to_history(self, action, currency_amount, uah_amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {"timestamp": timestamp, "action": action, "currency_amount": currency_amount,
                       "uah_amount": uah_amount}
        self.history.append(transaction)

        with open(self.history_path, "a") as history_file:
            json.dump(transaction, history_file, indent=4)

    def get_rate(self):
        return round(self.rate, 2)

    def get_available_balance(self):
        return {"USD": round(self.usd_balance, 2), "UAH": round(self.uah_balance, 2)}

    def buy(self, amount):
        if self.uah_balance < amount * self.rate:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {amount * self.rate:.2f}, AVAILABLE {self.uah_balance:.2f}")
            return
        self.uah_balance -= amount * self.rate
        self.usd_balance += amount
        self.save_to_history("BUY", amount, amount * self.rate)

    def sell(self, amount):
        if self.usd_balance < amount:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {self.usd_balance:.2f}")
            return
        self.usd_balance -= amount
        self.uah_balance += amount / self.rate
        self.save_to_history("SELL", amount, amount / self.rate)

    def buy_all(self):
        if self.uah_balance == 0:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {self.uah_balance:.2f}, AVAILABLE 0.00")
            return
        amount = self.uah_balance / self.rate
        self.save_to_history("BUY", amount, amount * self.rate)

    def sell_all(self):
        amount = self.usd_balance
        if amount == 0:
            print("No USD to sell.")
            return
        self.usd_balance = 0
        uah_amount = amount * self.rate
        self.uah_balance += uah_amount
        self.save_to_history("SELL", amount)
        return uah_amount

    def next_rate(self):
        self.rate += random.uniform(-self.delta, self.delta)
        self.rate = round(self.rate, 2)

    def restart(self):
        self.rate = 36.00
        self.uah_balance = 10000.00
        self.usd_balance = 0.00
        self.history = []

    def main():
        parser = argparse.ArgumentParser(description="Currency Trader")
        parser.add_argument("--config", type=str, default="config.json", help="Path to configuration file")
        parser.add_argument("--history", type=str, default="history.json", help="Path to transaction history file")
        parser.add_argument("command", type=str, help="Command to execute", nargs="?")
        parser.add_argument("command_2", type=float, nargs="?", help="Second command")

        args = parser.parse_args()

        trader = Trader(args.config, args.history)

        if args.command == "RATE":
            print(trader.get_rate())
        elif args.command == "AVAILABLE":
            print(trader.get_available_balance())
        elif args.command == "NEXT":
            trader.next_rate()
            print(trader.get_rate())
        elif args.command == "BUY":
            if args.command_2 is not None:
                trader.buy(args.command_2)
                print(trader.get_available_balance())
            else:
                print("Invalid amount format")
        elif args.command == "BUY_ALL":
            trader.buy_all()
            print(trader.get_available_balance())
        elif args.command == "SELL_ALL":
            uah_amount = trader.sell_all()
            if uah_amount is not None:
                print(trader.get_available_balance())
        elif args.command == "RESTART":
            trader.restart()
            with open(args.history, "w") as history_file:
                history_file.write("")
        else:
            print("Unknown command")

    if __name__ == "__main__":
        main()
