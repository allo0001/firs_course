import os
import django


root_dir = django.__path__[0]
result = {}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        path = os.path.join(root, file)
        size = os.path.getsize(os.path.join(root, file))
        size = 10 ** len(str(size))
        
        result.setdefault(size, 0)
        result[size] += 1
        
print(result)
        