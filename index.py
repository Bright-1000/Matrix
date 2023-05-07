import re,os,datetime,sys,getopt,calendar,random,smtplib,shutil,webbrowser,time,termcolor,dbm,bs4,requests,lxml,dbms
from xlwt import *
from wcwidth import table_wide
from random import randint 
from prettytable import PrettyTable
#functions
def cmdval():
 cmds=['open file manager','date','help','open calendar','send email','create pin','create password','create name','create id','create phone number','create database']
 for i in cmds:
  if cmd!=i and len(cmd)>0:
   val=re.search('^'+cmd,i)
   if val:
    print('\nDid you mean '+i+'\n')
 if len(cmd)==0:
  print('\nPlease enter a command')
def help():
 if cmd=='help':
  print('Type help() for interactive help or help(object) for help about object')
  cd=input('\n> ')
  if cd=='help()':
   print('\nWelcome to Matrix help utility!')
   print('\nIf this is your first time using Matrix you should definitely check out this tutorial on the Internet at https://XXNet.com/Matrix/Tutorial')
   print('''\nHere's a summary of the Matrix tutorial''')
   print('\nMatrix is a Terminal app written in python. Matrix has a lot of modules and packages to help with the user interaction. The main aim of Matrix is automation')
   print('Here is an example of opening a folder and editing its content with Matrix.')
   print('\n\tExample:')
   print('\n\t\t$ open file manager')
   print('\n\t\tPACKAGE FILE MANAGER OPENED')
   print('\n\t\t> open folder')
   folders=['Android','.sys.drop','Download','DCIM','Matrix','Test','Pictures']
   print('\n\t\tLIST OF FOLDERS')
   for i in folders:
    print('\n\t\t'+i)
def date():
 if cmd=="date" or cmd=="Date" or cmd=="DATE":     
    date=datetime.datetime.today()
    print(date.strftime("%a"+" "+"%B"+" "+"%Y"))
    print()
def open_cal():
 if cmd=="open calendar" or cmd=="Open calendar" or cmd=="Open calendar" or cmd=="open Calendar":
  
  year=int(input("Enter year: "))
  print()
  i=0
  for i in range(12):
   i=i+1
   print(calendar.month(year,i))
  save=str(input("Do you want to save calendar[y/n]: "))
  if save=="y" or save=="Y" or save=="y " or save=="Y ":
   i=0
   print()
   print("Do not save calendar in existing file. file will be reset")
   print()
   folder_name=str(input("Folder name: "))
   print()
   file_name=str(input("File name: "))
   print()
   f=open("/storage/emulated/0/"+folder_name+"/"+file_name,"w")
   for i in range(12):
    i=i+1
    f.write(calendar.month(year,i))
    f.write(" ")
   f.close()
   if f:
    print("calendar saved")
    print()
   else:
    print()
    print("calendar closed")
    print()
  else:
   print("Calendar closed")
   print()
 
def list_cmd():
 if cmd=="list cmd" or cmd=="List cmd" or cmd=="List CMD" or cmd=="list CMD":                     
  print("date")
  print("open file")
  print("create file")
  print("delete file")
  print("edit file")
  print("open calendar")
     
def email():
 if cmd=="send email":
  sender_mail=input("Your email account: ")
  print()
  pswd=input("Password: ")
  print()
  reciever_mail=input("Reciever email account:")
  print()
  message=input("Your message: ")
  print()
  if True:
   smtpObj=smtplib.SMTP("gmail.com",587)
   smtpObj.login(sender_mail,pswd)
   smtpObj.sendmail(sender_mail,reciver_mail,message)
   print("Email sent successfully")
   print()
  else:
   print("Unable to send email")
   print()
