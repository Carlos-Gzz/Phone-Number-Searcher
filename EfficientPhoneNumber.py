import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Match object...we will cal it 'mo'
mo = phoneNumRegex.findall(message)
print(mo)

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*?)>')
print(greedy.findall(serve))

# The .* finds everything that is not a new line, such as /n
# For that we use, re.DOTALL
prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.findall(prime))

# We can search something and change it inside the same file/text.
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

# We can even just take part of the name and modify it.
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))