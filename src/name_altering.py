# name = '1534. Count Good Triplets'
name = input('题目:\n')
name = 'p' + name
name = name.replace('. ', '_')
name = name.replace(' ', '_')
name = name.lower()
print(name)

java_cpp_name = name.replace('_', ' ')
java_cpp_name = java_cpp_name[0] + java_cpp_name[1:]
java_cpp_name = java_cpp_name.title()
java_cpp_name = java_cpp_name.replace(' ', '_', 1)
java_cpp_name = java_cpp_name.replace(' ', '')
print(java_cpp_name)








