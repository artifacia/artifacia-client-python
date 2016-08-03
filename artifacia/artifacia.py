import json
import requests

class Client:
    """
    This is the entry point in Python client API.
    if you are going to use our API, first of all you should instanciate
    client objent with your username and passwrod which you got from the dashboard.
    Now start using Artifacia recommendations APIS.
    """
    def __init__(self, username, password):
        """
        Artifacia recommendation client initiallization

        @parameter username, password : will help you to access our API like
        upload your data and get recommendations

        """
        self.user = username
        self.passwd = password

    def upload_user_purchased_items(self, user_id ,user_data):
        """
        Input parameter :
            user_data which is list of json

        You can use this method with the username and password to upload your
        user's interaction data like purchased items

        output: status for your request in json format
        """
        response = requests.post('http://api.artifacia.com/v1/users/'+str(user_id)+'/purchased_items', data=json.dumps(user_data), auth=(self.user, self.passwd), headers={'Content-Type':'application/json'})
        return json.loads(response.text)

    def upload_user_viewed_items(self, user_id, user_data):
        """
        Input parameter :
            user_data which is list of json

        You can use this method with the username and password to upload your
        user's interaction data like viewed items

        output: status for your request in json format
        """
        response = requests.post('http://api.artifacia.com/v1/users'+str(user_id)+'/viewed_items', data=json.dumps(user_data), auth=(self.user, self.passwd), headers={'Content-Type':'application/json'})
        return json.loads(response.text)

    def upload_item_data(self, item_data):
        """
        Input parameter :
            item_data which is list of json
        You can use this method to upload your catalog data

        output : status for your request in json format
        """
        response = requests.post('http://api.artifacia.com/v1/items', data=json.dumps(item_data), auth=(self.user, self.passwd), headers={'Content-Type':'application/json'})
        return json.loads(response.text)

    def delete_item_data(self, item_ids):
        """
        Input parameter :
            item_ids which is in json format
        If you want to delete some items from our database incase if some
        items are out of stock then you can esily delete your items usinf this method

        output: status for your request in json format
        """
        response = requests.delete('http://api.artifacia.com/v1/items', data=json.dumps(item_ids), auth=(self.user, self.passwd), headers={'Content-Type':'application/json'})
        return json.loads(response.text)

    def get_visual_recommendation(self, prod_id, num):
        """
        Input parameter :
            prod_id which is an integer type
        It will help you to get similar image ids corresponding to a given image id
        output :
            return list of image item_ids
        """
        response = requests.get('http://api.artifacia.com/v1/recommendation/similar/' + str(prod_id)+'/'+str(num), auth=(self.user, self.passwd), headers={'Content-Type':'application/json'})
        return json.loads(response.text)

    def get_cpr_recommendation(self, prod_id, num):
        """
        Input parameter :
            prod_id which is an integer type
        If you want to get items which goes together you can use this method with the given username and password
        output:
            return list of product ids which can go with the given image
        """
        response = requests.get('http://api.artifacia.com/v1/recommendation/collections/' + str(prod_id)+'/'+str(num),  auth=(self.user, self.passwd), headers={'Content-Type':'application/json'})
        return json.loads(response.text)

    def get_personalized_recommendation(self, user_id, num):
        """
        Input parameter :
            user_id which is integer type
        If you want to get recommendation on the basis of user behaviour then use this method with the given username and passwd
        output:
            list of prod_ids
        """
        response = requests.get('http://api.artifacia.com/v1/recommendation/user/' +str(user_id)+'/'+str(num),  auth=(self.user, self.passwd), headers={'Content-Type':'application/json'})
        return json.loads(response.text)
