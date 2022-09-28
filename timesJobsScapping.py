from bs4 import BeautifulSoup
import pandas as pd
# from urllib.request import Request, urlopen
import requests

class TimesJobs:
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        self.timesjobsJobList=[]

    def extractTimesjobs(self,jobType):
        url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={jobType}&txtLocation=India'
        
        res=requests.get(url)
        soup=BeautifulSoup(res.content, 'lxml')
        return soup
    
    def transformTimesjobs(self,soup):
        jobCards = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        for item in jobCards:
            jobTitle = item.find('h2').text.strip()
            jobLink = item.find('a')['href']
            companyName = item.find('h3', class_='joblist-comp-name').text.strip()
            jobLocation = item.find('span').text.strip()

            salary = 'Not Disclosed'
            JD = item.find('ul', class_='list-job-dtl clearfix').find('li').text.strip()[:-12]

            jobs = {
            'Title': jobTitle,
            'Company Name': companyName,
            'Job Location': jobLocation,
            'Salary': salary,
            'Job Description': JD,
            'Job Link': jobLink
            }
            self.timesjobsJobList.append(jobs)
        return

    def getDataTimesjobs(self,jobType):
        
            soup = self.extractTimesjobs(jobType)
            self.transformTimesjobs(soup)