import urllib2, sys
from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

#Oh boy, I can't wait for this code to collapse on itself and cause a python singularity
f = open('reviews.txt','r+')

    

companyname = raw_input("Please enter company name: ")
companyname = companyname .strip("\n");
req = urllib2.Request("https://www.google.com/search?q=" + companyname + "%20glassdoor%20reviews&rct=j",
                          headers={"User-Agent" : "Magic Browser"})
con = urllib2.urlopen(req)
webContent = con.read()
appendStartIndex = webContent.find ("https://www.glassdoor.com/Reviews/")
appendEndIndex = webContent.find(".htm")
url = webContent[appendStartIndex: appendEndIndex]
url2 = url + ".htm" 



#url = raw_input("Please enter the URL of the website you want to scrape reviews from: ")
site = url2
hdr = {"User-Agent":"Magic Browser"}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
webpage = page.read()
webpage1 = webpage
startindex = webpage1.find ("<p class=' tightBot '>")
yearsworked = webpage1.find ("<p class=' pros noMargVert truncateThis wrapToggleStr'>")
pros = webpage1.find ("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")
cons = webpage1.find ("</p> <p class=' cons noMargVert truncateThis wrapToggleStr'>") 

while startindex!=-1:


    
    startindex += 22;
    yearsworked += 54;
    cons += 59;

    webpage1 = webpage1[startindex:]
    yearsworked = webpage1[yearsworked:]
    endindex = webpage1.find ("</p> <div class='description")

    if endindex != -1:
        review1 = webpage1[0:endindex]
        review1 = review1.replace("&nbsp","");
        review1 = review1.replace("</p> </div> </div> <div class='row'> <div class='cell top '> <p class=\"strong tightVert\">Advice to Management</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>","")
        
        #print review1
    startindex = webpage1.find ("<p class=' tightBot '>")
    yearsworked = webpage1.find ("<p class=' pros noMargVert truncateThis wrapToggleStr'>")



pros = 0
startindex = 0
webpage1= webpage
while startindex !=-1:
    pros = webpage1.find ("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")
    startindex += len("<p class=' tightBot '>")
    pros += len("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")
    webpage1 = webpage1[pros:]
    
    
    endindexpros = webpage1.find("</p> </div> </div> <div class='row padBotLg'> <div class='cell top '> <p class=\"strong tightVert\">")

    if endindexpros != -1:
        review2 = webpage1[0:endindexpros]
        review2 = review2.replace("#","");
        review2 = review2.replace("&","");
        review2 = review2.replace("<br/>","");
        review2 = review2.replace("039;","");
        review2 = review2.replace("</p> </div> </div> <div class='row'> <div class='cell top '> <p class=\"strong tightVert\">Advice to Management</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>","")
        #print review2
    startindex = webpage1.find ("<p class=' tightBot '>")
    pros = webpage1.find ("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")


    
cons = 0
startindex = 0
webpage1 = webpage
while startindex !=-1:
    cons = webpage1.find ("</p> <p class=' cons noMargVert truncateThis wrapToggleStr'>")
    startindex += len("<p class=' tightBot '>")
    cons += len("</p> <p class=' cons noMargVert truncateThis wrapToggleStr'>")
    webpage1 = webpage1[cons:]

    endindexcons = webpage1.find("</p> </div> </div>")
    if endindexcons != -1:
        review3 = webpage1[0:endindexcons]
        review3 = review3.replace("<br/>","");
        review3 = review3.replace("&#034","");
        review3 = review3.replace("&#039;","");
        review3 = review3.replace("</p> </div> </div> <div class='row'> <div class='cell top '> <p class=\"strong tightVert\">Advice to Management</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>","")
    #print review3
    startindex = webpage1.find ("<p class=' tightBot '>")
    cons = webpage1.find ("</p <p class=' cons nomargVert truncateThis wrapToggleStr'>")

