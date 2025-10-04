import random
from mountains import apsan, palgongsan, biseulsan


class TouristInfo:
    def __init__(self, places):
        self.places = places

    def show_all_places(self):
        for place in self.places:
            print(f"산 명칭: {place['name']}")
            print(f"한자: {place.get('hanja', '정보 없음')}")
            print(f"위치: {place.get('locate', '정보 없음')}")
            print("-" * 30)

    def show_random_place(self):
        place = random.choice(self.places)
        print(f"산 명칭: {place['name']}")
        print(f"한자: {place.get('hanja', '정보 없음')}")
        print(f"위치: {place.get('locate', '정보 없음')}")


# 예제 사용법
daegu_tourist_spots = apsan + palgonsan + biseulsan
tour = TouristInfo(daegu_tourist_spots)

print("대구의 관광지 전체 보기:")
tour.show_all_places()

print("\n무작위 관광지 정보:")
tour.show_random_place()
