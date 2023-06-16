import os

source="newFile.txt"
destination="newFile.py"

os.rename(source,destination)
print("source path renamed to destination path succefully")