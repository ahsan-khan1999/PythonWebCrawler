import requests
from bs4 import BeautifulSoup
value = True
while(value == True):
    word = input("Enter a word If Multi Word Than enter With '_': ")
    
    url = 'https://www.lexico.com/en/definition/' + "" +word
    data =  requests.get(url,word).text
    try:
        soupObject = BeautifulSoup(data,'lxml')
        get = soupObject.find('section',class_='gramb')
        meaning =  get.ul.li.div.p.find('span', class_='ind').text
        
        print(meaning)
        print("This word and its definition is saved automatically in permenent storage")
        with open('dictionary.tsv','a',newline='') as dic:
            dic.write(word + " : " + meaning)
    except:
        print("Sorry Word Not Found Try Again")
    finally:
        ques = input("For Another Word C to Continue Q for Quit : ")
        if(ques == 'c' or ques == 'C'):
            value = True
        else:
            value = False 


    



# print(get)
    # soup = BeautifulSoup(data,'html.parser')
    # for each_text in soup.find_all('div',{"class" : "entry-content"}):
    #     content = each_text.text
    #     print(content)

        # meaning = get.div.ul.li.find('li')

# "class" : "entry-content"}):
#     #     content = each_text.text
        # meaning = get.div.ul.li.find('li')
        
# "class" : "entry-content"}):
        # content = each_text.text




# print(get)
    # soup = BeautifulSoup(dat



# url = 'https://www.dictionary.com/list/0'
# data = requests.get(url).content


# soup = BeautifulSoup(data,'html.parser')
# read = soup.find('div')
# # print(read)
# # for r in read :
# mylist = [] 
# mylist = read.main.ul.li.find('a')
# print(mylist)

# words = read.section('div' , class_="css-7ac8yh e16867sm0")


# value = 1
# while(value ==1):
#     # word = input("Entpython dictionary.puer A Word")
#     source = requests.get('https://www.dictionary.com/list/0').text
#     # print(source)
#     soup = BeautifulSoup(source.title,'html.parser')
#     print(soup.find('ul'))

#     # try:
#     #     soup=BeautifulSoup(source,'html.parser')
#     #     get = soup.findChildren('section',class_= 'css-0 exfcwu50')
        
    #     print(get)

    # except:
    #     print("No url Found") 
    #     break  