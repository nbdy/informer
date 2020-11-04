## informer
[![Build Status](http://build.eberlein.io:8080/job/python_informer/badge/icon)](http://build.eberlein.io:8080/job/python_informer/)
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

usage: ./informer.py {arguments}
	{arguments}		    {info}
	-sc 	--site-config 	    can be used more than once
	-h 	--headless
	-d 	--driver
	-e 	--executable_path
```

#### ... to add new products
[check here](https://github.com/nbdy/informer/blob/master/libs/amazon.py#L78)
