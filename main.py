import requests
import selectorlib
from send_email import sendemail
import sqlite3
import time

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# get url
URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
"""
# INSERT INTO events VALUES("Monkeys","MonkeyCITY","2024.10.22")
#SELECT *FROM events WHERE date='2024.10.22'
#DELETE FROM events WHERE band='Monkeys'

"""


# get the source
def scrape(url):
    """Scrape the source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


# extra value from website
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    value = extractor.extract(source)["tours"]
    return value


# send email if value extracted not in db


def store(extracted_list_tuple):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO events VALUES {extracted_list_tuple}")
    # extracted_list = [item.strip() for item in extracted]
    # band, city, date = extracted_list
    # cursor.execute("INSERT INTO events VALUES WHERE band=? AND citi=? AND  date=?", (band, city, date))
    connection.commit()

    #connection.close()
    # with open('data.txt', "a") as file:
    #     file.write(extracted + "\n")


def read():
    # with open('data.txt', 'r') as data_list:
    #     data_list = data_list.read()
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events ")
    result = cursor.fetchall()
    connection.close()
    return result


# store in database


if __name__ == '__main__':

    while True:
        source = scrape(URL)
        extrated = extract(source)
        print(extrated)
        # extracted_list = extrated.split(", ")
        # extracted_list = tuple(extracted_list)
        # print(extracted_list)
        if extrated != "No upcoming tours":
            content_data = read()
            print(content_data)
            extracted_list_tuple = tuple(extrated.split(", "))
            print(extracted_list_tuple)
            if extracted_list_tuple not in content_data:
                store(extracted_list_tuple)
                x = f"{content_data} '\n'{extrated} "
                print("email send")
                sendemail(x)
        time.sleep(5)
