# First install necessary packages

# pip install flask

# Import the modules
from flask import Flask, jsonify, request

# create the app. This variable named jh constains our app'
FOODIE_NEEDY = Flask(__name__)

schools = ['Mahadevi Birla World Academy', ' St.Francis Xavier School', 'Kendriya Vidyalaya Ballygunge']
address = ['17A  Dargah Road,Park Circus,Kolkata-17', 'GA Road, Purbanchal, Phase1 ,Sector 3,Salt Lake City ,Kolkata-97', 'Military Camp,Ballygunge Circular Road, Ballygunge Kolkata-97']
location = ['22.540 , 88.370', '22.573 , 88.406', '22.533 , 88.353']
dropoff = ['9:00am to 11:00am', '7:00 am to 10:30am', '10:00 am to 12:00pm']
pickup = [' 4:00pm to 5:30pm', '3:00pm to 4:30pm', '5:00pm to 7:30pm']


# add routes to our app
@FOODIE_NEEDY.route('/')
def foodie_needy():
    return 'Welcome To Foodie Needy'

@FOODIE_NEEDY.route('/location')
def LOCATION():
    resp = jsonify(location)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@FOODIE_NEEDY.route('/information')
def INFORMATION():
    twod=[]
    for i in range(len(schools)):
        oned=[schools[i],address[i],dropoff[i],pickup[i]]
        twod.append(oned)

    resp = jsonify(twod)
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp
'''

@jh.route('/city/add')
def add_city():
    args = request.args.to_dict()
    name = args['name']
    if len(name) < 3:
        return jsonify(dict(status=False, message='Too short'))
    else:
        data['data'].append(name)
        return 'Added city {}'.format(name)
'''
# This comment a comment
# Run the app if someone runs this file.
if __name__ == "__main__":
    FOODIE_NEEDY.run(debug=True)

# to run call: python filename.py
