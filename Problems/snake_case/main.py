value = str(input().strip())
output = value[0].lower() + ''.join(('_{}'.format(value[i].lower()) if value[i].isupper() else value[i] for i in range(1, len(value))))
print(output)
