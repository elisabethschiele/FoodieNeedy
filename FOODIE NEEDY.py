# First install necessary packages

# pip install flask

# Import the modules
from flask import Flask, jsonify, request

# create the app. This variable named jh constains our app'
FOODIE_NEEDY = Flask(__name__)

schools = ['ABC SCHOOL', 'DEF SCHOOL', 'GHI SCHOOL']
address = ['2B, BALLYGUNGE ROAD,KOLKATA-32', '5F, PARK STREET,KOLKATA-17', '18D,BEHALA ROAD,KOLKATA-56']
location = ['22.533,88.366', '22.576,88.350', '22.498,88.310']
time = ['8am-9am', '10am-11am', '7am-8am']


# add routes to our app
@FOODIE_NEEDY.route('/')
def foodie_needy():
    return 'Welcome To Foodie Needy'

@FOODIE_NEEDY.route('/location')
def LOCATION():
    return jsonify(location)


@FOODIE_NEEDY.route('/information')
def INFORMATION():
    twod=[]
    for i in range(len(schools)):
        oned=[schools[i],address[i],time[i]]
        twod.append(oned)
    return jsonify(twod)
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
