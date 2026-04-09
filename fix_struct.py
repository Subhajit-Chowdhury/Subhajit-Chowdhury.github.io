path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line numbers (0-indexed)
# We need to:
# 1. Find line 287 (Git </div>) - last skill item closes
# 2. Line 288: closes skills-container   -> keep
# 3. Line 289: closes content-box        -> keep
# 4. Line 290: closes main-content       -> REPLACE with: close skills row + keep main-content open
# Then achievements is already there starting line 291

# Current line 290 (0-indexed: 289) is: \t\t\t\t</div>
# We need to insert ONE MORE </div> after 289 to close the skills row,
# and then NOT close main-content yet (remove the extra </div> at 290)

# Let's verify what lines 287-295 look like
for i, line in enumerate(lines[286:296], start=287):
    print(f"Line {i}: {repr(line)}")
