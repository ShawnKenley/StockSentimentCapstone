import pandas as pd
import numpy as np
from newspaper import Article
from newspaper import Config
import time

user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10

def getArticle_Body(dataframe, filename):
    total = len(dataframe)

    for i in range(total):
        print('set 1:',i, 'out of', total)
        try:
            url = dataframe['Links'][i]
            page = Article(url, config=config)
            time.sleep(3)
            page.download()
            page.parse()

            dataframe['Bodies'].iloc[i] = page.text
            dataframe['Published_Date'].iloc[i] = page.publish_date
            
        except:
            dataframe['unscraped_links'].iloc[i] = dataframe['Links'][i]
    
    dataframe.to_csv(filename+'_bodies.csv', index=False)
    print('SAVED')


def main():

    dflinks_1 = pd.read_csv("dflinks_1.csv")
    getArticle_Body(dflinks_1, 'dflinks_1')

if __name__ == "__main__":
	main()