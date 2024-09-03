from flask import Flask, jsonify #to make an API end-point
import requests # to fetch html content 
import re # to parse the html text (python's in-built library for string manipulation)

app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    target_url = 'https://time.com'
    
    response = requests.get(url=target_url)
    html = response.text

    stories_pattern = re.compile(r'<div class="partial latest-stories".*?<ul>(.*?)</ul>', re.DOTALL)
    item_pattern = re.compile(r'<li class="latest-stories__item">.*?<a href="(.*?)">.*?<h3 class="latest-stories__item-headline">(.*?)</h3>', re.DOTALL)

    stories_section = stories_pattern.search(html)
    output = []
    if stories_section:
        stories_html = stories_section.group(1)
        items = item_pattern.findall(stories_html)
        
        for link, title in items[:6]:
            content = {
                'title': title.strip(),
                'link': target_url + link.strip()
            }
            output.append(content)
    else:
        return jsonify([])
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
