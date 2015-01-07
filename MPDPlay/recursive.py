import os

def GetListForBackup(PathForBackup):
    ListForBackup = []
    for file in os.listdir(PathForBackup):
        path = os.path.join(PathForBackup, file)
        if not os.path.isdir(path):
            #ListForBackup.append(path)
	    pass
        else:
	    ListForBackup.append(path)
            ListForBackup += GetListForBackup(path)
    return ListForBackup
c=0

mydir=GetListForBackup('/var/log')

while mydir[c]:
    print mydir[c]
    c+=1