import zipfile
import zlib
from zipfile import ZipFile

# Build the list of candidate passwords
with open('Ashley-Madison.txt') as f:
    passwords = f.readlines()

for i, password in enumerate(passwords):
    password = password.strip()  # drop the trailing newline

    if i % 10000 == 0:
        print(f"Tried {i} passwords, currently on: {password}")

    try:
        with ZipFile('whitehouse_secrets.zip') as zf:
            zf.extractall(pwd=password.encode())
        print(f"SUCCESS! Password is: {password}")
        break  # stop so later guesses don't overwrite the real file
    except (RuntimeError, zipfile.BadZipFile, zlib.error):
        continue