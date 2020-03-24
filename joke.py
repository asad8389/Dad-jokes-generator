import requests
from pyfiglet import figlet_format
from random import choice
import sys

print(figlet_format('Dad Joke 3000'))

topic = input('Let me tell you a joke! Give me a topic:')

res = requests.get('https://icanhazdadjoke.com/search',
                   headers={'Accept': 'application/json'},
                   params={'term': topic}
                   )


result = res.json()['results']
jokes = []
if not result:
    print(f"Sorry! i don't have any joke about {topic}, please try again later)")
    sys.exit()
else:
    print(f"I have {len(result)} jokes")
    print("one of them is:")
    print(choice(result)['joke'])
