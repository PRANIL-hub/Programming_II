def main():
    places = []

    place = input("Place: ")
    while place != "":
        places.append(place.title())
        place = input("Place: ")

    if len(places) == 0:
        print("I went nowhere :(")
    else:
        print("On my holiday, I went to:")
        longest_place = ""
        for place in places:
            print(place)
            if len(place) > len(longest_place):
                longest_place = place
        print(f"The place with the longest name was {longest_place}")
main()