def file_manager():
 if cmd=="open file manager":
  while True:
   print("\nPACKAGE FILE MANAGER OPENED ")
   print()
   cmmd=input("> ")
   print()      
   if cmmd=="open folder":
    print()
    print("LIST OF FOLDERS: ")
    print()
    i=0
    with os.scandir("/storage/emulated/0") as entries:
     for entry in entries:
      i=i+1
      print(int(i),entry.name)
      print()
     folder_name=input("Folder name: ")
     print()
     i=0
     with os.scandir("/storage/emulated/0/"+folder_name) as entries:
      for entry in entries:
       i=i+1
       print(int(i),entry.name)
       print()    
     print("FOLDER OPENED")
     print()
    print("LIST OF FOLDER COMMANDS:")
    print()
    commands=["open file","edit file","delete file","rename file"]
    
    while True:
     print("Enter 'close folder' to close folder")
     print()
     cmmnd=str(input(">> "))
     print()
     if cmmnd=="open file":
      file_name=str(input("File name: "))
      print()
      
      if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):
       ext=".txt$"
       find=re.search(ext,file_name)
       if find:
        print("This is a text file!")
        print()
       ext=".py$"
       find=re.search(ext,file_name)
       if find:
        print("This is a Python file!")
        print()
       ext=".html$"
       find=re.search(ext,file_name)
       if find:
        print("This is a HTML file!")
        print()
       ext=".css$"
       find=re.search(ext,file_name)
       if find:
        print("This is a CSS file!")
        print()
       ext=".js$"
       find=re.search(ext,file_name)
       if find:
        print("This is a JavaScript file!")
        print()
       ext=".json$"
       find=re.search(ext,file_name)    
       if find:
        print("This is a JSON file!")  
        print() 
       f=open("/storage/emulated/0/"+folder_name+"/"+file_name,"r")
       fi=f.read()
       f.close()
       print(fi)
       print()
      else:
       print("File doesn't exist in this folder")
       print()
     if cmmnd=="edit file":
      file_name=str(input("File name: "))
      print()
      if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):
       ext=".txt$"
       find=re.search(ext,file_name)
       if find:
        print("This is a text file!")
        print()
       ext=".py$"
       find=re.search(ext,file_name)
       if find:
        print("This is a Python file!")
        print()
       ext=".html$"
       find=re.search(ext,file_name)
       if find:
        print("This is a HTML file!")
        print()
       ext=".css$"
       find=re.search(ext,file_name)
       if find:
        print("This is a CSS file!")
        print()
       ext=".js$"
       find=re.search(ext,file_name)
       if find:
        print("This is a JavaScript file!")
        print()
       ext=".json$"
       find=re.search(ext,file_name)    
       if find:
        print("This is a JSON file!")  
        print() 
       print("Directory:"+"/storage/emulated/0/"+folder_name+"/"+file_name)
       print()
       file=open("/storage/emulated/0/"+folder_name+"/"+file_name,"a")
       print("\nPress RETURN to start a new line.\nPress SAVE to save and close.\n\n")
       line_count = 1
       while line_count > 0:
        try:
          line = input(str(line_count) + " ")
          if line=="SAVE":
           print("\n\tSaving...")
           print("\n\tSaved")
           break
           
          file.write(line)
          file.write('\n')
          line_count += 1
          
        except :
         if line=="SAVE":
          print("\n\tSaving...")
          break
       file.close()
       print("REVIEW: ")
       print()
       fi=open("/storage/emulated/0/"+folder_name+"/"+file_name,"r")
       review=fi.read()
       fi.close
       print(review)
     if cmmnd=="delete file" or cmmnd=="Delete file":
      file_name=str(input("File name: "))
      print()
      if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):
       choice=input("Do you want to delete this file?[y/n]: ")
       if choice=="y" or choice=="Y":
        os.remove("/storage/emulated/0/"+folder_name+"/"+file_name)
        print("File deleted")
        print()
       else:
        print("Couldn't delete file")
        print()
      if choice=="n" or choice=="N":
       print("Ok")
       print()
      else:
       print("File doesn't exist")
       print()
     if cmmnd=="rename file" or cmmnd=="Rename file":
      file_name=input("File name: ")
      print()
      if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):
       new_file_name=input("New file name: ")
       os.rename("/storage/emulated/0/"+folder_name+"/"+file_name,"/storage/emulated/0/"+folder_name+"/"+new_file_name)
       print("File renamed")
      else:
       print("File doesn't exist in this folder")
       print()
     if cmmnd=="create file" or cmmnd=="Create file":
      file_name=input("File name: ")
      print()
      if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):
       print("File already exists")
      else:
       f=open("/storage/emulated/0/"+folder_name+"/"+file_name,"x")
       print("File created")
       print()
     if cmmnd=="list files":
      with os.scandir("/storage/emulated/0/"+folder_name) as entries:
       i=0
       for entry in entries:
        i=i+1
        print(int(i),entry.name)
        print()
     if cmmnd=="close folder" or cmmnd=="Close folder":
      break;
      print("Folder closed")
      print()
     
     if cmmnd=="copy file":
      file_name=input("File Name: ")
      print()
      print("Enter a folder name to copy file to")
      print()
      to=input("Copy To: ")
      print()
      copy=shutil.copy("/storage/emulated/0/"+folder_name+"/"+file_name,"/storage/emulated/0/"+to)
      if copy==True:
       print("File copied successfully")
       print()
      if copy==False:
       print("Couldn't copy file")
       print()
     if cmmnd=="copy files":
      print("Enter number of files to copy")
      print()
      num=input("No. of Files: ")
      print()
      copy=shutil.copy("/storage/emulated/0/"+folder_name+"/"+file_name,"/storage/emulated/0/"+folder_name)
      for i in range(num):
       file_name=input("File Name: ")
       print()
       print(copy)      
      print("Files copied successfully")        
     if cmmnd=="move file":
      file_name=input("File Name: ")
      print()
      print("Enter folder to move file to")
      print()
      to=input("Move To: ")
      move=shutil.move("/storage/emulated/0/"+folder_name+"/"+file_name,"/storage/emulated/0/"+to) 
      print()        
      print("File moved successfully")
      print()
      if move==False:
       print("Couldn't move file")    
     
     if cmmnd=="delete files":
      try:
       print("Enter number of files to delete")       
       print() 
       i=0
       files_num=int(input("No. of files: "))
       print()
       for files in range(files_num):
        i=i+1
        print("Enter file name")
        print()
        file_name=input("File: ")
        print()
        if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):        
         os.remove("/storage/emulated/0/"+folder_name+"/"+file_name)
         continue;
        else:
         raise;
       print("Files have been deleted successfully")
       print()
      except file_error:
       print("File doesn't exist")
      except:
       print("This code doesn't work")
     elif cmmnd=="create files":
      try:
       print("Enter number of files to create")       
       print() 
       i=0
       files_num=int(input("No. of files: "))
       print()
       for files in range(files_num):
        i=i+1
        print("Enter file name")
        print()
        file_name=input("File: ")
        print()
        if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):        
         raise file_error;
        else:
         open("/storage/emulated/0/"+folder_name+"/"+file_name,"x")
         continue;
       print("Files have been created successfully")
       print()  
      except Exception:
       print("File  exists")
      except:
       print("This code doesn't work") 
     if cmmnd=="open sub folder":
      sfolder_name=input("Sub folder name: ")
     print()
     print("LIST OF FILES IN THIS SUB FOLDER : ")
     print()
     i=0
     with os.scandir("/storage/emulated/0/"+folder_name+"/"+sfolder_name) as entries:
       for entry in entries:
        i=i+1
        print(int(i),entry.name)
        print()
     print("SUB FOLDER OPENED")
     print()
     print("LIST OF SUB FOLDER COMMANDS:")
     print()
     commands=["open file","edit file","delete file","rename file"]
    
     while True:
      print("Enter 'close sub folder' to close sub folder")
      print()
      cmmmnd=str(input(">>> "))
      print()
      if cmmmnd=="open file":
       file_name=str(input("File name: "))
       print()
      
       if os.path.exists("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name):
        ext=".txt$"
        find=re.search(ext,file_name)
        if find:
         print("This is a text file!")
         print()
        ext=".py$"
        find=re.search(ext,file_name)
        if find:
         print("This is a Python file!")
         print()
        ext=".html$"
        find=re.search(ext,file_name)
        if find:
         print("This is a HTML file!")
         print()
        ext=".css$"
        find=re.search(ext,file_name)
        if find:
         print("This is a CSS file!")
         print()
        ext=".js$"
        find=re.search(ext,file_name)
        if find:
         print("This is a JavaScript file!")
         print()
        ext=".json$"
        find=re.search(ext,file_name)    
        if find:
         print("This is a JSON file!")  
         print() 
        f=open("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name,"r")
        fi=f.read()
        f.close()
        print(fi)
        print()
       else:
        print("File doesn't exist in this folder")
        print()
      if cmmmnd=="edit file":
       file_name=str(input("File name: "))
       print()
       if os.path.exists("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name):
         
        file=open("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name,"a")
        print("\nPress RETURN to start a new line.\nPress SAVE to save and close.\n\n")
        line_count = 1
        while line_count > 0:
         try:
          line = input(str(line_count) + " ")
          if line=="SAVE":
           
           print("\n\tSaving...")
           print("\n\tSaved")
           break;
           
          file.write(line)
          file.write('\n')
          line_count += 1
          
         except :
          if line=="SAVE":
           print("\n\tSaving...")
           break
        file.close()
        print("REVIEW: ")
        print()
        fi=open("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name,"r")
        review=fi.read()
        fi.close
        print(review)
      if cmmmnd=="delete file" or cmmmnd=="Delete file":
       file_name=str(input("File name: "))
       print()
       if os.path.exists("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name):
        choice=input("Do you want to delete this file?[y/n]: ")
        if choice=="y" or choice=="Y":
         os.remove("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name)
         print("File deleted")
         print()       
        if choice=="n" or choice=="N":
         print()       
         print("Ok")
         print()
       else:
        print("File doesn't exist")
        print()
      if cmmmnd=="rename file" or cmmmnd=="Rename file":
       file_name=input("File name: ")
       print()
       if os.path.exists("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name):
        new_file_name=input("New file name: ")
        os.rename("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name,"/storage/emulated/0/"+folder_name+"/"+new_file_name)
        print("File renamed")
       else:
        print("File doesn't exist in this folder")
        print()
      if cmmmnd=="create file" or cmmmnd=="Create file":
       file_name=input("File name: ")
       print()
       if os.path.exists("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name):
        print("File already exists")
       else:
        f=open("/storage/emulated/0/"+folder_name+"/"+sfolder_name+"/"+file_name,"x")
        print("File created")
        print()
      if cmmmnd=="list files":
       with os.scandir("/storage/emulated/0/"+folder_name+"/"+sfolder_name) as entries:
        i=0
        for entry in entries:
         i=i+1
         print(int(i),entry.name)
         print()
      if cmmmnd=="close folder" or cmmnd=="Close folder":
       break;
       print("Folder closed")
       print()
     
     if cmmnd=="copy file":
      file_name=input("File Name: ")
      print()
      print("Enter a folder name to copy file to")
      print()
      to=input("Copy To: ")
      print()
      copy=shutil.copy("/storage/emulated/0/"+folder_name+"/"+file_name,"/storage/emulated/0/"+to)
      if copy==True:
       print("File copied successfully")
       print()
      if copy==False:
       print("Couldn't copy file")
       print()
     if cmmnd=="copy files":
      print("Enter number of files to copy")
      print()
      num=input("No. of Files: ")
      print()
      copy=shutil.copy("/storage/emulated/0/"+folder_name+"/"+file_name,"/storage/emulated/0/"+folder_name)
      for i in range(num):
       file_name=input("File Name: ")
       print()
       print(copy)      
      print("Files copied successfully")        
     if cmmnd=="move file":
      file_name=input("File Name: ")
      print()
      print("Enter folder to move file to")
      print()
      to=input("Move To: ")
      move=shutil.move("/storage/emulated/0/"+folder_name+"/"+file_name,"/storage/emulated/0/"+to) 
      print()        
      print("File moved successfully")
      print()
      if move==False:
       print("Couldn't move file")    
     
     if cmmnd=="delete files":
      try:
       print("Enter number of files to delete")       
       print() 
       i=0
       files_num=int(input("No. of files: "))
       print()
       for files in range(files_num):
        i=i+1
        print("Enter file name")
        print()
        file_name=input("File: ")
        print()
        if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):        
         os.remove("/storage/emulated/0/"+folder_name+"/"+file_name)
         continue;
        else:
         raise;
       print("Files have been deleted successfully")
       print()
      except file_error:
       print("File doesn't exist")
      except:
       print("This code doesn't work")
     elif cmmnd=="create files":
      try:
       print("Enter number of files to create")       
       print() 
       i=0
       files_num=int(input("No. of files: "))
       print()
       for files in range(files_num):
        i=i+1
        print("Enter file name")
        print()
        file_name=input("File: ")
        print()
        if os.path.exists("/storage/emulated/0/"+folder_name+"/"+file_name):        
         raise file_error;
        else:
         open("/storage/emulated/0/"+folder_name+"/"+file_name,"x")
         continue;
       print("Files have been created successfully")
       print()  
      except Exception:
       print("File  exists")
      except:
       print("This code doesn't work")    
   elif cmmd=="list folders":
    print("LIST OF FOLDERS IN THIS DIRECTORY")
    print()
    with os.scandir("/storage/emulated/0") as entries:  
     i=0      
     for entry in entries:
      i=i+1
      print(int(i),entry.name)
      print() 
   elif cmmd=="delete folder" or cmmd=="Delete folder":
    print("package File manager opened")
    print()
    print("List of folders in current directory:")
    print()
    with os.scandir("/storage/emulated/0") as entries:
     for entry in entries:
      print(entry.name)
      print()
    folder_name=str(input("Folder name: "))
    print()   
    os.rmdir("/storage/emulated/0/"+folder_name)     
    print("Folder deleted")
    print()

#create folder
   elif cmmd=="create folder":
#ask for folder name
    folder_name=input("Folder Name: ")
#check if folder already exists 
    if os.path.exists("/storage/emulated/0/"+folder_name) is True:  
#alert the user folder exists
     print("Folder already exists") 
#if folder doesn't exist create folder
    elif os.path.exists("/storage/emulated/0/"+folder_name) is False:     
     os.mkdir("/storage/emulated/0/"+folder_name) 
     print("Folder created successfully")
   if cmmd=="close file manager":
    
    print("PACKAGE FILE MANAGER CLOSED")
    print()
def pswdgen():
 if cmd=="generate password":
  
   password = ['a','M','L','T','b','S','c','P','d','e','f','g','h','i','j','k', 
            'N','m','J','n','U''R''o','H','Q','p','q','I','r','s','t','u','v', 
            'w','O','x','y','K','z','A','B','C','D','F','G',
            'H','I','V','W','X','Y','Z',]        
   genpass = ""
   for i in range(0,9):
    genletter=password[randint(0,49)]
    genpass=str(genletter) +str(genpass)
   time.sleep(0.1)
   print("\n\tCreating Password...")
   time.sleep(2.3)
   print("\nPassword:",genpass)
   print()
  
def pingen():
 if cmd=="generate pin" or cmd=="generate PIN":
  try:
   pinlen=int(input("No. of digits: "))
   print()
   pin=[0,1,2,3,4,5,6,7,8,9]
   genpin=""
   for i in range(pinlen):
    genNum=pin[randint(0,9)]
    genpin=str(genNum) + str(genpin)
   time.sleep(0.1)
   print("\n\tCreating PIN...")
   time.sleep(2.3)
   print("\nPIN:",genpin)
   print()
  except ValueError:
   print("\nNo. of digits should be a number not a letter")
   print()
def virus():
 if cmd=='create virus':
  print('\nPlease select your wizard')
  wizards=['Fat Jack','Kraken','Ripper','Medusa','Spy','cubic']
  x=1
  for i in wizards:
   print('\n'+str(x)+' '+i)
   x+=1
  wiz=input('\nWizard Name: ')
  if wiz=='Fat jack':
   print('\nBelow is a list of the viruses i can create')
   viruses=['storage pest','app killer']
   x=1
   for i in viruses:
    print('\n'+str(x)+' '+i)
    x+=1
   print('\nWhat virus would you like me to create')
   virus=input('\nVirus Name: ')
   if virus=='storage pest':
    vir=shutil.copy('matrix_fat_jack_storage_pest.py','/storage/emulated/0/download')
    if vir:
     print('\nYour virus has been created successfully. Open file manager, open folder Folder name: Download')
    else:
     print('''\nI'm sorry. I couldn't create the virus. Please choose another wizard''')
#Take user input
def web_scraper():
 if cmd=='scan url':
   print('Enter a hostname or IP address')
   print('If you enter an IP address, please state the port number')
   url = input('\nAddress: ')
   url_links=[]
   des=[]
   res=requests.get('http://'+url)
   soup=bs4.BeautifulSoup(res.text,'html5lib')
   meta_data=soup.find_all('meta',{'name':'description'})
   for i in meta_data:
    data=i['content']
    des.append(data)
   link=soup.find_all('a')
   num=0
   for anchor in link:
    links='http://'+url+'/'+anchor['href']
    url_links.append(links)
    num+=1
   for i in url_links:
    get=requests.get(i)
    get_soup=bs4.BeautifulSoup(get.content,'html5lib')
    num=0
    anchor=get_soup.find_all('a')
   print('\nLIST OF LINKS IN THIS URL: ')
   for i in url_links:
    print('\n'+i)
   for i in soup.find_parents('p'):
    print(i.text)
def xploit():
 if cmd=='open xploit':
  print('\n\tXPLOIT OPENED')
  while True:
   xcmd=input('\nxploit>: ')
   if xcmd=='scan url':
    url=input('\nURL: ')
    url_links=[]
    meta_des=[]
    meta_keys=[]
    if len(url)>0:
     res=requests.get('http://'+url+'/')
     try:
      soup=bs4.BeautifulSoup(res.text,'html5lib')
      links=soup.find_all('a')
      meta_description=soup.find_all('meta',{'name':'description'})
      meta_keywords=soup.find_all('meta',{'name':'keywords'})
      for anchor in links:
       link='http://'+url+'/'+anchor['href']
       url_links.append(link)
      for description in meta_description:
       descriptions=description['content']
       meta_des.append(descriptions)
      for key in meta_keywords:
       keys=key['content']
       meta_keys.append(keys)
      num=0
      print('\nURL META DESCRIPTION: ')
      for i in meta_des:
       print('\n'+str(i))
      print('\nURL META KEYWORDS: ')
      for i in meta_keys:
       print('\n'+str(i))
      print('\nLIST OF LINKS IN THIS URL: ')
      for i in url_links:
       num+=1
       print('\n'+str(num)+' '+i)
       try:
        res=requests.get(i)
        link_in_links=[]
        if res.status_code==200:
         soup=bs4.BeautifulSoup(res.content,'html5lib')
         link=soup.find_all('a')
         print('\nLIST OF LINKS IN THIS LINK')
         for anchor in link:
          a_tag='http://'+url+'/'+anchor['href']
          link_in_links.append(a_tag)
          if len(link_in_links)<1:
           print('\nTHERE IS NO LINK HERE')
          else:
           for i in link_in_links:
            print('\n     '+i)
       except:
        print('\nError: Couldn\'t get links in this link')
     except:
      print('''\nNetwork error. Couldn't connect''')
    else:
     print('\nPLEASE ENTER A VALID URL')
     
print("Welcome to Matrix!")
print("\nWebsite:    https://XXNet.com/matrix")
print("\nForum:      https://XXNet.com/matrix/community")    
print("\nWorking with packages:")
print("\n * Search packages:    search <query>")    
print("\n * Install package:    install <package>")
print("\n * Upgrade packages:   upgrade")
print("\nReport issues at https://XXNet.com/matrix/issues")    
print('''\nType 'help', 'copyright','credits' or 'licence' for more information''')
while True:
 cmd=input("\n$ ")
 cmdval()
 help()
 date()
 pingen()
 pswdgen()
 list_cmd()
 open_cal()
 web_scraper()
 virus()
 xploit()
 file_manager()
 email()
 if cmd=="exit":
  exit=input("Do you want to exit?[y/n]: ")
  if exit=="y":
   break;
  if exit=="n":
   print()
   continue;

    