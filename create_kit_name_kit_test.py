import sender_stand_request
import data


def create_new_user_token_on_success():
  user_response = sender_stand_request.post_new_user(data.user_body)
  return user_response.json()["authToken"]

#Prueba positiva
def positive_assert(kit_body, auth_token):

    user_response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert user_response.status_code == 201
    assert user_response.json()["name"] == kit_body["name"]

#prueba negativa
def negative_assert(kit_body, auth_token):

    user_response = sender_stand_request.post_new_kit(kit_body, auth_token)


    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 1 caracteres y no más de 511 caracteres"

def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def test_create_user_1_letter_in_first_name_get_success_response():
    auth_token = create_new_user_token_on_success()
    positive_assert({"name": "a"}, auth_token)


def test_create_user_511_letter_in_first_name_get_success_response():
    auth_token = create_new_user_token_on_success()
    positive_assert(data.kit_body_name_limit, auth_token)

def test_create_user_0_letter_in_first_name_get_error_response():
    auth_token = create_new_user_token_on_success()
    negative_assert({"name": ""}, auth_token)

def test_create_user_512_letter_in_first_name_get_error_response():
    auth_token = create_new_user_token_on_success()
    negative_assert(data.kit_body_name_exceeds_limit, auth_token)

def test_create_user_english_letter_in_first_name_get_success_response():
    auth_token = create_new_user_token_on_success()
    positive_assert({"name": " A Aaa "}, auth_token)


def test_create_user_has_special_symbol_in_first_name_get_success_response():
    auth_token = create_new_user_token_on_success()
    positive_assert({"name": "\"№% @\","}, auth_token)



def test_create_user_has_number_in_first_name_get_success_response():
    auth_token = create_new_user_token_on_success()
    positive_assert({"name": "123"}, auth_token)


def test_create_kit_numbers_as_string_in_name_get_success_response():
  auth_token = create_new_user_token_on_success()
  positive_assert({"name": "123"}, auth_token)

def test_create_kit_empty_json_get_error_response():
  auth_token = create_new_user_token_on_success()
  negative_assert({}, auth_token)


def test_create_kit_different_param_type_in_name_get_error_response():
  auth_token = create_new_user_token_on_success()
  negative_assert({"name": 123}, auth_token)
