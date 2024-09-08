import json
import allure
from requests import Response
from utils.checking import checking
from utils.api import google_maps_api

@allure.epic("Test create a new place")
class Test_create_place():

    @allure.description("Test create, update, delete a new place")
    def test_create_new_place(self):

        print("Method POST")
        result_post: Response = google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        checking.check_status_code(result_post, 200)
        checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text) # For see all required fields!!!
        # print(list(token))
        checking.check_json_value(result_post, 'status', 'OK')

        print("Method GET POST")
        result_get: Response = google_maps_api.get_new_place(place_id)
        checking.check_status_code(result_get, 200)
        checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Method PUT")
        result_put: Response = google_maps_api.put_new_place(place_id)
        checking.check_status_code(result_put, 200)
        checking.check_json_token(result_put, ['msg'])
        checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Method GET PUT")
        result_get: Response = google_maps_api.get_new_place(place_id)
        checking.check_status_code(result_get, 200)
        checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        checking.check_json_value(result_get, 'address', '70 winter walk, USA')

        print("Method DELETE")
        result_delete: Response = google_maps_api.delete_new_place(place_id)
        checking.check_status_code(result_delete, 200)
        checking.check_json_token(result_delete, ['status'])
        checking.check_json_value(result_delete, 'status', 'OK')


        print("Method GET DELETE")
        result_get: Response = google_maps_api.get_new_place(place_id)
        checking.check_status_code(result_get, 404)
        checking.check_json_token(result_get,['msg'])
        checking.check_json_search_word_in_value(result_get, 'msg', 'failed')
        print("All tests are passed")