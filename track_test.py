 # Чеснаков Артем 9 кагорта - Финальный проект

import request

current_track = request.track

def test_return_status_code():

    order_response = request.get_order_track(current_track)

    assert order_response.status_code == 200

    if order_response.status_code == 200:
        print("OK")
    else:
        print("ERROR")

