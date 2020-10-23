import numpy as np 
import pandas as pd 
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 

df = pd.read_csv('tweets.csv')

text = df.text.values