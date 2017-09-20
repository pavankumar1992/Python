from urllib.request import  urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
table = page_soup.findAll("tbody",{"class":"lister-list"})

filename = ("IMDB.csv")
f = open(filename,"w")
headers = "Title, Year, Rank, Rating\n"
f.write(headers)

for table_loop in table:
    tr_tag = table_loop.find_all("tr")

    for tr_loop in tr_tag:
        details = tr_loop.findAll("td",{"class":"titleColumn"})
        title_name = details[0].a.text.replace(",",".")
        year = details[0].span.text.replace("(","").replace(")","").strip()
        rank = details[0].div.text.split('(')[0].strip()

        details_2 = tr_loop.findAll("td",{"class":"ratingColumn imdbRating"})
        rating = details_2[0].text.strip()
        #print(details)
        #print(title_name)
        #print(year)
        #print(rank)
        #print(rating)

        f.write(title_name + "," + year + "," + rank + "," + rating +"\n")
f.close()

