#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:9696/predict'

#row number: 300
#val expected: 54

song = {
  "artists": "callum j wright",
  "album_name": "isn't she lovely (acoustic)",
  "track_name": "isn't she lovely - acoustic",
  "duration_ms": 11.889799,
  "explicit": 0,
  "danceability": 0.69,
  "energy": 0.306,
  "key": 9,
  "loudness": -9.193,
  "mode": 1,
  "speechiness": 0.0356,
  "acousticness": 0.805,
  "instrumentalness": 0.0,
  "liveness": 0.0968,
  "valence": 0.424,
  "tempo": 115.671,
  "time_signature": 4,
  "track_genre": "acoustic"
}

requests.post(url, json=song)

requests.post(url, json=song).json()

response = requests.post(url, json=song).json()

rx = (response['popularity'])
print('The popularity of the song is: ', rx )