#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      danny
#
# Created:     08/06/2023
# Copyright:   (c) danny 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from pathlib import Path
import shutil
import time
import os

def copyFromTo(fromFile,toFile):
    print ("From: "+fromFile.name)

    for path in Path(toFile+"\\").glob("**/*"):
        if(path.is_dir()):
            print(path)
            if(path.name.split('(')[1].split(')')[0] == fromFile.name.split('.')[0]):
                shutil.copyfile(sys.argv[1]+"\\"+fromFile.name, path.__str__()+"\\"+fromFile.name)
                os.remove(sys.argv[1]+"\\"+fromFile.name)



def getCustomerNumber(fileName):
    flag = False
    customerNumber = ""
    counter=0
    counterMax=20

    for page_layout in extract_pages(fileName):
        if(counter == counterMax):
            break
        if(flag == True):
            break
        for element in page_layout:
            if(counter == counterMax):
                break
            counter = counter+1
            if isinstance(element, LTTextContainer):
                if(flag == True):
                    customerNumber =element.get_text()
                    break
                elif(element.get_text() == "CUSTOMER NO.\n"):
                    flag = True



    customerNumber =customerNumber.rstrip()
    return customerNumber

def main(pdfPath):

    while(True):
        #iterate through all files in directory
        root=None
        if(pdfPath!=None):
            root=pdfPath
        else:
            root = "C:\\Users\\danny\\Documents"  # take the current directory as root

        for path in Path(root).glob("**/*.pdf"):
            if(getCustomerNumber(path)!= ""): # if customer # is found
                copyFromTo(path,sys.argv[2])
        time.sleep(6)


if __name__ == '__main__':
    main(sys.argv[1])

