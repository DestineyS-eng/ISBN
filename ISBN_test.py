ISBN_CODES_BY_PREFIX_978 = [
        # 1-Digit
        "0", "1", "2", "3", "4", "5", "7",

        # 2-Digit
        "65", "66",
        "80", "81", "82", "83", "84", "85", "86", "87", "88", "89",
        "90", "91", "92", "93", "94",

        # 3-Digit (600–635)
        "600", "601", "602", "603", "604", "605", "606", "607", "608", "609",
        "611", "612", "613", "614", "615", "616", "617", "618", "619", "620",
        "621", "622", "623", "624", "625", "626", "627", "628", "629", "630",
        "631", "632", "633", "634", "635",

        # 3-Digit (950–989)
        "950", "951", "952", "953", "954", "955", "956", "957", "958", "959",
        "960", "961", "962", "963", "964", "965", "966", "967", "968", "969",
        "970", "971", "972", "973", "974", "975", "976", "977", "978", "979",
        "980", "981", "982", "983", "984", "985", "986", "987", "988", "989",

        # 4-Digit (9900–9989)
        "9910", "9915", "9916", "9920", "9921", "9922", "9923", "9925", "9927",
        "9934", "9935", "9936", "9939", "9946", "9948", "9949", "9950", "9956",
        "9957", "9958", "9960", "9966", "9970", "9971", "9972", "9973", "9974",
        "9975", "9976", "9980",

        # 5-Digit (99900–99999)
        "99901", "99903", "99904", "99911", "99912", "99913", "99914", "99915",
        "99916", "99921", "99940", "99941", "99942", "99943", "99944", "99950",
        "99957", "99958", "99959", "99960", "99962", "99963", "99964", "99967",
        "99968", "99969", "99970", "99971", "99972", "99973", "99974", "99980",
        "99982", "99983", "99984", "99985", "99986"]

ISBN_CODES_BY_PREFIX_979=["8", "10", "11", "12", "13"]


def first3digits (s):
    s=s[:3]
    if s=="978" or s=="979":
        return True
    return False

def CountryPrefix(s):
    remaining=s[3:]
    prefix=s[:3]
    if prefix=="978":
        for num in ISBN_CODES_BY_PREFIX_978:
            if remaining.startswith(num) and 4<=(len(remaining)-len(num))<=8:
                return True
        return False
    elif prefix=="979":
        for number in ISBN_CODES_BY_PREFIX_979:
            if remaining.startswith(number) and 7<=(len(remaining)-len(number))<=8:
                return True
        return False 

def lengthCheckfirst(s):
    if len(s)==12:
        return True
    return False
    
def CheckdigitCal(isbn12):
   
    total=0
    for i in range(len(isbn12)):
        char=isbn12[i]
        digit=int(char)
        if (i+1)%2==0:
            total+=digit*3
        elif (i+1)%2!=0:
            total += digit

    remainder=total%10
    checkdigit=10-remainder
    if checkdigit==10:
            checkdigit=0

    return isbn12+str(checkdigit)

with open("ISBNnum.txt","r") as file:
    for line in file:
        File_line = line.strip()
        if not File_line:
            continue
        with open("ISBN_Output.txt","w") as file:
            
            if not File_line.isdigit():
                file.write(f"\nerror  {File_line} is not a number")
            elif not lengthCheckfirst(File_line):
                file.write(f"\nerror {File_line} is an incorrect length.")
            elif not first3digits (File_line):
                file.write(f"\nerror {File_line} has a incorrect 3-digit prefix")
            elif not CountryPrefix (File_line):
                file.write(f"\nerror {File_line} has no country number ")
            else:
                file.write(f"\nyour final ISBN is: {CheckdigitCal (File_line)}")
