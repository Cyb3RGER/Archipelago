from BaseClasses import MultiWorld, CollectionState
from worlds.generic.Rules import set_rule, add_rule


def set_rules(world: MultiWorld, player: int, required_locations: int, progression_item_count: int, required_prog_item_factor: float):
    set_rule(world.get_location("Run End", player),
             lambda state: state.has(f"Progression Item", player,
                                     progression_item_count * required_prog_item_factor) and state.can_reach(
                 world.get_location(f"ItemPickup{required_locations}", player).parent_region))

    world.completion_condition[player] = lambda state: state.has("Victory", player)
