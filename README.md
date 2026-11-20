# ISBN-13 Check Digit Generator & Validator

A Python program I built to validate post-2007, 12-digit ISBNs (without hyphens) and calculate the final 13th check digit.

I kept the scope focused on raw, unhyphenated 12-digit numbers since the goal is verifying the structure and generating the check digit rather than dealing with hyphens or legacy pre-2007 10-digit ISBNs.

## How It Works

Every input goes through these checks in order before a check digit gets generated:

1. **Numbers only (`isdigit`):** Rejects anything with letters, spaces, hyphens, decimals, or symbols.


2. **Exact length (`lengthCheckfirst`):** Makes sure the input is strictly 12 digits long before adding the check digit.


3. **Post-2007 prefix (`first3digits`):** Checks that the number starts with `978` or `979`.


4. **Country code & body length (`CountryPrefix`):**
* Checks the country/registration group code against separate lists for `978` and `979` so invalid cross-prefix combos (like `979-0`) get caught.


* Checks that the remaining digits for the publisher and book elements add up to the right length (`4–8` digits left for `978`, `7–8` digits left for `979`) so the whole body after `978`/`979` is always 9 digits.




5. **Check digit calculation (`CheckdigitCal`):** Multiplies odd-position digits by `1` and even-position digits by `3`, works out `10 - (total % 10)` (turning `10` into `0` when the remainder is `0`), and adds it to the end.



## Files in This Repo

* **`ISBN_Program.py`** — The main script. Keeps asking for 12-digit ISBNs until you enter `0`, validates them, and saves the valid 13-digit ISBNs to `ISBNcheckdigit.txt`.


* **`ISBNcheckdigit.txt`** — Output file where valid generated ISBN-13s get saved.


* **`ISBN_test.py`** — Test script that reads inputs line by line from `ISBNnum.txt` and prints out either the error or the final 13-digit ISBN.


* **`ISBNnum.txt`** — Test data file with 24 test cases ordered to match the validation steps.


* **`ISBN_Validation_Test_Cases.docx`** — Full test table breaking down all 24 erroneous, invalid, and valid test cases along with their expected outputs.



## Testing

The test suite covers 24 cases ordered in the exact sequence the `if/elif` checks run—starting with non-numeric/erroneous inputs, moving through invalid lengths, bad prefixes, and unassigned country codes, and finishing with valid `978` and `979` numbers (including the `0` check-digit edge case).
