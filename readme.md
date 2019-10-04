## informer

### why
i want to get notified when products become available

### how ...
#### ... to get started
```
./setup.sh
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