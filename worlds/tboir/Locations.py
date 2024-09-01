import typing
from BaseClasses import Location
from .Names import stage_names, alt_stage_names, room_type_names, disallowed_room_types_per_stage, all_stage_names


class TheBindingOfIsaacRepentanceLocation(Location):
    game: str = "The Binding of Isaac Rebirth"


base_id = 7880000

base_location_table = {
    "Run End": None
}

item_pickups = {
    f"ItemPickup{i + 1}": base_id + i for i in range(0, 500)
}

stage_pickups = {
    f"{v} Item {i + 1}": base_id + i + len(item_pickups) + j * 50 for j, v in
    enumerate(all_stage_names) for i in range(0, 50)
}

room_type_pickups = {
    f"{v} Item {i + 1}": base_id + i + len(item_pickups) + len(stage_pickups) + j * 50 for j, v in
    enumerate(room_type_names) for i in range(0, 50)
}

stage_room_type_pickups = {}

cur_index = base_id + len(item_pickups) + len(stage_pickups) + len(room_type_pickups)
for j, v in enumerate(all_stage_names):
    for j2, v2 in enumerate(room_type_names):
        if v in disallowed_room_types_per_stage and v2 in disallowed_room_types_per_stage[v]:
            continue
        for i in range(0, 50):
            stage_room_type_pickups[f"{v} {v2} Item {i + 1}"] = cur_index
            cur_index += 1


location_table = {**base_location_table, **item_pickups, **stage_pickups, **room_type_pickups,
                  **stage_room_type_pickups}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in location_table.items()}
