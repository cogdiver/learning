from ksql import KSQLAPI


def mod1():
    rows = [
        {
            'profileId': 'c2309eec',
            'latitude': 37.7877,
            'longitude': -122.4205
        },
        {
            'profileId': '18f4ea86',
            'latitude': 37.3903,
            'longitude': -122.0643
        },
        {
            'profileId': '4ab5cbad',
            'latitude': 37.3952,
            'longitude': -122.0813
        },
        {
            'profileId': '8b6eae59',
            'latitude': 37.3944,
            'longitude': -122.0813
        },
        {
            'profileId': '4a7c7b41',
            'latitude': 37.4049,
            'longitude': -122.0822
        },
        {
            'profileId': '4ddad000',
            'latitude': 37.7857,
            'longitude': -122.4011
        }
    ]
    
    client = KSQLAPI('http://localhost:8088')
    client.ksql('show tables')
    client.inserts_stream('riderLocations', rows)
    result = client.query('select * from currentLocation EMIT CHANGES;')
    try:
        for r in result:
            print(r)
    except:
        pass
    finally:
        result.close()
    print('1')
