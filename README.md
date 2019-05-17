# AWS-ALB-lambda-python

Framework for load-balancer and lambda function.

To learn more about writing AWS Lambda functions in python, go to [the official documentation](https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html)

Blogs about AWS lambda and python is [here](https://aws.amazon.com/blogs/networking-and-content-delivery/lambda-functions-as-targets-for-application-load-balancers/)


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![serverless](http://public.serverless.com/badges/v3.svg)](4)
[![Pyhton-Lambda-Doc](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](1)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](5)
[![PyPI version fury.io](https://badge.fury.io/py/ansicolortags.svg)](7)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](2)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](2)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](3)
[![Pyhton Lambda](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

[1]: https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html
[2]: https://aws.amazon.com/blogs/networking-and-content-delivery/lambda-functions-as-targets-for-application-load-balancers/
[3]: https://github.com/aws-samples/serverless-sinatra-sample
[4]: https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html
[5]: https://www.python.org/
[6]: https://pypi.python.org/
[7]: https://pypi.python.org/pypi/ajayau404/
[8]: https://pypi.python.org/pypi/ansicolortags/

# Getting Started

This is the AWS lambda framework written in python. When the lambda function is triggered by ALB or API-Gateway the event variable that contain all the required info will be sent to the init function. By default this init function will be in lambda_function.py and the name will be lambda_handler. This framework contains the request resource mappin for the URL and response that you have to send back to Load-Balancer.

The package information is in [Pypi info](https://pypi.org/project/py-lambda/)

```
pip install py-lambda
```

This source code contain the following files:
* **lambda_function** : Contains the code that will be triggered by ALB or API-Gateway etc.
* **request** : Contains the request object which is created from the event that is send as an input.
* **response** : Contains the object that should be sent back from lambda function to ALB.
* **lambda_mapping** : Is the file that contain the mapping for the routes. Add your routes in here.
* **all_functions** : Contain the function contains the respective code that can be used for the given path.
* **test_LambdaHandler** : Contains the test code that can be usedfortesting all the functions.

``` Python
## test_LambdaHandler.py
import py_lambda.test_LambdaHandler as lTest
print(lTest.EVENT_FROM_ALB)
```

The above code will give the sample of the request that will be send by ALB.

```python
## lambda_function.py

import py_lambda.test_LambdaHandler as lTest
import py_lambda.lambda_function as lf

RESOURCE_PREFIX = ""
lTest.EVENT_FROM_ALB["path"]= RESOURCE_PREFIX+'/abc'
lTest.EVENT_FROM_ALB["httpMethod"] = "GET"

resp = lf.lambda_handler(event=lTest.EVENT_FROM_ALB,context= "some_context")
print(resp)
```

This will give you the reponse if you have a mapping in `lambda_mapping.py`. body in the response will contain whatever you set in the response. Even you can set the header and the response code accordingly using  `py_lambda.response.setResp` and `py_lambda.response.setHeader`
