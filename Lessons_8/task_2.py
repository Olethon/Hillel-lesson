import json
import pprint
import time


def get_json_data() -> dict:
    """opens a file for reading"""
    with open("acdc.json", "r") as some_json_file:
        data = json.load(some_json_file)
        return data


def count_time_in_tracks(data: dict) -> int:
    """counts the total time in seconds"""
    counter = 0
    for track in data['album']['tracks']['track']:
        counter += int(track["duration"])
    return counter


def convert_time(total_time: int) -> str:
    """converts seconds to time format"""
    ty_res = time.gmtime(total_time)
    return time.strftime("%H:%M:%S", ty_res)


def counter_all_music_time():
    """general function"""
    data = get_json_data()
    total_time = count_time_in_tracks(data)
    return convert_time(total_time)


print(counter_all_music_time())
