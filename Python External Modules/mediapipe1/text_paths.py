import sys

spacer = "- " * 5

for each in sys.path:
	print(each)

print(spacer)

python_ext = tdu.expandPath(ipar.ExtPython.Target)

if python_ext not in sys.path:
	sys.path.append(python_ext)

for each in sys.path:
	print(each)

print(spacer)