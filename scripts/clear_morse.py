brute_data = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>++++++++++++++++++.+.++++++++.-------.--.++.+.>>---.<<++++.>>+..++.<<.----.-.+++.-----.+++++.----.+++++.>>++.<<------.++++++.+++.>>--.++.<<--------.+++++++.>>----.<<---.-----.."

clean_data = ""

for char in brute_data:
    if char not in [".", "-"]:
        continue
    clean_data += char

inverted_data = ""

for char in clean_data:
    if char == "-":
        inverted_data += "."
    else:
        inverted_data += "-"

print(clean_data)
print(inverted_data)
