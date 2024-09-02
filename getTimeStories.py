from flask import Flask, jsonify # for generating the API and the json object 
import requests # importing request for making http request
from bs4 import BeautifulSoup # for parsing the html

app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    target_url = 'https://time.com'
    
    data = requests.get(url=target_url)
    soup = BeautifulSoup(data.text, 'lxml')
    
    stories_section = soup.find('div', class_='partial latest-stories')
    stories = stories_section.find_all('li')
    
    output = []
    for i in stories[:6]:
        contents = {
            'title': i.find('h3').text,
            'link': target_url + i.find('a')['href']
        }
        output.append(contents)
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
