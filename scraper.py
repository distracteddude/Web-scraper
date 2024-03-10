from bs4 import BeautifulSoup
import requests
import time
print("Put some skills that you are not familiar with (type exit when you are done): ")

unfamiliarSkillsString = ""

while True:
    unfamiliarSkills = input('>> ')
    
    if unfamiliarSkills == "exit":
        break
    
    else:
        # Add a comma only if unfamiliarSkillsString is not empty
        if unfamiliarSkillsString:
            unfamiliarSkillsString += ','
        unfamiliarSkillsString += unfamiliarSkills

def find_jobs():
    base_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation="

    response = requests.get(base_url).text

    soup = BeautifulSoup(response, 'lxml')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:

        published_date = job.find('span', class_ = 'sim-posted').span.text.replace(' ', '')

        if published_date == "Postedfewdaysago":

            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')

            skills = job.find('span', class_ = 'srp-skills').text.replace(" ", "")

            skills_l = list(job.find('span', class_ = 'srp-skills').text.replace(" ", "").split(','))

            skills_list = [item.strip() for item in skills_l]

            more_info = job.header.h2.a['href']

            if any(string in unfamiliarSkillsString for string in skills_list) == False:
                with open("get_job_info", "w") as f:

                    f.write(f"Company Name: {company_name}".strip())
                    f.write(f"Skills: {skills.strip()}")
                    f.write(f"More Info: {more_info}")
                    f.write("\n")

find_jobs()