class Dir:
	def __init__(self,dirname):
		self.dirname = dirname
		self.folderlist = {}
		self.filelist = []
		
	def createfolder(self,folder):
		if(folder not in self.folderlist):
			self.folderlist[folder.dirname] = folder
			print(f"Folder {folder.dirname} CREATED in {self.dirname}")
		else:
			print(f"Folder{folder.dirname} PRESENT")

	def createfile(self,file):
		if(file not in self.filelist):
			self.filelist.append(file)
			print(f"File {file} CREATED in {self.dirname}")
		else:
			print(f"File {file} PRESENT")


	def remove(self,name):
		if(name in self.filelist):
			self.filelist.remove(name)
			print(f"{name} REMOVED from {self.dirname}")
		elif(name in self.folderlist):
			self.folderlist.pop(name)
			print(f"{name} REMOVED from {self.dirname}")
		else:
			print("Doesn't Exist")

	def __repr__(self):
		return(f"{self.dirname}")	
	

dirname = input("Directory name:")
d  = Dir(dirname)
print(f"Directory {d.dirname} CREATED\n")
while(1):
        print("1.Create Folder\n2.Create File\n3.Remove\n4.Open Folder\n5.Insert\n6.Display\n7.Exit\n")
        x = int(input("\nChoose option "))
        if(x==1):
                foldername = input("Give directory name: ")
                folder = Dir(foldername)
                d.createfolder(folder)
        elif(x==2):
                filename = input("Give file name: ")
                d.createfile(filename)
        elif(x==3):
                filename = input("Give file/directory name: ")
                d.remove(filename)
        elif(x==4):
                foldername = input("Give foldername to open: ")
                if(foldername in d.folderlist):
                        open_folder = d.folderlist[foldername]
                        print(f"Path: {d.dirname}/{foldername}")
                        for name in open_folder.filelist:
                                print(f"{name} <- file")
                print()
        elif(x==5):
                foldername = input("Enter foldername:" )
                filename = input("Enter filename: ")
                if(foldername not in d.folderlist):
                        print("Folder not in list")
                else:
                        d.folderlist[foldername].createfile(filename)
        elif(x==6):
                print("*****************************")
                print(f"\nDirectory ->{d.dirname}\n")
                for folder in d.folderlist:
                        print(f"{folder} <-folder")
                        open_folder = d.folderlist[folder]
                        for name in open_folder.filelist:
                                print(f"    ->{name} <- file")

                for file in d.filelist:
                        print(f"{file} <-file")
                if(d.folderlist == {} and d.filelist==[]):
                        print("Empty\n")
                print("*****************************")
                print()
        elif(x==7):
                print("Bye")
                exit(0)
        else:
                print("Invalid Input")

