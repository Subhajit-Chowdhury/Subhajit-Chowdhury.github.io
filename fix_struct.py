path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Current state (0-indexed):
# Line 290 (idx 289): '\t\t\t\t\t\t</div><!-- /#skills -->\n'   (6 tabs - closes skills row) ✓
# Line 291 (idx 290): '\t\t\t\t</div>\n'                          (4 tabs - closes #main-content) ← WRONG position
# Line 292 (idx 291): '\t\t\t\t\t\t<div ... id="achievements">\n'  (6 tabs) ← outside main-content

# Fix: remove the 4-tab </div> from idx 290, and we need to:
# - Keep achievements inside main-content
# - After achievements closing </div> sequence, THEN close main-content

# Let's find the achievements closing sequence
for i, line in enumerate(lines[289:320], start=290):
    print(f"Line {i}: {repr(line)}")
