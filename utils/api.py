from utils.http_methods import http_methods

"""Methods for testing Google Maps API"""

base_url = "https://rahulshettyacademy.com"    # Base URL
key = "?key=qaclick123" # Key for all requests

class google_maps_api():

    """Method for create a new locating"""

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Rehuse",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"    # Method POST resource
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Method for check a new locating"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for change a new locating"""

    @staticmethod
    def put_new_place(place_id):

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "70 winter walk, USA",
            "key": "qaclick123"
        }
        result_put = http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    """Method for delete a new locating"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = http_methods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete