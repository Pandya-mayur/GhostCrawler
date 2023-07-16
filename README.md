 <pre>



██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║  ███╗███████║██║   ██║███████╗   ██║   ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                     


             Empowering Exploration: GhostCrawler - Open Source Intelligence for the DarkWeb
  
                                                     

## OSINT tool for Deep and Dark Web.

GhostCrawler is an open-source intelligence tool developed in Python that enables deep exploration of the Dark Web. It offers valuable insights into information security, providing knowledge about threats and malicious activities that can impact businesses. While open-source intelligence using the internet is common, venturing into the darknet poses unique challenges for cybersecurity analysts. GhostCrawler addresses these challenges by utilizing specialized collection, processing, and analysis tools.
 
## Explore the Hidden Depths 

Motivated by the need to navigate the deep web, GhostCrawler aims to collect open data from the dark web and leverage data mining algorithms to extract as much information as possible. The tool generates an interactive tree graph that visually represents the relationships among the collected intelligence data. This graph module allows users to delve into the intricate web of connections within the darknet. 
 
 
### Versatile Applications

Beyond its primary objective of identifying illegal activities, GhostCrawler offers a range of useful features. It can crawl and create an index for the deep web, storing the index in a database or a JSON file for future reference. The tool includes a live checker to verify the availability of web addresses, which is particularly important given the dynamic nature of deep web links. Researchers and security enthusiasts can utilize GhostCrawler to assess basic vulnerabilities in dark web pages, expanding their understanding of the security landscape.


### How GhostCrawler Works
GhostCrawler employs a web crawling algorithm that takes a list of seed URLs as input and executes a series of steps iteratively. These steps involve removing a URL from the list, checking the page's existence, downloading the page, assessing its relevance, extracting any embedded links, checking the cache for duplicate links, and adding unique links back to the URL list. After processing all URLs, GhostCrawler returns the most relevant page.

1. Remove a URL from the URL list.
2. Check existence of the page.
3. Download the corresponding page.
4. Check the Relevancy of the page.
5. Extract any links contained in it.
6. Check the cache if the links are already in it.
7. Add the unique links back to the URL list.
8. After all URLs are processed, return the most relevant page.

### Features
1. Onion Crawler (.onion).(Completed)
2. Returns Page title and address with a short description about the site.(Partially Completed)
3. Save links to database.(PR to be reviewed)
4. Get emails from site.(Completed)
5. Save crawl info to JSON file.(Completed)
6. Crawl custom domains.(Completed)
7. Check if the link is live.(Completed)
8. Built-in Updater.(Completed)
9. Visualizer module.(Not started)
10. Social Media integration.(not Started)
...(will be updated)

## Contribute
Contributions to this project are always welcome.
To add a new feature fork the dev branch and give a pull request when your new feature is tested and complete.
If its a new module, it should be put inside the modules directory.
The branch name should be your new feature name in the format <Feature_featurename_version(optional)>. For example, <i>Feature_FasterCrawl_1.0</i>.
Contributor name will be updated to the below list. 😀
<br>
<b> NOTE : The PR should be made only to `dev` branch of GhostCrawler. </b>

### OS Dependencies
- Tor
- Python 3.x
- Golang 1.x (Not Currently Used)

### Python Dependencies
- beautifulsoup4
- pyinstaller
- PySocks
- termcolor
- requests
- requests_mock
- yattag


## Basic setup
Before you run the torBot make sure the following things are done properly:

* Run tor service
`sudo service tor start`

* Make sure that your torrc is configured to SOCKS_PORT localhost:9050

* Install TorBot Python requirements
`pip3 install -r requirements.txt`

On Linux platforms, you can make an executable for TorBot by using the install.sh script.
You will need to give the script the correct permissions using `chmod +x install.sh`
Now you can run `./install.sh` to create the torBot binary.
Run `./torBot` to execute the program. 

An alternative way of running torBot is shown below, along with help instructions.

`python3 torBot.py or use the -h/--help argument`
<pre>
usage: torBot.py [-h] [-v] [--update] [-q] [-u URL] [-s] [-m] [-e EXTENSION]
                 [-l] [-i]

optional arguments:
  -h, --help            Show this help message and exit
  -v, --version         Show current version of TorBot.
  --update              Update TorBot to the latest stable version
  -q, --quiet           Prevent header from displaying
  -u URL, --url URL     Specifiy a website link to crawl, currently returns links on that page
  -s, --save            Save results to a file in json format
  -m, --mail            Get e-mail addresses from the crawled sites
  -e EXTENSION, --extension EXTENSION
                        Specifiy additional website extensions to the
                        list(.com or .org etc)
  -l, --live            Check if websites are live or not (slow)
  -i, --info            Info displays basic info of the scanned site (very
                        slow)` </pre>

* NOTE: All flags under -u URL, --url URL must also be passed a -u flag.


## TO-DO
- [ ] Visualization Module
- [x] Implement BFS Search for webcrawler
- [X] Multithreading for Get Links
- [ ] Improve stability (Handle errors gracefully, expand test coverage and etc.)
- [ ] Create a user-friendly GUI 
- [ ] Randomize Tor Connection (Random Header and Identity)
- [ ] Keyword/Phrase search
- [ ] Social Media Integration
- [ ] Increase anonymity and efficiency

### Have ideas?
If you have new ideas which is worth implementing, mention those by starting a new issue with the title [FEATURE_REQUEST].
If the idea is worth implementing, congratz, you are now a contributor.

## Related Works
OSINT and the Dark Web: The Dark Web has proven a very useful and reliable tool in the hands of individuals wishing to be involved in illegal, criminal or terrorist activities, setting sight on getting great economic or political benefits without being identified from government authorities and security agencies world-wide. To this end, LEAs need to become more agile when dealing with criminality on the Dark Web, and in particular on its Hidden Service Markets, and need to invest in new training and technology, if not to get ahead of the criminals, then at least to keep pace[1]. 

Using TOR for Open Source Intelligence: Although the use of Tor for OSINT does not raise specific legal concerns, there are a few interesting arguments that have been raised about using OSINT in general. One of them touches on the Council of Europe’s Convention on Cybercrime. Article 32 (a) of the Convention regulates transborder access to stored computer data with respect to ‘publicly available (open source) stored computer data, regardless of where the data is located geographically’[2].

OSINT in Social Networks: In summary, they examined and compared the needs of the Open Source Intelligence community with what social media has to offer investigators. They observed that a friends list of a given individual is a useful starting point for launching an investigation but found that several technical limitations (privacy and platform restrictions and data availability and longevity) may prevent investigators from accessing friend list information of a target account. They address privacy restrictions for the particular case of friends by creating a private friend discovery algorithm with hunter-seeker behaviours[3]. 

Data Mining in The Dark: This paper successfully explored an open-source intelligence automation toolset that scanned across the darknet. It described and shared the tools, process, and techniques to build a secure darknet connection, and then collected, processed, stored, and analysed data. This paper showed the viability of darknet open-source intelligence using the completed toolset. In the end, the toolset finds entities and links entities from the darknet thereby showing strong potential to aid the open source intelligence professional[4]. 




## License
GNU Public License

