class Room:
    def __init__(self, room_number, price_per_night,  availability_status) -> None:
        self.room_number = room_number
        self.price_per_night = price_per_night
        self._availability_status = availability_status

    def check_availability(self):
        if self._availability_status:
            return True
        
    def set_availability(self, availability_status):
        self._availability_status = availability_status
        print(f"Availability status changed to {availability_status}")

    

    def add_ratings(self,room_type,rating,rating_record={
        "Standard Room":4,
        'Standard Room':3,
        "Standard Room":4,
        'Standard Room':4,
        "Standard Room":4,
        'Standard Room':3,
        'Delux Room':4,
        'Delux Room':4,
        'Delux Room':4,
        'Suite':5,
        'Suite':5,
        'Suite':4
    }):
        try:
            rating_record[room_type] = rating
            print("Rating added")
        except Exception as e:
            print(f"error")

    def get_average_rating(self,room_type,rating_record={
        "Standard Room":4,
        'Standard Room':3,
        "Standard Room":4,
        'Standard Room':4,
        "Standard Room":4,
        'Standard Room':3,
        'Delux Room':4,
        'Delux Room':4,
        'Delux Room':4,
        'Suite':5,
        'Suite':5,
        'Suite':4
    }):
        
        ratings = rating_record.get(room_type, [])
        if not ratings:
            return 0.0  
        return sum(ratings) / len(ratings)
        
        

class Standard_Room(Room):
    def __init__(self, room_number, price_per_night, availability_status, basic_amenities, room_type = 'Standard Room') -> None:
        super().__init__(room_number, price_per_night, availability_status)
        
        self.room_type = room_type
        self.basic_amineties = basic_amenities

    


class Deluxe_Room(Room):
    def __init__(self, room_number, price_per_night, availability_status, additional_amineties, minibar, room_type = 'Deluxe Room') -> None:
        super().__init__(room_number, price_per_night, availability_status)
        self.additional_amineties = additional_amineties
        self.minibar = minibar
        self.room_type = room_type


class Suite(Room):
    def __init__(self, room_number, price_per_night, availability_status, additional_amineties, minibar,  personal_buttler_service,luxary_aminites,room_type = 'Suite') -> None:
        super().__init__(room_number, price_per_night, availability_status)
        self.additional_amineties = additional_amineties
        self.luxary_amineties = luxary_aminites
        self.minibar = minibar
        self.room_type = room_type
        self.personal_buttler_service =personal_buttler_service



room1 = Standard_Room(room_number=1, price_per_night=500, availability_status=1, basic_amenities="keyless entry")

if room1.check_availability():
    print("It is available")

else:
    print("Not available")


print(f"The amineties in {room1.room_type} are: {room1.basic_amineties}")
room1.add_ratings('Standard Room', 5)

avg = room1.get_average_rating("Standard Room")
print(avg)



