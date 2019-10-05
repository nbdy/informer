## informer
[![Build Status](http://build.eberlein.io:8080/job/informer/badge/icon)](http://build.eberlein.io:8080/job/informer/)
### why
i want to get notified when products become available

### how ...
#### ... to get started
```
(optional)
pip install git+https://github.com/smthnspcl/seleniumloader
```

#### ... to run
```
./informer.py --help

usage: python3 Informer.py {arguments}
	-h	--help
	-d	--driver	sets the webdriver
		default: chrome
		possible arguments: chrome, c, firefox, f
	-e	--executable-path	path to driver
		default: chrome/linux/chromedriver
	--headless	run browser headless
		possible arguments: none
```

#### ... to add new products
[check here](https://github.com/smthnspcl/informer/blob/master/libs/amazon.py#L78)
