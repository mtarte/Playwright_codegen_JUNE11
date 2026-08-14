import re
# import requests

from api.booking_client import BookingAPIClient
from api.builders import make_booking

# Request
# curl -X POST \
#   https://restful-booker.herokuapp.com/booking \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "firstname" : "Jim",
#     "lastname" : "Brown",
#     "totalprice" : 111,
#     "depositpaid" : true,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-01-01"
#     },
#     "additionalneeds" : "Breakfast"
# }'



def test_create_booking(booking_client:BookingAPIClient):
    playload = make_booking()
    response = booking_client.create_booking(playload)


    # response = requests.post(
    #     "https://restful-booker.herokuapp.com/booking",
    #     json={"firstname" : "Jim",
    #         "lastname" : "Brown",
    #         "totalprice" : 111,
    #         "depositpaid" : True,
    #         "bookingdates" : {
    #             "checkin" : "2018-01-01",
    #             "checkout" : "2019-01-01"
    #         },
    #         "additionalneeds" : "Breakfast"  
    #     },
    #     timeout=10
    # )
    print(response.json())
    # print(response.status_code)
    assert response.status_code == 200
    print(response.json()["bookingid"])
    assert response.json()["bookingid"]

{'bookingid': 2363, 'booking': {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}}




# Response
# HTTP/1.1 200 OK

# {
#     "bookingid": 1,
#     "booking": {
#         "firstname": "Jim",
#         "lastname": "Brown",
#         "totalprice": 111,
#         "depositpaid": true,
#         "bookingdates": {
#             "checkin": "2018-01-01",
#             "checkout": "2019-01-01"
#         },
#         "additionalneeds": "Breakfast"
#     }
# }

