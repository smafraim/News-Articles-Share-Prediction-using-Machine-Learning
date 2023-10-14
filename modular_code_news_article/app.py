# Import the required modules
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from news_articles_features import NewsArticleShares
import pandas as pd
import pickle
import numpy as np

# Create the FastAPI app
NewsArticle = FastAPI()
'''templates = Jinja2Templates(directory="templates")

@NewsArticle.get("/")
async def render_page(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})'''

# Load the model from disk
loaded_model = pickle.load(open('news_shares_modelcorrected2.pkl', 'rb'))

# Expose the prediction functionality
@NewsArticle.post('/predict')
def predict_shares(data: NewsArticleShares):
    # Convert the input data to a dictionary
    data = data.dict()
    print(data)
    # Create a DataFrame from the data
    data = pd.DataFrame([data])
    print(data.head())
    # Make predictions using the loaded model
    #final_features = [np.array(data)]
    prediction = loaded_model.predict(data)


    # Return the predicted number of shares as a response
    return {f"Your news article would have around {int(prediction)} shares"}

# Run the API with uvicorn
'''if __name__ == '__main__':
    uvicorn.run("app:NewsArticle", host='0.0.0.0', port=8005, reload=True, debug=True, workers=3)
'''