path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 289 (0-indexed: 288) is: '\t\t\t\t\t</div>\n'  (5 tabs - closes content-box)
# Line 290 (0-indexed: 289) is: '\t\t\t\t</div>\n'    (4 tabs - incorrectly closes main-content)
# We need to INSERT a line '\t\t\t\t\t\t</div>\n' (6 tabs - closes skills row) before line 290

# Verify line 289 and 290 first
l289 = lines[288]  # 0-indexed
l290 = lines[289]
print(f"L289: {repr(l289)}")
print(f"L290: {repr(l290)}")

expected_289 = '\t\t\t\t\t</div>\n'
expected_290 = '\t\t\t\t</div>\n'

if l289 == expected_289 and l290 == expected_290:
    # Insert the missing skills row close at position 289 (between 288 and 289)
    new_line = '\t\t\t\t\t\t</div><!-- /#skills -->\n'
    lines.insert(289, new_line)
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('SUCCESS - inserted missing skills closing div')
    # Verify
    for i, line in enumerate(lines[286:296], start=287):
        print(f"Line {i}: {repr(line)}")
else:
    print('MISMATCH - lines not as expected')
    print(f"Expected L289: {repr(expected_289)}")
    print(f"Expected L290: {repr(expected_290)}")
