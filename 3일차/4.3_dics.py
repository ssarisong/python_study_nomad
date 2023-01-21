player = {
    'name': 'sujin',
    'age': 22,
    'alive': True,
    'fav_food': ["🍜", "🍣"]
}
print(player.get('age')) #get(키 값), age 값 출력
print(player.get('fav_food')) #fav_food 값 출력
print(player) #전체 dictionary 출력
player.pop('age') #age를 삭제한 dictionary 출력
print(player) #age를 제외한 dictionary 출력

player['fav_food'].append("🧀") #fav_food 딕셔너리에 치즈 인덱스 추가
print(player.get('fav_food')) 
print(player['fav_food'])