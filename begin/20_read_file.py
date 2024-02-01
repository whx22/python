"""
# import class or function from module
from module_name import class_name
from module_name import function_name
"""

from pathlib import Path
path = Path("file_read_operation.txt")
content = path.read_text()
print(content)
lines = content.splitlines()
for line in lines:
    print(line)