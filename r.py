import re


# l=re.match(r'^\d{3}\-\d{3,8}$','010-12345')
# print(l)
# l=re.match(r'^\d{3}\-\d{3,8}$','010 12345')
# print(l)

#切分字符串
# l='a b   c'
# print(l.split(' '))
# print(re.split(r'\s+',l))

# l='a,b, c  d'
# print(re.split(r'[\s\,]+',l))

# l='a,b;; c   de'
# print(re.split(r'[\s\,\;]+',l))

#分组
# l=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
# print(l.group(0),l.group(1),l.group(2),l.groups())

#编译
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')

l=re_telephone.match('010-12345').groups()
print(l)