name = '172. Factorial Trailing Zeroes'
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

# py_file = '/home/jcglqmoyx/projects/pycharm_projects/leetcode/src/' + name + '.py'
# os.mknod(py_file)
#
# java_file = '/home/jcglqmoyx/projects/idea_projects/leetcode/src/' + java_cpp_name + '.java'
# cpp_file = '/home/jcglqmoyx/projects/clion_projects/leetcode_cpp/src/' + java_cpp_name + '.cpp'
# os.mknod(java_file)
# os.mknod(cpp_file)
#
# java_file = open(java_file, 'wb')
# content = 'public class ' + java_cpp_name + '{}'
# java_file.write(bytes(content))
# java_file.close()
