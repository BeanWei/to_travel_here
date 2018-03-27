import re

test = 'href="/wenda/detail-10921684.html"'

print (re.findall(r'href="/wenda/detail-(.*?).html"',test))