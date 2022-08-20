# importing libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

# parameters
wait_time = random.uniform(1.5, 3.0)
url_linkedin = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'
output_file = 'selenium linkedin output.txt'

# code
if __name__ == '__main__':
    
    # starting the webdriver and going to the specified url
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get( url_linkedin )
    
    #getting the list of jobs that will be collected
    jobs_list = driver.find_elements(By.CLASS_NAME, 'base-card')
    
    # creating a list and adding each job description to it
    description_list = []
    for c in jobs_list:
        time.sleep( wait_time )
        c.click()
        time.sleep( wait_time )
        description_path = '/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/div'
        description_element = driver.find_element(By.XPATH, description_path)
        description_list.append( description_element.text )
    
    # closing driver
    driver.quit()
    
    # saving results to output file
    to_save = '\n######################################################\n'.join( description_list )
    with open( output_file , 'w' , encoding='utf-8' ) as f:
        f.write( to_save )