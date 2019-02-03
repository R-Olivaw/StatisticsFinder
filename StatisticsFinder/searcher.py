   
#To use: Generate a new instance of this class with a single, string attribute.
##This string will be the text that selenium inputs into the Google Search bar.
###To run, apply the generate_url_list() method to your instance.    
class UrlGrabber():
    
    #Search_input must be a string!
    def __init__(self, search_input):
        #This is the search text
        self. search_input = search_input
        #This will become the html source that BS will parse.
        self.page_source = None
        self.output_file_id = None
        
    def define_page_source(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.keys import Keys
        
        #This is the webdriver that selenium uses to conduct a search.
        browser = webdriver.Chrome(r'C:\Users\Alexa\Dropbox\Python Projects\chromedriver.exe')
        #This is where we will search.
        browser.get('http://www.google.com')

        #This block actually types and runs the search.
        search = browser.find_element_by_name('q')
        search.send_keys(self.search_input)
        search.send_keys(Keys.RETURN)
        
        #Finally, we assign the gathered html as our source.
        self.page_source = browser.page_source
        
    def generate_url_list(self, folder):
        #Runs the function to grab the appropriate html source.
        self.define_page_source()
        import os
        from bs4 import BeautifulSoup as bs
        
        #Generates a new text file with the search_input as the name.
        file_name = (folder+"\\"+self.search_input.replace(" ", "_")+"_URLS.txt")
        #replaces any " in the file name.
        file_name = file_name.replace(r'"', '')
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        f = open((file_name),'w')
        
        #Finds the appropriate links in the google html.
        soup = bs(self.page_source, 'html.parser')
        main_window = soup.find_all(class_='r')
        
        #Gets rid of unnecessary pieces and prints the urls to txt file.
        for item in main_window:
            try:
                if item.contents[0]:
                    new_soup = item.contents[0]
                link = new_soup.get('href')
                if isinstance(link, str):
                    f.write('\n'+ link + '\n')
            except:
                pass
        
        f.close()
        
        #Removes blank lines in the txt file.
        f = open((file_name), 'r+')
        d = f.readlines()
        f.seek(0)
        for i in d:
            if not i.startswith('/') and i != '\n':
                f.write(i)
        f.truncate()
        f.close()
        
        self.output_file_id = file_name
            
'''
EXAMPLE
new_search = UrlGrabber('travel management rfp')
new_search.generate_url_list()
'''