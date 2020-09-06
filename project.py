
import urllib.request as urllib2
import pandas as pd
from datetime import datetime,date
import logging
class Project:
    
    def downloadData(self,url):
        x = urllib2.urlopen(url)
        return x

    def processData(self,data):
        df=pd.read_csv(data)
        dict={}
        for index, row in df.iterrows():
            try:
                row['birthday'] = datetime.strptime(row['birthday'], "%d/%m/%Y")
                dict[row['id']] = (row['name'], row['birthday'])
               
            except:
                logger=logging.getLogger('assignment2')
                logging.basicConfig(filename='error.log', filemode='w', format='%(levelname)s - %(message)s')
                logging.error("Error processing line "+ str(index)+" for ID: "+str(row.id))


        return dict
       


    def displayPerson(self,userid,personData):
        num=0
        
        for key,value in personData.items():
            if(key==userid):
                num=key
                break
                
            else:
                num=0
                
        
        if(num!=0):
            print("Person "+ str(num)+ " is ",value[0], " with a birthday of ", value[1])
        else:
            print( 'No user found with that id')
        



    
    



        
            
       
        




def main():
    p = Project()
    x=p.downloadData('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
    personData=p.processData(x)
    id=int(input('Please enter id '))
    if(id<=0):
        exit
    else:
        p.displayPerson(id,personData)
       

    

   
    


if __name__ == "__main__":
    main()
