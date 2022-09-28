import naukriScrapping
import indeedScrapping
import pandas as pd
from datetime import datetime
import schedule
import time
from emailNotification import *
import timesJobsScapping


class Main:

    def convertToCSV(self,jobList,email):
        
        time = datetime.now().strftime("%H-%M-%S")
        
        df = pd.DataFrame(jobList)
        
        file_name = 'Job-Data({}).csv'.format(time)
        
        df.to_csv(file_name, index=False)

        email_alert("New Job Postings", 'Kindly find the attached CSV files to get the details',
                    f'{email}', time)

    def getData(self,jobType,email):

        objNaukri = naukriScrapping.Naukri()
        objNaukri.getDataNaukri(jobType)

        objTimesJobs = timesJobsScapping.TimesJobs()
        objTimesJobs.getDataTimesjobs(jobType)

      
        naukriJobList = objNaukri.naukriJobList
        timesjobsJobList = objTimesJobs.timesjobsJobList

        jobList = naukriJobList+timesjobsJobList

        self.convertToCSV(jobList,email)


if __name__ == '__main__':

    mainObj=Main()
    
    jobType = input("Enter The Job Type You Are looking for: ")
    emailId = input('Enter The Email Id: ')

    schedule.every(30).seconds.do(mainObj.getData,jobType,emailId)

    while True:
        schedule.run_pending()
        time.sleep(1)
