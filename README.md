<h1>Smartphone Data Scraper using Selenium and Beautiful Soup</h1>

<p>This project demonstrates how to scrape smartphone data from 
<a href="https://www.smartprix.com/">Smartprix.com</a> using Selenium and Beautiful Soup. 
The scraped data includes key specifications of various smartphone models and is stored in 
a dataset format for further use.</p>

<h2>Features</h2>

<ul>
  <li><strong>Data Source:</strong> Smartprix.com (Smartphone section)</li>
  <li><strong>Web Scraping Tool:</strong> Selenium (with WebDriver Manager)</li>
  <li><strong>Data Parsing Tool:</strong> Beautiful Soup</li>
  <li><strong>Data Format:</strong> The dataset contains the following columns:
    <ul>
      <li><code>model</code>: The name of the smartphone model</li>
      <li><code>price</code>: The price of the smartphone</li>
      <li><code>rating</code>: User rating of the smartphone</li>
      <li><code>sim</code>: SIM card specifications (e.g., single, dual)</li>
      <li><code>processor</code>: Processor information</li>
      <li><code>ram</code>: RAM capacity</li>
      <li><code>battery</code>: Battery capacity</li>
      <li><code>display</code>: Display size and type</li>
      <li><code>camera</code>: Camera specifications</li>
      <li><code>card</code>: Memory card support</li>
      <li><code>os</code>: Operating system</li>
    </ul>
  </li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/lagyal/advanced-web-scraping.git
cd advanced-web-scraping
</code></pre>
  </li>

  <li>Install the required dependencies:
    <ul>
      <li><strong>Selenium</strong></li>
      <li><strong>WebDriver Manager</strong></li>
      <li><strong>Beautiful Soup</strong></li>
    </ul>
  </li>
</ol>

<h2>How It Works</h2>

<ol>
  <li><strong>Web Scraping with Selenium:</strong> Selenium is used to automate browser actions and scrape the raw HTML content of the smartphone listings from Smartprix.com.</li>
  <li><strong>WebDriver Manager:</strong> WebDriver Manager is used to automatically manage the browser drivers required by Selenium.</li>
  <li><strong>HTML Parsing with Beautiful Soup:</strong> After scraping, the HTML content is parsed using Beautiful Soup to extract relevant information about each smartphone.</li>
  <li><strong>Dataset Creation:</strong> The extracted data (model, price, rating, etc.) is structured into a tabular format for easy access and analysis.</li>
</ol>

<h2>Usage</h2>

<ol>
  <li>Ensure you have the necessary web drivers installed using WebDriver Manager. No manual downloads required.</li>

  <li>Run the script:
    <pre><code>python smartprix.py</code></pre>
  </li>

  <li>The script will:
    <ul>
      <li>Scrape smartphone data from Smartprix.com using Selenium.</li>
      <li>Extract the required information from the HTML using Beautiful Soup.</li>
      <li>Store the data in a dataset (e.g., CSV or Excel format).</li>
    </ul>
  </li>

  <li>The final dataset will contain the following smartphone specifications:
    <ul>
      <li>Model, Price, Rating, SIM, Processor, RAM, Battery, Display, Camera, Card, OS</li>
    </ul>
  </li>
</ol>

<h2>Dataset Example</h2>

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Price</th>
      <th>Rating</th>
      <th>SIM</th>
      <th>Processor</th>
      <th>RAM</th>
      <th>Battery</th>
      <th>Display</th>
      <th>Camera</th>
      <th>Card</th>
      <th>OS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Example Phone 1</td>
      <td>$300</td>
      <td>4.5</td>
      <td>Dual</td>
      <td>Snapdragon</td>
      <td>4GB</td>
      <td>5000mAh</td>
      <td>6.5"</td>
      <td>12MP</td>
      <td>Yes</td>
      <td>Android</td>
    </tr>
    <tr>
      <td>Example Phone 2</td>
      <td>$250</td>
      <td>4.3</td>
      <td>Single</td>
      <td>MediaTek</td>
      <td>3GB</td>
      <td>4000mAh</td>
      <td>6.3"</td>
      <td>8MP</td>
      <td>No</td>
      <td>Android</td>
    </tr>
  </tbody>
</table>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>Selenium</li>
  <li>Beautiful Soup 4</li>
  <li>WebDriver Manager</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
