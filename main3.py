import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

# pytrend.build_payload(kw_list=['Taylor Swift'])
# # Interest by Region
# df = pytrend.interest_by_region()
# df.head(10)
#
# print(df.head(10))
# df.reset_index().plot(x='geoName', y='Taylor Swift', figsize=(120, 10), kind='bar')


# df = pytrend.trending_searches(pn='russia')
# print(df.head(10))
#
# # Get Google Top Charts
# df = pytrend.top_charts(2020, hl='en-US', tz=300, geo='RU')
# print(df.head(10))
#
# keywords = pytrend.suggestions(keyword='Путин')
# df = pd.DataFrame(keywords)
# df.drop(columns='mid')
# print(df.head(100))

pytrend.build_payload(kw_list=["adult"])
related_queries = pytrend.related_queries()
# print(type(related_queries))
# print(related_queries)
for k,v in related_queries.items():
    print(v['top'], type(v['top']))
    print(v['rising'], type(v['rising']))
