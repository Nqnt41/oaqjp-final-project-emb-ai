import requests, json
from flask import Flask, request, jsonify, make_response

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)

    formatted_response = json.loads(response.text)

    emotion = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotion['anger']
    disgust = emotion['disgust']
    fear = emotion['fear']
    joy = emotion['joy']
    sadness = emotion['sadness']

    curr_max = anger
    curr_emotion = 'anger'

    if (disgust > curr_max):
        curr_max = disgust
        curr_emotion = 'disgust'
    if (fear > curr_max):
        curr_max = fear
        curr_emotion = 'fear'
    if (joy > curr_max):
        curr_max = joy
        curr_emotion = 'joy'
    if (sadness > curr_max):
        curr_max = sadness
        curr_emotion = 'sadness'    

    dominant_emotion = curr_emotion

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
