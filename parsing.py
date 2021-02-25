#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv

req = requests.get('http://hanbit.co.kr/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

