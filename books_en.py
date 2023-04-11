import random
from colorama import init, Fore, Back, Style

# Initialize colors
init()
total_books = 66

oldTestament = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
                "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
                "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
                "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
                "Ecclesiastes", "Song of Songs", "Isaiah", "Jeremiah",
                "Lamentations", "Ezekiel", "Daniel", "Hosea",
                "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
                "Zephaniah", "Haggai", "Zechariah", "Malachi"]

newTestament = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
                "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians",
                "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
                "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"]

choose = input("New or Old?: ")


if choose == 'New':
    print("The book you will read is: " +
          Fore.RED + random.choice(newTestament))
elif choose == 'Old':
    print("The book you will read is: " +
          Fore.CYAN + random.choice(oldTestament))
else:
    print("Exit...")
