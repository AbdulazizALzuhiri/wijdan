# share me: https://replit.com/join/tgnxbbfctc-malgz
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import initialize_app
from typing import List

creds = credentials.Certificate("./wijbase-service-account.json")
app = initialize_app(creds)

db = firestore.client()

fields_coll = db.collection('user-interface').document('fields').collection(
  'meta')


def make_field(name: str, valuetype: str, defaultVal: str, options: list(),
               required: bool, applicable_for: list(), weight: int):
  field = {
    'name': name,
    'value_type': valuetype,
    'default_value': defaultVal,
    'applicable_for': applicable_for,
    'required': required,
    'options': options,
    'weight': weight
  }

  return (field, name.lower().replace(' ', '_'))


# f = make_field(
#   name='Age Range',
#   valuetype='single-option',
#   defaultVal='',
#   options=['18-24', '25-34', '35-44', '45-54', '55-64', '65 or older'],
#   applicable_for=['vid', 'vp'],
#   weight=1,
#   required=True)

# print(f[0])

#fields_coll.document(f[1]).set(f[0])

# doc = fields_coll.get()
# newdoc = doc.to_dict().update({'sensitive': True})


def make_fields():
  fields = []
  fields.append(
    make_field(name='Language',
               valuetype='single-option',
               defaultVal='',
               options=['Arabic', 'English'],
               applicable_for=['vid', 'vp'],
               weight=1,
               required=False))

  fields.append(
    make_field(name='Birth Date',
               valuetype='date',
               defaultVal='',
               options=[],
               applicable_for=['vp'],
               weight=2,
               required=True))

  fields.append(
    make_field(name='Residence Location',
               valuetype='string',
               defaultVal='',
               options=[],
               applicable_for=['vp'],
               weight=3,
               required=True))

  fields.append(
    make_field(name='Family Order',
               valuetype='digit',
               defaultVal='0',
               options=[],
               applicable_for=['vp'],
               weight=4,
               required=False))

  fields.append(
    make_field(name='Education',
               valuetype='single-option',
               defaultVal='',
               options=[
                 'Pre-High School', 'High School', 'Diploma', 'Bachelor',
                 'Master', 'PhD'
               ],
               applicable_for=['vp'],
               weight=5,
               required=True))

  fields.append(
    make_field(name='Occupation',
               valuetype='string',
               defaultVal='',
               options=[],
               applicable_for=['vp'],
               weight=6,
               required=True))

  fields.append(
    make_field(name='Networth',
               valuetype='single-option',
               defaultVal='',
               options=[
                 'Less than 10,000 SAR', '10,000 - 50,000 SAR',
                 '50,000 - 100,000 SAR', '100,000 - 500,000 SAR',
                 '500,000 - 1,000,000 SAR', 'above 1mil'
               ],
               applicable_for=['vp'],
               weight=7,
               required=True))

  fields.append(
    make_field(name='List of Favorite Books',
               valuetype='array',
               defaultVal='',
               options=[],
               applicable_for=['vp'],
               weight=8,
               required=True))

  fields.append(
    make_field(name='List of Favorite Music Genres',
               valuetype='array',
               defaultVal='',
               options=[],
               applicable_for=['vp'],
               weight=9,
               required=True))

  fields.append(
    make_field(name='Favorite Sports Teams',
               valuetype='array',
               defaultVal='',
               options=[],
               applicable_for=['vp'],
               weight=10,
               required=True))

   return fields

#fs = make_fields()


#for f in fs:
 # fields_coll.document(f[1]).set(f[0])
