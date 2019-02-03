class MainMenu:
    def __init__(self):
        self.user_key_phrase = None
        self.folder = None
    
    #This asks the user about input.
    def seek_input(self):    
        import utilities
        print(utilities.boxer.make_text_box("\n     STATISTIC FINDER     \n\n"))
        print("Tip: Use quotes for specific results!")
        user_input = input("Enter a keyword phrase: ")
        
        if user_input in ['Quit', 'quit', 'Exit', 'exit']:
            print(utilities.boxer.make_text_box("\n     Exiting...     \n\n"))
            from sys import exit
            exit(0)
        
        else:    
            print(utilities.boxer.make_text_box("\n         THANK YOU     \n     ONE MOMENT PLEASE     \n\n"))
            self.user_key_phrase = user_input
            return
        
    def generate_folder(self):
        from os import makedirs, getcwd
        from os.path import exists, dirname
        import datetime, utilities
        
        cwd = getcwd()
        
        self.folder = (cwd+"\\Generated Documents\\"+self.user_key_phrase.replace(" ", "_"))
        #This allows the user to use google's syntax to search for a specific term.
        #EX: I want my search results to include "cats"
        self.folder = self.folder.replace("\"","")
        filename = (cwd+"\\Generated Documents\\"+self.user_key_phrase.replace(" ", "_")+"\\Details.txt")
        #replaces any " in the file name.
        filename = filename.replace(r'"', '')
        
        if exists(filename):
            print(utilities.boxer.make_text_box("\n             ERROR     \n\n     FOLDER ALREADY EXISTS     \n\n"))
            from sys import exit
            exit(0)
            
        else:
            makedirs(dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                currentDT = datetime.datetime.now()
                year = str(currentDT.year)
                month = str(currentDT.month)
                day = str(currentDT.day)
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                
                f.write("This folder was created on {}\{}\{} at {}:{}.".format(month, day, year, hour, minute))
            

            f.close()
            print(utilities.boxer.make_text_box("\n     FOLDER GENERATED     \n\n"))
            return
        
    def run(self):
        import utilities, searcher, scraper
        self.seek_input()
        self.generate_folder()
        search = searcher.UrlGrabber(self.user_key_phrase)
        search.generate_url_list(self.folder)
        print(utilities.boxer.make_text_box("\n     URL LIST GENERATED     \n\n"))
        
        scrape = scraper.ScraperTool(search.output_file_id)
        
        scrape.scrape(self.folder)
        print(utilities.boxer.make_text_box("\n     EXITING PROGRAM     \n\n"))
        
        from sys import exit
        exit(0)

if __name__ == "__main__": 
    Researcher = MainMenu()
    Researcher.run()
    
    