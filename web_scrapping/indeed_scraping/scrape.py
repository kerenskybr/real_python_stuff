import requests
from bs4 import BeautifulSoup

url = "https://br.indeed.com/empregos?q=python&l=Brasil"

response = requests.get(url)

soup = BeautifulSoup(response.content)

# Finding the 'loop for' column whose have all the info
# we are looking for
results = soup.find(id='resultsCol')

# Here class could be only one from the list (which is separate by space)
# <div class="jobsearch-SerpJobCard unifiedRow row result" 
# and class should have a underscore, cause class is a python
#reserved word
jobs = results.find_all('div', class_='result')
#print(len(jobs))
#print(jobs[0].title)
title = jobs[1].find('h2')
#print(title)
remote = jobs[1].find_all('span', class_='remote')
#print(remote[0].text)  

title_link = title.find('a')
#print(title_link)

link_text = title_link.text
#print(link_text.strip())

# All job titles
job_titles = [job.find('h2').find('a').text.strip() for job in jobs]
#print(job_titles)

# Getting the link from each job
#print(title_link)
#print(title_link['href'])

base_url = 'https://br.indeed.com'
job_url = base_url + title_link['href']
#print(job_url)

for i in jobs:
    print("Title: ", i.find('h2').text.strip())
    try:
        print("Company: ", i.find('span', class_='company').text.strip())
    except:
        print("Company: Nothing")
    try:
        print("Home office: ", i.find('span', class_='remote').text.strip())
    except:
        print("Home office: No")
    try:
        print("Salary: ", i.find('span', class_='salaryText').text.strip())
    except:
        print("Salary: ---------")
    print("*"*20)