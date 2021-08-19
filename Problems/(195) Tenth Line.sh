#Question Link
# https://leetcode.com/problems/tenth-line/

#Descrpytion
# Given a text file file.txt, print just the 10th line of the file.

count=0
filename=file.txt
IFS=$'\n'


for line in $(cat $filename);
do
    let count=count+1
    if [[ count -eq 10 ]] ; then
        echo $line
    fi

done