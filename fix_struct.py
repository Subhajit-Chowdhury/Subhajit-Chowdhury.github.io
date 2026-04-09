import sys

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 291 (0-indexed: 290) is the premature main-content close: '\t\t\t\t</div>\n' (4 tabs)
# Achievements at line 292 (idx 291) should be INSIDE main-content
# The close of main-content should be AFTER achievements (currently at line 314 idx 313 = 4 tabs)
# So we just DELETE line 291 (idx 290)

idx = 290  # 0-indexed = line 291
line_to_remove = lines[idx]

print(f"Removing line {idx+1}: {repr(line_to_remove)}")

if line_to_remove == '\t\t\t\t</div>\n':
    lines.pop(idx)
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    sys.stdout.buffer.write(b'SUCCESS - removed premature main-content closing div\n')
    # Print context
    for i, line in enumerate(lines[287:297], start=288):
        sys.stdout.buffer.write(f"Line {i}: {repr(line)}\n".encode('ascii', errors='replace'))
else:
    sys.stdout.buffer.write(f"MISMATCH: {repr(line_to_remove)}\n".encode('ascii', errors='replace'))
