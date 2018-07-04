from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("Questions:")
print(f"Do u like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
You said {likes} about liking me.
You live in {lives}. Where's that?
And you have a {computer} 'puter. Holla.
""")
