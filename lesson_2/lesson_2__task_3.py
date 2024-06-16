import re

# • Напишіть приклад регулярного виразу, який збігається з "d", "dog", "dogog", але не
# збігається з "dogogog".

pattern = r'd(og){0,2}$'
strings = ["d", "dog", "dogog", "dogogog"]
print(f'\t{pattern = }')
for _ in strings:
    print(f"string = '{_}'   {re.match(pattern, _) is not None}")

# • Напишіть приклад регулярного виразу, який збігається одразу з трьома рядками: "dog", "box", "bog".

pattern = r'[db]o[gx]'
strings = ["dog", "box", "bog"]
print(f'\t{pattern = }')
for _ in strings:
    print(f"string = '{_}'   {re.match(pattern, _) is not None}")

# • Напишіть приклад регулярного виразу, який не збігається одразу з трьома рядками:
# "dog", "box", "bog", але збігається з “cot”.

pattern = r'[^db]o[^gx]'
strings = ["dog", "box", "bog", "cot"]
print(f'\t{pattern = }')
for _ in strings:
    print(f"string = '{_}'   {re.match(pattern, _) is not None}")

# • Напишіть приклад регулярного виразу, який збігається одразу з трьома рядками: "cat", "cbt", "ctt".

pattern = r'c[abt]t'
strings = ["cat", "cbt", "ctt"]
print(f'\t{pattern = }')
for _ in strings:
    print(f"string = '{_}'   {re.match(pattern, _) is not None}")

# • Напишіть приклад регулярного виразу, який не збігається одразу з трьома рядками: "cat", "cbt", "ctt".

pattern = r'c[^abt]t'
strings = ["cat", "cbt", "ctt"]
print(f'\t{pattern = }')
for _ in strings:
    print(f"string = '{_}'   {re.match(pattern, _) is not None}")

# • Напишіть приклад регулярного виразу, що збігається з "c", "cat", "catat" або "catatatatat".

pattern = r'(c(at){0,2}$|c(at){5})'
strings = ["c", "cat", "catat", "catatatatat"]
print(f'\t{pattern = }')
for _ in strings:
    print(f"string = '{_}'   {re.match(pattern, _) is not None}")

# • Напишіть приклад регулярного виразу, який збігатиметься “c”, “cat”, але не збігатиметься
# повністю з “catat” чи “catatatatat”, а лише з “cat” у них.

pattern = r'c(at)?'
strings = ["c", "cat", "catat", "catatatatat"]
print(f'\t{pattern = }')
for _ in strings:
    print(f"string = '{_}'   {re.match(pattern, _) is not None}")
