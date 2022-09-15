import json
import pprint
import time

json_file = "acdc.json"


def counter_all_music_time():
    with open(json_file, "r") as some_json_file:
        data = json.load(some_json_file)

        def unpacking_dict():
            album = data["album"]
            tracks = album["tracks"]
            track = tracks['track']

            def counter_time_music():
                counter = 0
                for i in track:
                    music_time = int(i["duration"])
                    counter += music_time

                def conversion_time():
                    ty_res = time.gmtime(counter)
                    res = time.strftime("%H:%M:%S", ty_res)
                    return res
                return conversion_time()
            return counter_time_music()
    return unpacking_dict()


print(counter_all_music_time())

