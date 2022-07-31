from datetime import datetime
from typing import List, Optional
def sum_light(els: List[datetime], start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None) -> int:
    a = els[0]
    print(a)



print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10)))

print(sum_light(els=[
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
    start_watching=datetime(2015, 1, 12, 10, 0, 0),
    end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 7)) == 7)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
    datetime(2015, 1, 12, 10, 0, 3),
    datetime(2015, 1, 12, 10, 0, 10)) == 7)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
    datetime(2015, 1, 12, 10, 0, 10),
    datetime(2015, 1, 12, 10, 0, 20)) == 0)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],
    datetime(2015, 1, 12, 10, 30, 0),
    datetime(2015, 1, 12, 11, 0, 0)) == 0)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],
    datetime(2015, 1, 12, 10, 10, 0),
    datetime(2015, 1, 12, 11, 0, 0)) == 10)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],
    datetime(2015, 1, 12, 10, 10, 0),
    datetime(2015, 1, 12, 11, 0, 10)) == 20)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],
    datetime(2015, 1, 12, 9, 50, 0),
    datetime(2015, 1, 12, 10, 0, 10)) == 10)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],
    datetime(2015, 1, 12, 9, 0, 0),
    datetime(2015, 1, 12, 10, 5, 0)) == 300)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],
    datetime(2015, 1, 12, 11, 5, 0),
    datetime(2015, 1, 12, 12, 0, 0)) == 310)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
],
    datetime(2015, 1, 12, 11, 5, 0),
    datetime(2015, 1, 12, 11, 10, 0)) == 300)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
],
    datetime(2015, 1, 12, 10, 10, 0),
    datetime(2015, 1, 12, 11, 0, 10)) == 20)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
],
    datetime(2015, 1, 12, 9, 10, 0),
    datetime(2015, 1, 12, 10, 20, 20)) == 610)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
],
    datetime(2015, 1, 12, 9, 10, 0),
    datetime(2015, 1, 12, 10, 20, 20)) == 1220)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
],
    datetime(2015, 1, 12, 9, 9, 0),
    datetime(2015, 1, 12, 10, 0, 0)) == 0)

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
],
    datetime(2015, 1, 12, 9, 9, 0),
    datetime(2015, 1, 12, 10, 0, 10)) == 10)