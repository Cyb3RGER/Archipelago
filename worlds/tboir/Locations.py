from BaseClasses import Location
import typing

class TheBindingOfIsaacRebirthLocation(Location):
    game: str = "The Binding of Isaac Rebirth"


base_location_table = {
    "Victory": None,
}

item_pickups = {
    f"ItemPickup{i}": 78000+i for i in range(0, 500)
}

location_table = {**base_location_table, **item_pickups}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in location_table.items()}