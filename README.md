# Wisplus_Projects-
I INCLUDED ALL MY PYTHON CODES AND PROJECTS 



1. Roman Numeral Converter 🔢➡️ⅠⅡⅢ

A Python script that converts integer numbers (1-3999) into Roman numerals using a dictionary-based approach.
meaning that you can enter any integer and the scrupt changes it to an equivalent eligible  roman nunber 
NOTE: tge max roman numbe is 3999 so basically i used that approach 

🎯 Features

· Converts numbers from 1 to 3999 (standard Roman numeral range)
· Zero-free number handling: Currently optimized for numbers without zero digits
· Simple dictionary-based logic
· Clean, modular code structure

📋 How It Works
it is based on my idea that on converting an integer to a roman number it , we change each digit in a tge given number to its equivalent roman eg 345 , means cinvert  5, convert 4 and convert 3 individually and combine the results ..boom it's basically that 

The converter uses four dictionaries to map place values:

· dictA: Units (1-9) → i to ix  →the ones 
· dictB: Tens (10-90) → x to xc → the tenth place 
· dictC: Hundreds (100-900) → c to cm  →the hundredths olace 
· dictD: Thousands (1000-3000) → m to mmm → thousandths place 

USAGE:
. Run the script on your python environment, you will be prompted to enter any number from 1-3999 
. once input is given , the code displays the right output

⚠️ Current Limitation

· Zero digits not supported: Numbers containing '0' in any position (e.g., 10, 101, 2020) are not yet handled

📝 Examples

```
Input: 49     Output: XLIX
Input: 399    Output: CCCXCIX
Input: 1984   Output: MCMLXXXIV
Input: 777    Output: DCCLXXVII
```

🛠️ Future Improvements

· Add support for numbers with zero digits
· Input validation and error handling
· Reverse conversion (Roman to integer)

---

Made with  by [Gerson] - A simple yet effective Roman numeral converter for learning and reference!

"Thriving to Excel " 
