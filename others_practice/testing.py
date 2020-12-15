def exception_handling():
    car = {'make': 'bmw', 'model': '550i', 'year': '2018'}

    try:
        print(car['colour'])
    except KeyError as msg:
        print('Invalid Key', msg)
    finally:
        print('Go Home!')

exception_handling()
