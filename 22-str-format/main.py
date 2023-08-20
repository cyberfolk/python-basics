weight = 65
height = 189
age = 25
phrase = f"Hello I'm Luca and I'm {height:.2f}cm tall, I'm {weight:.1f} weight and I'm {age} years old. I'm {age} years old"
phrase = phrase.format(height=65, weight=weight, age=27)
print(phrase)