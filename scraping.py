# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:34:23 2019

@author: wyeth
"""
# Scraping WJE PDFs 
import PyPDF2
import os
folder = "D:\Job Scrape\WJE_SF"
filenames = os.listdir(folder)

substring = 'Philosophy' #specify string to search for
count = 0 #initialize count for what I want to find
for i in filenames:
    # print(i)
    endpoint = '\\' + i
    pdfFileObj = open(folder + endpoint, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    
    a = pageObj.extractText()
    result = a.find(substring)
    print'For Employee', i
    print "Substring -", substring, "- found at index:", result 
    if result > 0:
        count = count++1
    

print count
print "Substring -", substring, "- found for", count, "employees"

