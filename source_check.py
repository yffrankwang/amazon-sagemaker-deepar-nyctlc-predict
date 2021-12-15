import boto3
import io
import json
import time
import s3fs
import pandas as pd
import matplotlib.pyplot as plt
import datetime

datafile = "source.csv"

lineno = 0
with open(datafile) as fr:
	while True:
		lineno += 1
		s = fr.readline()
		if not s:
			break

		ss = s.split(",")
		try:
			datetime.datetime.strptime(ss[0], "%Y-%m-%d %H:%M:%S")
		except Exception as e:
			print("%d timestamp error: %s" % (lineno, str(e)))
			break


