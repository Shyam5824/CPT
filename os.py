import os
folder=input()
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"folder'{folder}'created")
else:
    print("Folder exits")

