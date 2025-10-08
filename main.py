import os

def pathconf():
    if not os.path.exists("path.txt"):
        path = input("Enter the path to base folder: ")
        with open("path.txt",'w') as file:
            file.write(path)
        print("Path has been added")

    with open("path.txt","r") as file:
            fileContents = file.read()
    
    return fileContents

def displayContents(fileContents):
    if os.path.exists(fileContents):
        i=0
        for (path, dirs, files) in os.walk(fileContents):
            for dir in dirs:
                 print(i,dir,"/")
                 i+=1
            for file in files:
                 print(i,file)
                 i+=1
            break
            
            

    else:
         print("Path not found")

def main():
    fileContents = pathconf()
    displayContents(fileContents)

if __name__ == "__main__":
    main()

