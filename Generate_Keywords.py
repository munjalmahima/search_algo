from flask import Flask,jsonify,request
from flask_restful import Resource,Api
import nltk 
from nltk.corpus import wordnet 
def Keywords(user_inputs):
    full_forms={'ac':'Air Conditioner','tv':'Television','ro filter':'Reverse Osmosis Filter',
            'ro purifier':'Reverse Osmosis Purifier','sms':'Short Message Service',
            'lcd tv':'Liquid Crystal Display Television','sd card':'Secure Digital Card',
            'pin':'Personal Identification Number','led bulb':'Light Emitting Diode Bulb',
            'led tv':'Light Emitting Diode Television','oled tv':'Organic Light Emitting Diode Television',
            'qled tv':'Quantum Light Emitting Diode Television','lpg cylinder':'Liquefied Petroleum Gas',
            'cng car':'Compressed Natural Gas Car','usb cable':'Universal Serial Bus Cable'}

    diction=['iphone','iphone 11','iphone 6','laptop','dell laptop','buckets','clothes','refrigerator','lg refrigerator',
           'crunchzase','zase','crunch','iphone','air conditioner','alarm clock','answering machine','barbecue grill',
           'bbq grill','blender','blow dryer','burglar alarm','calculator','camera','can opener','cd player',
           'ceiling fan','phone','clock','clothes dryer','clothes washer','coffee grinder','coffee maker',
           'computer','convection oven','copier','crock-pot','curling iron','dishwasher','doorbell','sunglasses',
           'mobile','care','race','end','dine','den','car','samsung mobile','micromax mobile','redmi mobile',
           'apple mobile']
    ignore_words=[' on rent',' available',' for sale',' for rent',' on sale']
    flag=False
    user_inputs=user_inputs.lower()
    for i in ignore_words:
        if i in user_inputs:
            user_input=user_inputs.replace(i,'')
            flag=True
            break
    if(flag==False):
        user_input=user_inputs
    boolean=False
    for k in full_forms:
        if(k==user_input):
            output=full_forms[k]
            return output
            boolean=True
            break
    if boolean==False:
            diction=sorted(diction)
            ans='y'
            constant=3
            count_of_frequency_char=[]
            output=[]
            indexes=[]
            indices=[]
            strings_with_substring=[]
            strings_with_substringi=[string for string in diction if user_input in string]
            temp=list(user_input.split(' '))
            for i in range(len(temp)):
                if temp[i] in diction:
                    strings_with_substring=[string for string in diction if temp[i] in string]
            for mahima in strings_with_substring:
                if(mahima not in strings_with_substringi):
                    strings_with_substringi.append(mahima)
              
            if strings_with_substringi:
                if ' ' in user_input:
                    output=strings_with_substringi
                    return output
                else:
                    output=sorted(strings_with_substringi,key=len)
                    return output
            else:
                set_string2=set(user_input)
                for i in range(len(diction)):
                    if(diction[i][0]==user_input[0]):
                        l=diction[i]
                        length=0
                        length=len(l)
                        if(length<=len(user_input)+constant and length>=len(user_input)-constant):
                            set_string1=set(l)
                            matched=set_string1 & set_string2
                            matched.discard(' ')
                            c=len(matched)
                            count_of_frequency_char.append(c)
                            indexes.append(diction.index(l))
                if count_of_frequency_char:
                    maxi=max(count_of_frequency_char)
                    for me in range(len(count_of_frequency_char)):
                        if(count_of_frequency_char[me]==maxi):
                            indices.append(indexes[me])
                    for i in indices:
                        output.append(diction[i])
                    output=sorted(output,key=len)
                    return output
                else:
                    synonyms=[]
                    for syn in wordnet.synsets(user_input): 
                        for l in syn.lemmas(): 
                            synonyms.append(l.name())
                    o=(set(synonyms))
                    output= list(o)
                    return output
                    if not o:
                        output='Sorry.No valid item found in database.'
                        return 
    
app=Flask(__name__)
api=Api(app)
@app.route("/")
def hello():
    return jsonify({"about":"Generating Keywords"})
Data=[]
name=''
class People(Resource):
    def get(self,name):
        return Keywords(name)
        
api.add_resource(People,'/Name/<string:name>')
    
if __name__=="__main__":
    app.run(debug=True)

