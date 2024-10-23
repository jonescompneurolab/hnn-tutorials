###############################################################################

import os
import sys
import subprocess
import pypandoc

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

if 'pypandoc' in installed_packages:
    print('pypandoc installed. Proceeding to next step.')
elif not 'pypandoc' in installed_packages:
    input('\nIMPORTANT: This script requires pypandoc (and, in turn, pandoc) to run. See the information below on installing pypandoc (and pandoc). Press any key to close this message and halt the script. \n\n------------------------------\n-------- Installation --------\n------------------------------\n\nSee: https://pypi.org/project/pypandoc/\n\nPypandoc uses pandoc, so it needs an available installation of pandoc. For some common cases (wheels, conda packages), pypandoc already includes pandoc (and pandoc-citeproc) in it’s prebuilt package.\n\n------------------------------\n----- Installing via Pip -----\n------------------------------\n\nInstall via pip:\n\n     pip install pypandoc\n\nPrebuilt wheels for Windows and Mac OS X include pandoc. If there is no prebuilt binary available, you have to install pandoc yourself.\n\nIf you use Linux and have your own wheelhouse, you can build a wheel which include pandoc with python setup.py download_pandoc; python setup.py bdist_wheel. Be aware that this works only on 64bit intel systems, as we only download it from the official releases.\n\n------------------------------\n---- Installing via Conda ----\n------------------------------\n\nPypandoc is included in conda-forge. The conda packages will also install the pandoc package, so pandoc is available in the installation.\n\nInstall via conda: \n\n     install -c conda-forge pypandoc\n\nYou can also add the channel to your conda config via conda config --add channels conda-forge. This makes it possible to use conda install pypandoc directly and also lets you update via conda update pypandoc.\n\nPress any key to exit the this message and halt the script.\n')
    quit()

###############################################################################

#os.chdir('/Users/dylandaniels/Documents/github-repos/hnn-tutorials')
parentdirectory=os.getcwd()

## get names of folders in working directory and save to 'y'. Save the number of folders to 'leny'.
#y=os.listdir()
y = [f.name for f in os.scandir(parentdirectory) if f.is_dir() and not f.name == '.ipynb_checkpoints' and not f.name == '.git' and not f.name == 'html-styling' and not f.name == 'images']  
leny=len(y)

## add names of folder to a string to prompt the user with options in the input code below
count=1
mystring="Select folder \n\n"
for e in y:
    mystring += str(count) + " = " + e + " \n" 
    count=count+1
mystring+="\nYour response: "

## prompt user to select folder, save folder chosen to 'subfolder'
shift = 0
while 1 > shift or leny < shift:
    try:
        shift = int(input(mystring))
    except ValueError:
        print('Try again')
subfolder = y[shift-1]

## join 'subfolder' to parent directory path
subfolder=os.path.join(parentdirectory,subfolder)

###############################################################################

## change directory to 'subfolder' as defined above
os.chdir(subfolder)

## save directory contents in list 'x' and save length of list in 'lenx'
x=[]
for file in os.listdir():
    if file.endswith(".md"):
        x+=[file]
    #if file.endswith(".html"):
        #x+=[file]
lenx = len(x)
print(x)

## add names of folder to a string to prompt the user with options in the input code below
count=1
mystring="Select file from the list below \n\n"
for e in x:
    mystring += str(count) + " = " + e + " \n" 
    count=count+1
mystring+="\nYour response: "

## prompt user to select file, save file chosen to 'subfile_og'
shift2 = 0
while 1 > shift2 or lenx < shift2:
    try:
        shift2 = int(input(mystring))
    except ValueError:
        print('Try again')
mdfile_og = x[shift2-1]
print('You chose: '+mdfile_og)

###############################################################################

## covert the chosen md file to html with pandoc
output = pypandoc.convert_file(mdfile_og, 'html', outputfile="body_only.html")

## get the filepath for the html header
headersubfolder='html-styling'
headerfile='page-setup.html'
htmlheader= os.path.join(parentdirectory,headersubfolder)
htmlheader=os.path.join(htmlheader,headerfile)

## get the filepath for the html body
htmlbody = os.path.join(subfolder, "body_only.html")

## define filenames
filenames = [htmlheader,htmlbody]

## strip filetype from filename, save filename to new var
output_fname = os.path.splitext(os.path.basename(mdfile_og))[0]
output_fname+=".html"

## write a new file 'output_fname' that combines html header and html body
with open(output_fname, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

## delete body_only.html
os.remove(htmlbody)

os.chdir(parentdirectory)
