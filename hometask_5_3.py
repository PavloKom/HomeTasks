import string

hash_name = (input("Enter a string: "))
result = ("#" + hash_name.title().replace(" ", "").replace('.', '').replace(',', '')
          .replace('.', '')).replace('!', '').replace(';', '').replace('/', '').replace(':', '')
if len(result) > 140:
    result = result[:140]

# for i in hash_name:
# if i in string.punctuation:
#   hash_name = hash_name.replace(i, '') чомусь не працює, підкажете?

print(result)
