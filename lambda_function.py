#!/usr/bin/env python
import sys, os, time, json
# sys.path.append("./lib")
## Custom modules
import request as Req
import response as Res
import lambda_mapping as lm
import lambda_defines as ld
import inp_validatn as inpValid
import funct_defines as funDef

def lambda_handler(event,context):
	"""
	lambda_function and lambda_handler are the name of the file and function name that should be specified in lambda configuration.
	"""
	reqObj = Req.Request(event)
	resObj = Res.Response()
	
	pathList = reqObj.getPathList()
	# print("pathList:", pathList)
	# resObj.setResp(httpCode = 200, httpCodeStr = "200 OK", respBody = event)
	# return resObj()

	respDict = reqObj.getHeaderParm(["referer"])
	if "referer" in respDict:
		retDomValid = inpValid.validateDomain(respDict["referer"])
		if retDomValid[funDef.FUNCTION_STAT] == funDef.SUCCESS:
			## Success
			resObj.setHeader("Access-Control-Allow-Origin", respDict["referer"])
			resObj.setResp(httpCode = 200, httpCodeStr = "200 OK", respBody = "")
		else:
			## Error
			resObj.setError(httpCode = 400, httpCodeStr = "400 ERROR", respBody = "Not authorized")
			return resObj()

	if reqObj.httpMeth().upper() == "OPTIONS":
		resObj.setHeader("Access-Control-Allow-Headers", "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token")
		resObj.setHeader("Access-Control-Allow-Credentials", True)
		resObj.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,PATCH,DELETE,OPTIONS")
		return resObj()

	if pathList == None:
		resObj.setError(httpCode = 400, httpCodeStr = "400 ERROR", respBody = "Invalid request")
		return resObj()
	if len(pathList) > 10:
		resObj.setError(httpCode = 400, httpCodeStr = "400 ERROR", respBody = "Invalid resource")
		return resObj()

	resMap = lm.FUNCT_MAPPING

	mapFlag = True
	resCount = 0
	for eachRes in pathList:
		if eachRes in resMap:
			resMap = resMap[eachRes]
			resCount += 1
		else:
			if ld.URL_REST_ID_STR in resMap: 
				resMap = resMap[ld.URL_REST_ID_STR]
				resCount += 1
			else:
				mapFlag = False
				break

	# print("pathList resCount:", pathList[resCount:], mapFlag)
	# print("resMap:", resMap, resCount)
	if mapFlag:
		if reqObj.httpMeth() in resMap:
			respMeth = resMap[reqObj.httpMeth()](reqObj)
			resObj.setResp(httpCode = 200, httpCodeStr = "200 OK", respBody = respMeth)
			return resObj()			
		else:
			resObj.setError(httpCode = 400, httpCodeStr = "400 ERROR", respBody = "Invalid request method")
			return resObj()
	
	resObj.setError(httpCode = 400, httpCodeStr = "400 ERROR", respBody = "Invalid resource")
	return resObj()

def main():
	None

if __name__ == "__main__":
	main()