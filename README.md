 <pre>

                        
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║  ███╗███████║██║   ██║███████╗   ██║   ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                     
          Empowering Exploration: GhostCrawler - Open Source Intelligence for the DarkWeb

</pre>



## 📚 Currently supported Search engines
- ahmia
- darksearchio
- onionland
- notevil
- darksearchenginer
- phobos
- GhostCrawler2server
- torgle
- GhostCrawler2engine
- tordex
- tor66
- tormax
- haystack
- multivac
- evosearch
- deeplink

## 🛠️ Installation
### With PyPI

```pip3 install GhostCrawler2```

### With Github

```bash
git clone https://github.com/megadose/GhostCrawler2.git
cd GhostCrawler2/
python3 setup.py install
```


## 📈  Usage

Help:
```
usage: GhostCrawler2 [-h] [--proxy PROXY] [--output OUTPUT]
                  [--continuous_write CONTINUOUS_WRITE] [--limit LIMIT]
                  [--engines [ENGINES [ENGINES ...]]]
                  [--exclude [EXCLUDE [EXCLUDE ...]]]
                  [--fields [FIELDS [FIELDS ...]]]
                  [--field_delimiter FIELD_DELIMITER] [--mp_units MP_UNITS]
                  search

positional arguments:
  search                The search string or phrase

optional arguments:
  -h, --help            show this help message and exit
  --proxy PROXY         Set Tor proxy (default: 127.0.0.1:9050)
  --output OUTPUT       Output File (default: output_$SEARCH_$DATE.txt), where $SEARCH is replaced by the first chars of the search string and $DATE is replaced by the datetime
  --continuous_write CONTINUOUS_WRITE
                        Write progressively to output file (default: False)
  --limit LIMIT         Set a max number of pages per engine to load
  --engines [ENGINES [ENGINES ...]]
                        Engines to request (default: full list)
  --exclude [EXCLUDE [EXCLUDE ...]]
                        Engines to exclude (default: none)
  --fields [FIELDS [FIELDS ...]]
                        Fields to output to csv file (default: engine name link), available fields are shown below
  --field_delimiter FIELD_DELIMITER
                        Delimiter for the CSV fields
  --mp_units MP_UNITS   Number of processing units (default: core number minus 1)

[...]
```

### Multi-processing behaviour

By default, the script will run with the parameter `mp_units = cpu_count() - 1`. It means if you have a machine with 4 cores,
it will run 3 scraping functions in parallel. You can force `mp_units` to any value but it is recommended to leave to default.
You may want to set it to 1 to run all requests sequentially (disabling multi-processing feature).

Please note that continuous writing to csv file has not been *heavily* tested with multiprocessing feature and therefore
may not work as expected.

Please also note that the progress bars may not be properly displayed when `mp_units` is greater than 1.
**It does not affect the results**, so don't worry.

### Examples

To request all the engines for the word "computer":
```
GhostCrawler2 "computer"
```

To request all the engines excepted "Ahmia" and "Candle" for the word "computer":
```
GhostCrawler2 "computer" --exclude ahmia candle
```

To request only "Tor66", "DeepLink" and "Phobos" for the word "computer":
```
GhostCrawler2 "computer" --engines tor66 deeplink phobos
```

The same as previously but limiting to 3 the number of pages to load per engine:
```
GhostCrawler2 "computer" --engines tor66 deeplink phobos --limit 3
```

Please kindly note that the list of supported engines (and their keys) is given in the script help (-h).


### Output

#### Default output

By default, the file is written at the end of the process. The file will be csv formatted, containing the following columns:
```
"engine","name of the link","url"
```





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
- https://github.com/KingAkeem/gotor (This service needs to be ran in tandem with GhostCrawler)

## Installation

### From source
Before you run the GhostCrawler make sure the following things are done properly:

### Mac/Linux/Windows:

* Run the tor service:
```sh
sudo service tor start
```
* Make sure that your torrc is configured to SOCKS_PORT localhost:9050

```sh
git clone https://github.com/Pandya-mayur/GhostCrawler.git
cd GhostCrawler
```

* Open a new terminal and run:
```sh
cd gotor && go run cmd/main/main.go -server
```
* Install GhostCrawler Python requirements using poetry

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

    `docker build -f docker/Dockerfile -t Pandya-mayur/GhostCrawler .`
- Run the container (make sure to link the tor container as `tor`):

    `docker run --link tor:tor --rm -ti Pandya-mayur/GhostCrawler`

### Using executable (Linux Only)

On Linux platforms, you can make an executable for TorBot by using the install.sh script.
You will need to give the script the correct permissions using `chmod +x install.sh`
Now you can run `./install.sh` to create the GhostCrwaler binary.
Run `./GhostCrawler` to execute the program.


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
- [x] Screenshot capture



## Credits
I would like to express my gratitude to all the team members of The Linux boys and all the open source projects that have made this tool possible and have made recon tasks easier to accomplish.

