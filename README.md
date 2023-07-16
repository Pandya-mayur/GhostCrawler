 <pre>

                        
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║  ███╗███████║██║   ██║███████╗   ██║   ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                     
          Empowering Exploration: GhostCrawler - Open Source Intelligence for the DarkWeb

</pre>


### Features
1. Onion Crawler (.onion)
2. Returns Page title and address with a short description about the site
3. Save links to database
4. Get data from site
5. Save crawl info to JSON file
6. Crawl custom domains
7. Check if the link is live
8. Built-in Updater
9. Build visual tree of link relationship that can be quickly viewed or saved to an image file

...(will be updated)

### Dependencies
- Tor
- Python ^3.8
- Golang 1.19
- Poetry

### Python Dependencies

(see requirements.txt for more details)

### Golang Dependencies
- https://github.com/KingAkeem/gotor (This service needs to be ran in tandem with TorBot)

## Installation

### From source
Before you run the torBot make sure the following things are done properly:

* Run the tor service:
```sh
sudo service tor start
```
* Make sure that your torrc is configured to SOCKS_PORT localhost:9050

* Open a new terminal and run:
```sh
cd gotor && go run cmd/main/main.go -server
```

* Install TorBot Python requirements using poetry

```sh
poetry install # to install dependencies
poetry run python run.py -u https://www.example.com --depth 2 -v # example of running command with poetry
poetry run python run.py -h # for help
```

<pre>
usage: Gather and analayze data from Tor sites.

optional arguments:
  -h, --help            show this help message and exit
  --version             Show current version of TorBot.
  --update              Update TorBot to the latest stable version
  -q, --quiet
  -u URL, --url URL     Specifiy a website link to crawl
  -s, --save            Save results in a file
  -m, --mail            Get e-mail addresses from the crawled sites
  -p, --phone           Get phone numbers from the crawled sites
  --depth DEPTH         Specifiy max depth of crawler (default 1)
  --gather              Gather data for analysis
  -v, --visualize       Visualizes tree of data gathered.
  -d, --download        Downloads tree of data gathered.
  -e EXTENSION, --extension EXTENSION
                        Specifiy additional website extensions to the list(.com , .org, .etc)
  -c, --classify        Classify the webpage using NLP module
  -cAll, --classifyAll  Classify all the obtained webpages using NLP module
  -i, --info            Info displays basic info of the scanned site` </pre>

* NOTE: -u is a mandatory for crawling


### Using Docker

- Ensure than you have a tor container running on port 9050.
- Build the image using following command (in the root directory):

    `docker build -f docker/Dockerfile -t dedsecinside/torbot .`
- Run the container (make sure to link the tor container as `tor`):

    `docker run --link tor:tor --rm -ti dedsecinside/torbot`

### Using executable (Linux Only)

On Linux platforms, you can make an executable for TorBot by using the install.sh script.
You will need to give the script the correct permissions using `chmod +x install.sh`
Now you can run `./install.sh` to create the torBot binary.
Run `./torBot` to execute the program.


## Curated Features
- [x] Visualization Module Revamp
- [x] Implement BFS Search for webcrawler
- [x] Use Golang service for concurrent webcrawling
- [x] Improve stability (Handle errors gracefully, expand test coverage and etc.)
- [ ] Randomize Tor Connection (Random Header and Identity)
- [ ] Keyword/Phrase search
- [ ] Social Media Integration
- [ ] Increase anonymity
- [x] Improve performance (Done with gotor)
- [ ] Screenshot capture



## Credits
I would like to express my gratitude to all the team members of The Linux boys and all the open source projects that have made this tool possible and have made recon tasks easier to accomplish.

