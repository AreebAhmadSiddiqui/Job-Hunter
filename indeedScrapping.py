from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
from requests_html import HTMLSession

class Indeed:
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
        self.indeedJobList=[]

    def extractIndeed(self,jobType):

        jobType=jobType.strip().replace(" ",'%20')
        url = f'https://in.indeed.com/jobs?q={jobType}&l=India'
        
        # print(url)
        # content = Request(url, headers=self.header)
        # page = urlopen(content).read()
        # soup = BeautifulSoup(page, 'lxml')

        session=HTMLSession()

        soup=session.get(url)
        print(soup)
        return soup
    
    def transformIndeed(self,soup):
        jobCards = soup.find_all('div', class_='cardOutline')
        for item in jobCards:
            jobTitle = item.find('a').text.strip()
            jobLink = 'https://in.indeed.com'+item.find('a')['href']
            companyName = item.find('span', class_='companyName').text.strip()
            jobLocation = item.find('div', class_='companyLocation').text.strip()

            try:
                salary = item.find(
                    'div', class_='salary-snippet-container').text.strip()
            except:
                salary = 'Not Disclosed'
            JD = item.find('div', class_='job-snippet').text.strip().replace('\n', '')
            jobs = {
            'Title': jobTitle,
            'Company Name': companyName,
            'Job Location': jobLocation,
            'Salary': salary,
            'Job Description': JD,
            'Job Link': jobLink
            }
            
            self.indeedJobList.append(jobs)
        return

    def getDataIndeed(self,jobType):
        
            soup = self.extractIndeed(jobType)
            self.transformIndeed(soup)

            print(self.indeedJobList)

obj=Indeed()

job = input("Enter The Job Type You Are looking for: ")
obj.getDataIndeed(job)