from bs4 import BeautifulSoup 
import requests

# currency codes 
def get_currency(in_currency, out_currency):
    
    # pass in the currency in the link 
    # og link https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1.32
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    
    content = requests.get(url).text # get the content 
    # print(content)

    soup = BeautifulSoup(content, "html.parser")
    # print(soup) similiar output to printing the content but more specific object 


    currencyOut = soup.find("span", class_="ccOutputRslt")

    # now only want to extract the final output from the html element 
    currencyOut = currencyOut.get_text()

    # return currency rate as a string with the output name 
    # we want only the value 

    currencyOut = float(currencyOut[:-4]) # remove last 4 characters and casted to float 

    return currencyOut


def main():

    in_curr = input("Enter input Currency: \n")
    out_curr = input("Enter output Currency: \n")

    currencyOutput = get_currency(in_curr, out_curr)
    print(currencyOutput)








main()
