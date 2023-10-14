from pydantic import BaseModel


class NewsArticleShares(BaseModel):
     max_avg_key: float
     href_avg_shares:float
     avg_shares_daily: float
     unique_tokens_rate: float
     global_rate_positive_words: float
     min_avg_key: float
     avg_avg_key: float
     num_keywords: float
     global_sentiment_polarity: float
     verb_count_title: float
     average_token_length: float
     global_subjectivity: float
     title_readability: float
     global_rate_negative_words: float
     num_videos: float
     noun_count_title: float
     num_hrefs: float
     num_imgs: float
     

 
