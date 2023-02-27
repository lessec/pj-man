t import os, shutil


srcip1 = ' - 10.0.0.1'
srcip2 = ' - 10.0.0.2'
srcip3 = ' - 10.0.0.3'
srcip4 = ' - 10.0.0.4'
srcip5 = ' - 10.0.0.5'
srcip6 = ' - 10.0.0.6'


def fwip(srcip, Sts):
    srcipst = ' ... '
    return srcip+srcipst+Sts+'\n'


def newreadme(pjpath, pjname, pjtype, pjaddress, pjsitetype, pjdescription):
    f = open(pjpath+'README.txt', 'w', encoding="utf8")
    f.write(pjname+'\n\n\nINFORMATION\n - Name: '+pjname+' ('+pjtype+')\n - Address: '+pjaddress+' ('+pjsitetype+' Server)\n\n\n')
    f.write('FIREWALL\n'+fwip(srcip1, 'Nothing')+fwip(srcip2, 'Nothing')+fwip(srcip3, 'Nothing')+fwip(srcip4, 'Nothing')+fwip(srcip5, 'Nothing')+fwip(srcip6, 'Nothing')+'\n\n')
    f.write('DESCRIPTION\n'+pjdescription)
    f.close()


def fwstatus(pjpath, status):
    with open(pjpath+'README.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
        fwline = [i for i in range(len(lines)) if 'FIREWALL' in lines[i]][0]
    with open(pjpath+'README.txt', 'w', encoding="utf8") as f:
        for line, line_i in enumerate(lines):
            if line_i is lines[fwline]:
                # f.write('FIREWALL\n'+status+'\n')
                f.write('FIREWALL\n')
            elif line_i is lines[fwline+1]:
                f.write(fwip(srcip1, status))
            elif line_i is lines[fwline+2]:
                f.write(fwip(srcip2, status))
            elif line_i is lines[fwline+3]:
                f.write(fwip(srcip3, status))
            elif line_i is lines[fwline+4]:
                f.write(fwip(srcip4, status))
            elif line_i is lines[fwline+5]:
                f.write(fwip(srcip5, status))
            elif line_i is lines[fwline+6]:
                f.write(fwip(srcip6, status))
            else:
                f.write(lines[line])


def descr(pjpath, desc):
    with open(pjpath+'README.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
        fwline = [i for i in range(len(lines)) if 'DESCRIPTION' in lines[i]][0]
    with open(pjpath+'README.txt', 'w', encoding="utf8") as f:
        for line, line_i in enumerate(lines):
            if line_i is lines[fwline]:
                f.write('DESCRIPTION\n')
            elif line_i is lines[fwline+1]:
                f.write(desc)
            else:
                f.write(lines[line])


def makedir(pjpath, dirname):
    if os.path.isdir(pjpath+dirname) is False:
        os.makedirs(pjpath+dirname)
        print('Generated "'+dirname+'" directory')


def main():
    dirpath = '..'
    finishpath = '../Finish'
    divline = '='*70

    print('\nPROJECT DIRECTORY MANAGER\n')
    dirls = ['Start New Project']
    dirls += [dir for dir in os.listdir(dirpath)]
    dirls += ['Quit Project Manager']
    print('Your project directory list: ', len(dirls)-2)
    for i in enumerate(dirls):
        print(' ', i[0], i[1])

    dirnum = int(input("Choose option number: "))
    print(divline+'\n'+dirls[int(dirnum)]+'\n')
    if dirnum == 0:
        newprojname = input("Enter a project name: ")
        if os.path.isdir(dirpath+'/'+newprojname) is True:
            print('Already exist project name')
            return
        newprojtype = int(input("Enter a project type (1: Senario, 2: Check List): "))
        if newprojtype == 1:
            newprojtype = 'Senario'
        elif newprojtype == 2:
            newprojtype = 'Check List'
        else:
            print('Wrong type number')
            return
        newaddress = input("Enter a project address: ")
        newsitetype = input("Enter a project site type (1: DEV, 2: PRD): ")
        if newsitetype == 1:
            newsitetype = 'DEV'
        elif newsitetype == 2:
            newsitetype = 'PRD'
        else:
            print('Wrong type number')
            return
        newdescription = input("Enter a project description: ")
        dirpath = dirpath + '/' + newprojname + '/'

        print(divline)
        os.makedirs(dirpath)
        print ('Generated "'+newprojname+'" directory')
        makedir(dirpath, 'Sources')
        makedir(dirpath, 'Pictures')
        newreadme(dirpath, newprojname, newprojtype, newaddress, newsitetype, newdescription)
        print('Successfully generate "'+newprojname+'" project')
    if dirnum == len(dirls)-1:
        print('Bye!')
        return
    else:
        dirpath = dirpath + '/' + dirls[int(dirnum)] + '/'
        updatenum = int(input("Enter a update type (0: Finish, 1: Firewall, 2: Description, 3: Remove): "))
        if updatenum == 0:
            rusure = input('Are you sure move "'+dirls[int(dirnum)]+'" project? (y/n): ')
            if rusure == 'y' or rusure == 'Y'  or rusure == 'yes' or rusure == 'Yes' or rusure == 'YES':
                if os.path.exists(dirpath) is True:
                    if os.path.isdir(finishpath) is True:
                        shutil.move(dirpath, finishpath)
                        print('Moved "'+dirls[int(dirnum)]+'" project')
                    else:
                        print('Can\'t find "'+finishpath+'" directory')
                    return
                else:
                    print('Can\'t find project')
            else:
                print('Canceled')
                return
        elif updatenum == 1:
            if os.path.exists(dirpath) is True:
                pjupdate = int(input("Enter firewall status (0: Nothing, 1: Progressing, 2: Done): "))
                if pjupdate == 0:
                    fwstatus(dirpath, 'Nothing')
                if pjupdate == 1:
                    fwstatus(dirpath, 'Progressing')
                elif pjupdate == 2:
                    fwstatus(dirpath, 'Ok')
                else:
                    print('Wrong type number')
                    return
                print('Updated "'+dirls[int(dirnum)]+'" project\'s firewall status on README.txt')
            else:
                print('Can\'t find README.txt')
        elif updatenum == 2:
            if os.path.exists(dirpath) is True:
                pjupdate = input("Enter a project description: ")
                descr(dirpath, pjupdate)
                print('Updated "'+dirls[int(dirnum)]+'" project\'s description on README.txt')
            else:
                print('Can\'t find README.txt')
        elif updatenum == 3:
            rusure = input('Are you sure remove "'+dirls[int(dirnum)]+'" project? (y/n): ')
            if rusure == 'y' or rusure == 'Y'  or rusure == 'yes' or rusure == 'Yes' or rusure == 'YES':
                if os.path.exists(dirpath) is True:
                    shutil.rmtree(dirpath)
                    print('Removed "'+dirls[int(dirnum)]+'" project')
                else:
                    print('Can\'t find project')
            else:
                print('Canceled')
                return
        
        if updatenum == 1 or updatenum == 2:
            makedir(dirpath, 'Sources')
            makedir(dirpath, 'Pictures')
    return


if __name__ == '__main__':
    main()
