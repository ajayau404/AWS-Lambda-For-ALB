#!/usr/bin/env python
import lambda_defines as ld
import all_Functions as allFun
"""
When the URL is in REST format then use ld.URL_REST_ID_STR in the mapping to indicate the REST-ID
/user/123/
To indicate user id as 123 use ld.URL_REST_ID_STR
"""
FUNCT_MAPPING = {
	"":{
		"GET":allFun.indexGET,
		"POST":allFun.indexPOST,
	},
	"test":{
		ld.URL_REST_ID_STR:{
			"GET": allFun.userIdGET,
		},
		"GET": allFun.testGET,
	},
	"abc":{
		"GET": allFun.abcGET,
	},
}

if __name__ == "__main__":
	None