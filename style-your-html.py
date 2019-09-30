#!/usr/bin/env python
# coding: utf-8

# In[6]:


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


# In[7]:


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

## prompt user to select file, save file chosen to 'subfile_og'

shift2 = 0
while 1 > shift2 or lenx < shift2:
    try:
        shift2 = int(input(mystring))
    except ValueError:
        print('Try again')
subfile_og = x[shift2-1]
print('You chose: '+subfile_og)


# In[8]:


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
htmlbody_og= os.path.join(subfolder,subfile_og)
subfile="body_"+subfile_og
htmlbody= os.path.join(subfolder,subfile)
#print(htmlbody)
os.rename(htmlbody_og,htmlbody)



filenames = [htmlheader,htmlbody]


# In[9]:


#outname=input('\nSpecify your output file name. Include the .html filetype. \n  Your response: ')
#outpath=os.path.join(subfolder,outname)
#print(outfile)

#with open(outpath, 'w') as outfile:
with open(htmlbody_og, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


# In[10]:


#print(htmlheader)
#print(htmlbody)
#print(outpath)
print(htmlbody)
print(htmlbody_og)
print(subfile_og)
print(subfile)


# In[ ]:




