input_data = '1Asdf3#4eC%*'
result = {
    "char": [],
    "vowel": [],
    "number": [],
    "specialCharacter": []
}

for ele in input_data:
    if ((ord(ele) > 64 and ord(ele) < 91) or (ord(ele) > 96 and ord(ele) < 123)):
        # 65 69 73 79 85
        upperChar = ele.upper()
        ordNum = ord(upperChar)
        if (ordNum / 65== 1 or ordNum / 69 == 1 or ordNum / 73 == 1 or ordNum / 79 == 1 or ordNum / 85 == 1):
            result["vowel"].append(ele)
        result["char"].append(ele)
    elif (ord(ele) >= 48 and ord(ele) <= 57):
        result["number"].append(ele)
    else:
        result["specialCharacter"].append(ele)
print(result)
