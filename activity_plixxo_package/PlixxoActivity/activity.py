""" A python program to push the data in the kinesis Stream """
from datetime import datetime
import json
import boto3

class activity:
	""" This class contains all the necessary functions to push the
		data in the kinesis stream """
	
	def __init__(self, stream_name):
		""" This is the constructor which takes stream_name as argument as a string """
		self.stream_name=stream_name

		
	def push_to_stream(self, s):
		""" This function actually pushes the string 's' in the kinesis 
		    stream """
		client_kinesis = boto3.client('kinesis')#Creation of a kinesis client
		response = client_kinesis.put_record(StreamName=self.stream_name,Data=s,PartitionKey=',')#calling the put_record function to push the record into th stream
		
	
				
	def insert_to_stream(self, json_data):
		""" This is the main function which further calls the push_to_s3
		    and pass the json to be pushed into the stream as string """
		self.push_to_stream(json.dumps(json_data))
		
		

		
		


