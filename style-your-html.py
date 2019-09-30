#!/usr/bin/env python
# coding: utf-8

# In[1]:


## import os

import os
os.chdir('/Users/dylandaniels/Documents/github-repos/hnn-tutorials')
parentdirectory=os.getcwd()

#y=os.listdir()
#print(y)

y = [f.name for f in os.scandir(parentdirectory) if f.is_dir() and not f.name == '.ipynb_checkpoints' and not f.name == '.git' and not f.name == 'html-styling']  
#print(y)

leny=len(y)
#print(leny)

count=1
mystring="Select file \n\n"
for e in y:
    mystring += str(count) + " = " + e + " \n" 
    count=count+1
mystring+="\nYour response: "
#print(mystring)

## prompt user to select file, save file chosen to 'subfile'

shift = 0
while 1 > shift or leny < shift:
    try:
        shift = int(input(mystring))
    except ValueError:
        print('Try again')
subfolder = y[shift-1]
#print(subfolder)

subfolder=os.path.join(parentdirectory,subfolder)
#If you cannot assume / to be the folder separator, do this: glob(os.path.join(path_to_directory, "*", ""))
#print(subfolder)


# In[2]:


## change directory to 'subfolder' as defined above

os.chdir(subfolder)

## save directory contents in list 'x' and save length of list in 'lenx'

x = os.listdir()
lenx = len(x)
#print(lenx)
#print(x)

## define user prompt based on list 'x' and 'lenx'

count=1
mystring="Select file from the list below \n\n"
for e in x:
    mystring += str(count) + " = " + e + " \n" 
    count=count+1
mystring+="\nYour response: "
#print(mystring)

## prompt user to select file, save file chosen to 'subfile'

shift2 = 0
while 1 > shift2 or lenx < shift2:
    try:
        shift2 = int(input(mystring))
    except ValueError:
        print('Try again')
subfile = x[shift2-1]
print('You chose: '+subfile)


# In[3]:


## change directory to 'parentdirectory' as defined above; not necessary

#os.chdir(parentdirectory)

## define file a

#htmlheader='/Users/dylandaniels/Documents/github-repos/hnn-tutorials/html-styling/page-setup.html'
#print(parentdirectory)
headersubfolder='html-styling'
headerfile='page-setup.html'
htmlheader= os.path.join(parentdirectory,headersubfolder)
htmlheader=os.path.join(htmlheader,headerfile)
#print(htmlheader)
htmlbody= os.path.join(subfolder,subfile)
#print(htmlbody)

filenames = [htmlheader,htmlbody]


# In[4]:


outname=input('Specify your file name. Include the .html filetype. \n  Your response: ')
outpath=os.path.join(subfolder,outname)
#print(outfile)

with open(outpath, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


# In[ ]:





# In[ ]:




