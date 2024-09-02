<h1>Time Stories API</h1>
<p>This is a Flask-based application that fetches and serves the latest 6 highlighted stories from Time.com. The application exposes a custom API endpoint to access these stories in JSON format.</p>

<h2>Libraries and Requirements</h2>
<p>To run this application, you need the following Python libraries:</p>
<ul>
    <li><strong>Flask</strong>: A lightweight web framework for Python.</li>
    <li><strong>requests</strong>: For making HTTP requests to fetch the web page content.</li>
    <li><strong>beautifulsoup4</strong>: For parsing HTML content.</li>
    <li><strong>lxml</strong>: An HTML/XML parser (optional but recommended for BeautifulSoup).</li>
</ul>

<h3>Installing Required Libraries</h3>
<p>You can install the required libraries using pip. Run the following command:</p>
<pre><code>pip install Flask requests beautifulsoup4 lxml</code></pre>

<h2>Applications Needed</h2>
<ul>
    <li><strong>Python 3.x</strong>: Ensure you have Python 3 installed. You can download it from <a href="https://www.python.org/downloads/" target="_blank">python.org</a>.</li>
</ul>

<h2>Running the Application</h2>
<ol>
    <li><strong>Navigate to the Directory:</strong> Open a terminal or command prompt and navigate to the directory where your <code>getTimeStories.py</code> file is located.</li>
    <li><strong>Start the Flask Application:</strong> Run the following command to start the Flask server:
        <pre><code>python getTimeStories.py</code></pre>
        Upon successful start of the server, you will see output indicating that Flask is running and listening on a specific port for example "http://127.0.0.1:5000".
    </li>
    <li><strong>Access the API:</strong> Open any web browser and go to the following URL with the specied port (in our case "5000"):
        <ul>
            <li><a href="http://127.0.0.1:5000/getTimeStories" target="_blank">http://127.0.0.1:5000/getTimeStories</a></li>
            <li><a href="http://localhost:5000/getTimeStories" target="_blank">http://localhost:5000/getTimeStories</a></li>
        </ul>
        You will receive a JSON response containing the latest 6 stories from Time.com.
    </li>
</ol>

<h2>How It Works</h2>
<ol>
    <li><strong>Fetching Data:</strong> The application makes an HTTP GET request to Time.com to fetch the latest stories from the homepage.</li>
    <li><strong>Parsing HTML:</strong> The fetched HTML content is parsed using BeautifulSoup to locate the section with the latest stories.</li>
    <li><strong>Extracting Stories:</strong> The application extracts the titles and links of the 6 most recent stories.</li>
    <li><strong>Serving JSON:</strong> The extracted stories are returned as a JSON array via the <code>/getTimeStories</code> endpoint.</li>
</ol>

<h2>Example JSON Response</h2>
<p>The JSON response will be an array of objects, each representing a story with the following structure:</p>
<pre><code>[
{
    "title": "Title of the first story",
    "link": "https://time.com/link-to-the-first-story"
},
{
    "title": "Title of the second story",
    "link": "https://time.com/link-to-the-second-story"
},
...
]
</code></pre>
