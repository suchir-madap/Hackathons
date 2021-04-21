
print("Suchir")
print('saketh')


for i in range(7):
    print('jello')

def recursive_prac(hello):
    if hello > 1:
        return hello + recursive_prac(hello - 1)
    if hello == 1:
        return hello 


print(recursive_prac(3))