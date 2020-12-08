# GAM-Tools

These two files I used pretty often to help me find information about our chromebooks to use in comparison with GAM. 

find-serial.py is pretty self explanatory from it's name. It takes two csv files and compares the two, and fills in the neccessary serial numbers for one of the spreadsheets. Basically, one csv is an exported out list of all of our inventory assets with the tags and serial numbers linked. The other spreadsheet is usually just made up of asset tag numbers. For example, we have spreadsheets of students who have chromebooks, but it only has the asset number of the device they have, not the serial number as the asset number is a scannable tag. The serial number would be tedious to get off each device when you're handing them out to hundreds of kids, and our secretary's swap out chromebooks to kids with defective devices, and all they right down is the asset number. So this script is very helpful in quickly filling in the blanks for me, given the serial number is actually a) in our inventory, and b) the correct serial number.

GAM-info.py uses the structure and algorithm I made for find-serial.py but instead can be used for a few different things. The main use is to pull the unqiue device-id only found in G Suite for each device that GAM likes to use for a lot of its utilities. I've found from reading around that querying the serial numbers of each device when trying to move/edit devices with GAM causes some problems with quotas, and is a much more smooth operation if you use the device-id instead. So this script finds that info for us. It takes a csv of all our G Suite devices exported out via GAM and a csv that has serial numbers of each device (aka usually from using find-serial.py) and tacks on the device-id to each serial number on a new csv.

Mainly putting these up just as a backup of my work. I intially used the main structure of these scripts in another script I wrote in a quick bind to help solve some issues we were having with SIS info not lining up correctly. Instead of our student data person running through two differnet spreadsheets, line by line, checking 4000+ lines for errors between the two, I used python to quickly compare them. I know my use of the csv library is a bit scuffed and not fully utilized, and there's soem unused lines and coutners carried over from other versions of boths scripts. However, it gets the job done and I think it's pretty great for my limited pool of python knowledge. I plan on diving deeper into python and down the road maybe I'll come back to these and fix them up to utilize the csv library fully.
