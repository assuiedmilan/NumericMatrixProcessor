string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

print(sum((1 if x in vowels else 0 for x in string)))
