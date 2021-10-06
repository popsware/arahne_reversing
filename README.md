# README #
### What is this repository for? ###

* Reverse Engineering Arahne Weave files

### Inspiration ###

I have been trying to manupilate the used files for too long now, and this is my first attempt that shows a good potential.

I have learned Python throuhg my latest project CCTV_MOTION_TRACKING and i 
am trying to used my latest experience into this project.

Reverse Engineering is a process that takes a whole lot of time. i normally go on and off into this project. I have very slight knowledge on reverse engineering. But i think now i have the appropriate amount of info to give it a real try.

### About Arahne Weave ###

Arahne Weave is a Sweden software that allow designers to convert thier weave designs into files that can easily be read by weaving machinery. The process of exporting the files takes too long to build, so im tryiung to find a way to automate some changes in the exported files.

This project is not meant as a way to overcome the software license or so. I highly encourage users to buy the license. However, i am trying to build a way to automate processes to make this process much faster.


### What knowledge i have on reverse engineering ###

* machine files are binary files
* i am trying to understand the files through exporting many files and testing them
* i am using this project to manupilate the files and try to display thier info in a slightly more friendly way
* the whole process depends on exporting multiple files and comparing them in order to find a pattern

### Trickiest challenges that hazed me ###

* the files had a number of prefix of bytes in the begining of the file that had to be eliminated from the pattern search
* the length of the pattern line was hte greatest issue. whether there is actually a constant size per line


### Message to the reader ###

This is my message when i succeed (I hope so)


### Reversind Process ###

1. To detect machine pattern
    - choose the machine you want to operate on
    - create a section with the machine name in `config_machine.ini`
    - set the machine name in `parseFiles.bat` file as the first arg
    - export two files from Arahne weave for the same design
    - use files with different selvages (preferebly white and black)
    - set the file names in `parseFiles.bat` as the second arg
    - use `parseFiles.bat` to run `readFile.py` on both files
    - compare the decimal exported files to detect the number of common prefix bytes between the two
    - set the prefix bytes by changing `prefix_values` in the `config_machine.ini`
    - rerun the `parseFiles.bat` script on both to generate new files with a separated prefix lines for both
    - compare the two binary files with WinMerge to detect the line length (line length may be concluded from the Arahne Weave Software)
    - change line length dynamically by changing `values_per_line` in the `config_machine.ini` in order to reach the exact line size
    - you now have the machine config all set up 
2. Plot the Exported File
    - use `plotFile.py` to plot the exported binary file

### External Tools Used ###

* WinMerge
* VSCode

