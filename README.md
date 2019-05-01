# AWS-ALB-lambda-python

Framework for load-balancer and lambda function.

To learn more about writing AWS Lambda functions in python, go to [the official documentation](https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html)

Blogs about AWS lambda and python is [here](https://aws.amazon.com/blogs/networking-and-content-delivery/lambda-functions-as-targets-for-application-load-balancers/)

[![Pyhton-Lambda-Doc][1]][1]
[![Blog][2]][2]
[![Sample][3]][3]

[1]: https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html
[2]: https://aws.amazon.com/blogs/networking-and-content-delivery/lambda-functions-as-targets-for-application-load-balancers/
[3]: https://github.com/aws-samples/serverless-sinatra-sample

# Getting Started

According to default lambda configuration lambda_function.py will be the first file called by lambda and lambda_handler will be the first function. 

``` Python
## lambda_function.py

import lambda_function as lf

EVENT_FROM_ALB = {  "body": u"", 
	u"requestContext": 
	{u"elb": 
		{
			u"targetGroupArn": u"arn:aws:elb:ap-region-1:11:targetgroup/FROM_TARGET-GROUP/abc"
		}
	}, 
	u"queryStringParameters": {"a":1}, 
	u"httpMethod": u"GET", 
	u"headers": 
	{
		u"via": u"2.0 test.cloudfront.net (CloudFront)", 
		u"accept-language": u"en-US,en;q=0.5", 
		u"cloudfront-viewer-country": u"IN", 
		u"accept": u"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
		u"upgrade-insecure-requests": u"1", 
		u"cloudfront-is-mobile-viewer": u"false", 
		u"accept-encoding": u"gzip, deflate, br", 
		u"x-forwarded-port": u"443", 
		u"user-agent": u"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/", 
		u"cache-control": u"no-cache", 
		u"te": u"trailers", 
		u"cloudfront-is-desktop-viewer": u"true", 
		u"cloudfront-is-smarttv-viewer": u"false", 
		u"x-forwarded-for": u"192.168.1.1, 1.1.1.1", 
		u"x-amzn-trace-id": u"Root=1-5c0a5a83-123344", 
		u"host": u"clib.fyers.in", 
		u"x-forwarded-proto": u"https", 
		u"x-amz-cf-id": u"abc==", 
		u"pragma": u"no-cache", 
		u"connection": u"Keep-Alive", 
		u"cloudfront-is-tablet-viewer": u"false", 
		u"cloudfront-forwarded-proto": u"https"
	}, 
	u"path": u"/Some_ramdom_path/345/", 
	u"isBase64Encoded": False
}

EVENT_FROM_ALB["path"]= RESOURCE_PREFIX+'/abc'
EVENT_FROM_ALB["httpMethod"] = "GET"

resp = lf.lambda_handler(event=EVENT_FROM_ALB,context= "some_context")
print(resp)
```