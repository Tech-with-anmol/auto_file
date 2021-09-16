import os

def __docs__(self):
    """THIS is a libray used for creating all required filrs for making liabrary also for creating normal files"""
    pass

def mklib(dict_name):
        
    """make all folder and files required to make a library"""
    os.mkdir(dict_name)
            
    open("ReadMe.md", "x")
    with open("ReadMe.md", "w") as f :
        f.write("## add readme here")
        
    open("git.gitignore", "x")
    with open("git.gitignore", "w") as git:
        git.write("# all folder you not want to upload will be here")
            
    open("setup.py", "x")
    with open("setup.py", "w") as f :
        f.write("import setuptools \n\nsetuptools.setup( \n    name="", \n    version="",\n )")
                
    open("LICENSE", "x")
    with open("LICENSE", "w") as f :
        f.write("MIT License \n\nCopyright (c) 2021 YOUR_NAME\n\nPermission is hereby granted, free of charge, to any person \nobtaining a copy of this software and associated documentation files (the Software), \nto deal in the Software without restriction, including without limitation\nthe rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, \nand to permit persons to whom the Software is furnished to do so, subject to the following conditions: \nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
                
    os.chdir(dict_name)
    try:
        open("__init__.py", "x")
        open("functions.py", "x")
    except Exception as e:
        print(e)
        raise FileExistsError






    