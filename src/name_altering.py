name = '1395. Count Number of Teams'
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


