code = "llolllollolllooollloolllollllllllolllooolllllolloollollllllollllllllolloololoolllollllllllloolllllllllollolllolllolloololoollllloollollllloololllolloollollollllolllolooloollloolllollolllloolollllllollllloolooloolllololoolllllolllollollloollllololollllolooollooloololllolllollllololoolololllolloololoolllloloolololoolololollooollollllllllloolooloolllllllolllooollolllloollooloolloolllllllooolooloolllllllllllloollollolloollollollllolloololooolloololllllloollollloololooooolloollolllolooolllolllllllllollollollllollloollllolllolllloloololllllolllolooloollllollolllollllollloloollloollloollloollloollloollloollloollloollloollloollloollloollloollloollloollloollloollloo"
# 665 digitos

binary_string = code.replace("l", "1").replace("o", "0")

# trocar 1 por 0 e vice versa
binary_inverted = ""
for binary in binary_string:
    for char in binary:
        if char == "1":
            binary_inverted += "0"
        else:
            binary_inverted += "1"

print(binary_string)
print(binary_inverted)