letstrythis = 0
for i in range(0,5000):      # Number of pages plus one
    #companyname = raw_input("Please enter company name: ")

    while i !=-1:
        
        companyname = companyname.strip("\n");
        req = urllib2.Request("https://www.google.com/search?q=" + companyname + "%20glassdoor%20reviews&rct=j",
                              headers={"User-Agent" : "Magic Browser"})
        con = urllib2.urlopen(req)
        webContent = con.read()
        appendStartIndex = webContent.find ("https://www.glassdoor.com/Reviews/")
        appendEndIndex = webContent.find(".htm")
        more_pages = "_P" 
        url = webContent[appendStartIndex: appendEndIndex:]
        url2 = url + more_pages + ".htm" 
        more_pages = "_P"
        letstrythis += 1
        yep = ".htm"
        url3 = url + more_pages + str(letstrythis) + yep
        req = urllib2.Request(url3,
                              headers={"User-Agent" : "Magic Browser"})
        con = urllib2.urlopen(req)
        webContent = con.read()
        #r = requests.get(url3)
        #soup = BeautifulSoup(url3, 'html.parser')
        #print url3
        

        startindex = webContent.find ("<p class=' tightBot '>")
        yearsworked = webContent.find ("<p class=' pros noMargVert truncateThis wrapToggleStr'>")
        pros = webContent.find ("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")
        cons = webContent.find ("</p> <p class=' cons noMargVert truncateThis wrapToggleStr'>") 

        while startindex!=-1:


            
            startindex += 22;
            yearsworked += 54;
            cons += 59;

            webContent = webContent[startindex:]
            yearsworked = webContent[yearsworked:]
            endindex = webContent.find ("</p> <div class='description")

            if endindex != -1:
                
                review1 = webContent[0:endindex]
                review1 = review1.replace("&nbsp","");
                
                print review1
            startindex = webContent.find ("<p class=' tightBot '>")
            yearsworked = webContent.find ("<p class=' pros noMargVert truncateThis wrapToggleStr'>")
            for line in f:
                f.write(review1)
            #f.close()


        pros = 0
        startindex = 0
        #webContent = webpage1
        while startindex !=-1:
            pros = webContent.find ("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")
            startindex += len("<p class=' tightBot '>")
            pros += len("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")
            webContent = webContent[pros:]
            
            
            endindexpros = webContent.find("</p> </div> </div> <div class='row padBotLg'> <div class='cell top '> <p class=\"strong tightVert\">")

            if endindexpros != -1:
                review2 = webContent[0:endindexpros]
                review2 = review2.replace("#","");
                review2 = review2.replace("&","");
                review2 = review2.replace("<br/>","");
                review2 = review2.replace("039;","");
                review2 = review2.replace("</p> </div> </div> <div class='row'> <div class='cell top '> <p class=\"strong tightVert\">Advice to Management</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>","")
                print review2
            startindex = webContent.find ("<p class=' tightBot '>")
            pros = webContent.find ("</p> <p class=' pros noMargVert truncateThis wrapToggleStr'>")
            for line in f:
                f.write(review2)
            #f.close()

            
        cons = 0
        startindex = 0
        #webContent = webpage
        while startindex !=-1:
            cons = webContent.find ("</p> <p class=' cons noMargVert truncateThis wrapToggleStr'>")
            startindex += len("<p class=' tightBot '>")
            cons += len("</p> <p class=' cons noMargVert truncateThis wrapToggleStr'>")
            webContent = webContent[cons:]

            endindexcons = webContent.find("</p> </div> </div> </div> <div class='tbl fill outlookEmpReview'>")
            if endindexcons != -1:
                review3 = webContent[0:endindexcons]
                review3 = review3.replace("<br/>","");
                review3 = review3.replace("&#034","");
                review3 = review3.replace("&#039;","");
                review3 = review3.replace("</div> </div> </div>","")
                review3 = review3.replace("</div> </div>","")
                review3 = review3.replace("<div> <div>","")
                review3 = review3.replace("</div> </div> </div> </div>","")
                review3 = review3.replace("</p>  <div class='row'> <div class='cell top '> <p class=\"strong tightVert\">Advice to Management</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>","")
            print review3
            startindex = webContent.find ("<p class=' tightBot '>")
            cons = webContent.find ("</p <p class=' cons nomargVert truncateThis wrapToggleStr'>")
            for line in f:
                f.write(review3)
            #f.close()

                                  

        """mgmt = 0
        startindex = 0
        while startindex !=-1:
            mgmt = webContent.find ("</p> </div> </div> <div")
            startindex += len("<p class=' tightBot '>")
            mgmt += len("</p> </div> </div> <div class='row'> <div class='cell top '> <p class='strong tightVert'>")
            webContent = webContent[mgmt:]
            review4 = ""               
            endindexmgmt = webContent.find("</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>")
            if endindexmgmt != -1:
                review4 = webContent[0:endindexmgmt]
                review4 = review4.replace("</p> </div> </div> <div class='row'>", "")
                review4 = review4.replace("</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>","")
                review4 = review4.replace("</div> </div> </div>","")
                review4 = review4.replace("</div> </div>","")
                review4 = review4.replace("<div> <div>","")
                review4 = review4.replace("</div> </div> </div> </div>","")
                review4 = review4.replace("</p>  <div class='row'> <div class='cell top '> <p class=\"strong tightVert\">Advice to Management</p> <p class=' adviceMgmt noMargVert truncateThis wrapToggleStr'>","")
            print review4
            startindex = webContent.find ("<p class=' tightBot '>")
            mgmt = webContent.find ("</p> </div> </div> <div class='row'> <div class='cell top '> <p class='strong tightVert'>")
            if letstrythis > 0:
                    continue
                    while letstrythis !=-1:
                        continue"""


        
            
