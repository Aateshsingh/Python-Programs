import os
#os.rename("clutteredFolder/file.txt","clutteredFolder/6.txt")
files = os.listdir("clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
        i = i + 1