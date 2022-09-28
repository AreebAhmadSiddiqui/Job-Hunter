from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

class Naukri:

    def __init__(self):
        self.naukriJobList = []

    def extractNaukri(self,jobType):

        jobType=jobType.strip().replace(" ",'-')

        url = f"https://www.naukri.com/{jobType}-jobs-in-india" 

        driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"))
        driver.get(url)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        driver.close()

        return soup

    def transformNaukri(self, soup):
        jobCards = soup.find_all('article', class_='jobTuple bgWhite br4 mb-8')
        for item in jobCards:
            jobTitle = item.find('a').text.strip()
            jobLink = item.find('a')['href']
            companyName = item.find('div', class_='companyInfo').find(
                'a', class_='subTitle').text.strip()
            jobLocation = item.find('li', class_='location').text.strip()
            try:
                salary = item.find(
                    'li', class_='salary').text.strip()
               
            except:
                salary = ''
            JD = item.find(
                'div', class_='job-description').text.strip().replace('\n', '')
            jobs = {
                'Title': jobTitle,
                'Company Name': companyName,
                'Job Location': jobLocation,
                'Salary': salary,
                'Job Description': JD,
                'Job Link': jobLink
            }
            self.naukriJobList.append(jobs)
        return

    def getDataNaukri(self,jobType):
        
            c = self.extractNaukri(jobType)
            self.transformNaukri(c)
