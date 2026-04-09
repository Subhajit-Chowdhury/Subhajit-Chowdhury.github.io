path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

tab10 = '\t' * 10
tab11 = '\t' * 11

old = (tab10 + '<h5>Bachelor of Technology (B.Tech) in Computer Science and Engineering</h5>\n' +
       tab10 + '<li>Relevant courses: Data Structures &amp; Algorithms, Operating Systems, Database Management Systems</li>\n' +
       tab10 + '<li>GPA: 8.90</li>')

new_val = (tab10 + '<h5>Bachelor of Technology (B.Tech) in Computer Science and Engineering</h5>\n' +
           tab10 + '<ul class="section-list">\n' +
           tab11 + '<li>Relevant courses: Data Structures &amp; Algorithms, Operating Systems, Database Management Systems</li>\n' +
           tab11 + '<li>GPA: 8.90</li>\n' +
           tab10 + '</ul>')

if old in c:
    c = c.replace(old, new_val)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('SUCCESS - wrapped education li tags')
else:
    # Try without &amp;
    old2 = old.replace('&amp;', '&')
    new_val2 = new_val.replace('&amp;', '&')
    if old2 in c:
        c = c.replace(old2, new_val2)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print('SUCCESS (plain &) - wrapped education li tags')
    else:
        idx = c.find('Bachelor of Technology')
        print('NOT FOUND. Context:')
        print(repr(c[idx-5:idx+300]))
