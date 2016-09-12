# Artifacia Python Client

This python client is a simple wrapper around our powerful Visual Discovery [API](http://docs.artifacia.com/).

The wrapper allows you to create your own index of images on which you would like to enhance the product discovery experiences. It also allows you to get various types of recommendations which are listed below.

* Visual Recommendation
* Cross Product Recommendation
* Personalized Recommendation

## Installation

To install the package you can follow the steps:-

```python
[sudo] pip install artifacia
```

## Getting Started

The API is really easy and simple to use. First you need to visit [this](http://www.artifacia.com/requestaccess/) page and request for username and password. Using that credentials you can create your constructor and get stated.

```python
from artifacia import artifacia
user_name = <your_username>
password = <your_password>
client = artifacia.Client(user_name, password)
```

### Creating your index
The first step is to create a index of the items that you would like to store in our databases to perform search against. If you don't have data ready right now you can quickly get started with our [sample data](https://github.com/artifacia/artifacia-client-python/blob/master/sample_data.json). Once the data is stored and indexed we will inform you shortly.

```python
import json
sample_data = json.load(open("sample_data.json","rb"))
data_indexing_response = client.upload_item_data(sample_data)
print data_indexing_response
```

### Performing Visual Recommendation
Once you receive a notification from us about the status of the indexed data, you are ready to search.
You can search for a product ID indexed in the sample data you inserted/uploaded. And also specify the number of results you want to be returned as well as attributes if want to proritize the result below is the example which you can refer.

```python
sample_prod_id = 2761
num = 4 
filters = {"color":1, "pattern":1}
query_response = client.get_visual_recommendation(sample_prod_id, num, filters)
print query_response
```
