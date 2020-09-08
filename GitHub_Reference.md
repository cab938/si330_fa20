## SI330 GitHub “Cheat Sheet”

We’ll be using git *extensively* throughout this course. Please familiarize yourself with some of the **basic commands** we’ll be using.

Once you’ve generated an assignment repo (from an invite link) and want to open it in JupyterLab, open a new terminal window (file → new → terminal), make sure you’re in the home directory, and then type:

`git clone [github repo url goes here]`

When you’re ready to submit (you MUST be in the directory of the assignment you’re working on):

`git add [filename/directory name to stage; if you want to commit everything just type . ]` (the `.` represents everything in the current directory)

`git commit -m “a place to put a memo or to describe changes made”` (it's a good habit to commit changes frequently and have descriptive messages!)

`git push origin master`

To get feedback files when grading is finished (you MUST be in the directory of the assignment of interest):

`git pull origin master`

**Other important command-line commands/notes:**

To delete a folder (useful if you come across issues and need to try again from scratch):

`rm -r [folder name]`

To check your present working directory (where you are currently at in the file system):

`ls`

To change into a different directory:

`cd [name of folder]`

To go up one level (i.e. if your in /name/Documents and want to go back to /name):

`cd ..`

For more details, please try searching for additional documentation first such as:

https://education.github.com/git-cheat-sheet-education.pdf

http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/unix_cheatsheet.html

and then ask us if you have further questions!