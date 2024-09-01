import logging
import string
from collections import Counter

from BaseClasses import Region, Entrance, Item, MultiWorld, Tutorial, ItemClassification, CollectionState
from worlds.AutoWorld import World, WebWorld
from .Items import TheBindingOfIsaacRepentanceItem, item_table, default_weights, default_junk_items_weights, \
    default_trap_items_weights, collectible_items
from .Locations import location_table, TheBindingOfIsaacRepentanceLocation, base_location_table
from .Options import IsaacOptions, ItemWeights
from .Names import stage_names, alt_stage_names, StageNames, RoomTypes, room_type_names, \
    disallowed_room_types_per_stage, all_stage_names
from .Rules import stage_progressive_connections, goal_stage_mapping, alt_stage_progressive_connections, \
    alt_stage_vanilla_connections, stage_vanilla_connections, alt_stage_non_progressive_connections
from ..generic.Rules import set_rule, add_rule


class TheBindingOfIsaacRepentanceWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the The Binding Of Isaac Repentance integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cyb3R"]
    )]


class TheBindingOfIsaacRepentanceWorld(World):
    """
    The Binding of Isaac: Rebirth is a randomly generated action RPG shooter with heavy Rogue-like elements.
    Following Isaac on his journey players will find bizarre treasures that change Isaac’s form giving him super
    human abilities and enabling him to fight off droves of mysterious creatures, discover secrets and fight his way
    to safety.
    """
    game = "The Binding of Isaac Repentance"
    options_dataclass = IsaacOptions
    options: IsaacOptions
    topology_present = False

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = location_table
    item_name_groups = {
        "Any Progression": [name for name, data in item_table.items() if data.is_progression() and data.id is not None]}

    web = TheBindingOfIsaacRepentanceWeb()

    total_locations: int = 0
    required_locations: int = 0
    collectible_item_count: int = 0
    trap_item_count: int = 0
    filler_item_count: int = 0
    required_prog_item_factor: float = 0.6
    location_counts: dict[str, int | dict[str, int]] = {}
    room_type_loc_amounts: dict[str, int] = {}

    def generate_early(self) -> None:
        if not self.multiworld.player_name[self.player].isalnum():
            logging.warning(f"The name {self.multiworld.player_name[self.player]} for a TBoI world contains "
                            f"non-alphanumerical characters. You are not guaranteed to be able to enter the name "
                            f"ingame and may have to edit the games savefile to connect.")
        if self.options.required_locations.value > self.options.total_locations.value:
            self.options.total_locations.value = self.options.required_locations.value

        self.room_type_loc_amounts = {
            RoomTypes.Treasure: self.options.location_amount_treasure.value,
            RoomTypes.Shop: self.options.location_amount_shop.value,
            RoomTypes.Boss: self.options.location_amount_boss.value,
            RoomTypes.Secret: self.options.location_amount_secret.value,
            RoomTypes.Devil: self.options.location_amount_devil.value,
            RoomTypes.Angel: self.options.location_amount_angel.value,
            RoomTypes.Planetarium: self.options.location_amount_planetarium.value,
            RoomTypes.Other: self.options.location_amount_other.value
        }

        self.location_counts = {}
        self.total_locations = self.options.total_locations.value
        self.required_locations = self.options.required_locations.value
        if self.options.locations_by_stage.value == 1:
            stages = all_stage_names if self.options.include_alt_stage_locations.value == 1 else stage_names
            locs_per_stage = self.total_locations // len(stages)
            leftover_locs = self.total_locations - locs_per_stage * len(stages)
            for stage in stages:
                locs_this_stage = locs_per_stage
                if leftover_locs > 0:
                    locs_this_stage += 1
                    leftover_locs -= 1
                if self.options.locations_by_room_type == 1:
                    disallowed_room_types = disallowed_room_types_per_stage[
                        stage] if stage in disallowed_room_types_per_stage else []
                    room_type_loc_amounts_stage = {
                        k: v for k, v in self.room_type_loc_amounts.items() if k not in disallowed_room_types
                    }
                    picks = self.random.choices([k for k, _ in room_type_loc_amounts_stage.items()],
                                                weights=[v for _, v in room_type_loc_amounts_stage.items()],
                                                k=locs_this_stage)
                    self.location_counts[f"{stage}"] = {f"{k}": v for k, v in Counter(picks).items()}

                else:
                    # ToDo: check
                    self.location_counts[f"{stage}"] = locs_this_stage

            assert sum([v if v is int else sum([v2 for _, v2 in v.items()]) for _, v in
                        self.location_counts.items()]) == self.total_locations
            # self.required_locations = self.total_locations
        elif self.options.locations_by_room_type.value != 0:
            #ToDo: check
            self.location_counts[f"{StageNames.Basement1}"] = {}
            self.location_counts[f"{StageNames.Basement2}"] = {}
            for k, v in self.room_type_loc_amounts.items():
                if k in disallowed_room_types_per_stage[StageNames.Basement1]:
                    self.location_counts[f"{StageNames.Basement2}"][f"{k}"] = v
                else:
                    self.location_counts[f"{StageNames.Basement1}"][f"{k}"] = v

        self.collectible_item_count = self.options.collectible_amount.value
        if self.collectible_item_count > self.total_locations:
            self.collectible_item_count = self.total_locations
        self.filler_item_count = self.total_locations - self.collectible_item_count
        if self.options.stage_unlocks.value == 1:
            if self.filler_item_count > 11:
                self.filler_item_count -= 11
            else:
                self.collectible_item_count -= 11
            if self.options.include_alt_stage_unlocks == 1:
                if self.filler_item_count > 8:
                    self.filler_item_count -= 8
                else:
                    self.collectible_item_count -= 8

        self.trap_item_count = round(
            self.filler_item_count * (self.options.trap_percentage.value / 100))
        self.filler_item_count = self.filler_item_count - self.trap_item_count

    def create_items(self):
        # Generate item pool
        itempool = []

        if self.options.stage_unlocks.value == self.options.stage_unlocks.option_progressive:
            itempool += ["Progressive Stage Unlock"] * 11
            if self.options.include_alt_stage_unlocks:
                itempool += ["Progressive Alt. Stage Unlock"] * 8

        assert self.collectible_item_count >= 20
        if self.options.item_weights.value == ItemWeights.option_custom:
            item_weights = {name: val for name, val in self.options.custom_item_weights.value.items()}
        else:
            item_weights = default_weights

        # Fill collectable items
        itempool += self.random.choices(list(item_weights.keys()), weights=list(item_weights.values()),
                                        k=self.collectible_item_count)

        trap_weights = {name: val for name, val in self.options.trap_item_weights.value.items()}
        junk_weights = {name: val for name, val in self.options.custom_junk_item_weights.value.items()}

        # Fill traps
        itempool += self.random.choices(list(trap_weights.keys()), weights=list(trap_weights.values()),
                                        k=self.trap_item_count)

        # Fill remaining items with randomly generated junk
        itempool += self.random.choices(list(junk_weights.keys()), weights=list(junk_weights.values()),
                                        k=self.filler_item_count)

        assert len(itempool) == self.total_locations

        # Convert itempool into real items
        itempool = list(map(lambda name: self.create_item(name), itempool))

        self.multiworld.itempool += itempool

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        if self.options.stage_unlocks.value == 0 and self.options.locations_by_stage.value == 0:
            # ToDo: what to do with location by room type here?
            set_rule(self.multiworld.get_location("Run End", self.player),
                     lambda state: state.has(f"Progression Collectible", self.player,
                                             self.collectible_item_count * self.required_prog_item_factor) and state.can_reach(
                         self.multiworld.get_location(f"ItemPickup{self.options.required_locations.value}",
                                                      self.player).parent_region))
        else:
            goal_stages = goal_stage_mapping[self.options.goal.value]
            # setup start connections
            self.multiworld.get_entrance("New Run", self.player).connect(
                self.multiworld.get_region(StageNames.Basement1, self.player))
            # setup goal connections
            for v in goal_stages:
                self.connect_regions(v, "Run End")

            # "vanilla" connections
            for region, exits in stage_vanilla_connections.items():
                for conn_data in exits:
                    self.connect_regions(region, conn_data[0],
                                         None if conn_data[1] is None else conn_data[1](self.player))
            for region, exits in alt_stage_vanilla_connections.items():
                for conn_data in exits:
                    self.connect_regions(region, conn_data[0],
                                         None if conn_data[1] is None else conn_data[1](self.player))
            # stage unlock connections
            if self.options.stage_unlocks.value == 1:
                for region, exits in stage_progressive_connections.items():
                    for conn_data in exits:
                        self.combine_connections(region, conn_data[0],
                                                 None if conn_data[1] is None else conn_data[1](self.player))
                if self.options.include_alt_stage_unlocks.value == 1:
                    for region, exits in alt_stage_progressive_connections.items():
                        for conn_data in exits:
                            self.combine_connections(region, conn_data[0],
                                                     None if conn_data[1] is None else conn_data[1](self.player))
                else:
                    for region, exits in alt_stage_non_progressive_connections.items():
                        for conn_data in exits:
                            self.combine_connections(region, conn_data[0],
                                                     None if conn_data[1] is None else conn_data[1](self.player))

    def create_regions(self):
        total_locations = self.total_locations
        self.multiworld.regions += [
            self.create_region("Menu", None, ["New Run"]),
            self.create_region("Run End", ["Run End"], None),
        ]
        self.multiworld.get_location("Run End", self.player).place_locked_item(
            TheBindingOfIsaacRepentanceItem("Victory", ItemClassification.progression, None, self.player))
        # ToDo: should this just use the other regions as well!?
        if self.options.locations_by_stage == 0 and self.options.locations_by_room_type == 0:
            # setup regions
            locations_per_section = 25
            num_of_sections = total_locations // locations_per_section
            if total_locations / locations_per_section == num_of_sections:
                num_of_sections -= 1
            num_of_sections += 1
            assert num_of_sections > 1
            for i in range(num_of_sections):
                # ToDo: locations by options (get_locations_for_section)
                locations = [f"ItemPickup{n}" for n in
                             range(i * locations_per_section + 1,
                                   min(total_locations + 1, (i + 1) * locations_per_section + 1))]
                if i == num_of_sections - 1:
                    locations += [location for location in base_location_table]
                self.multiworld.regions.append(self.create_region(f"Run Section {i + 1}", locations))

            # setup connections, ToDo: move to set_rules
            self.multiworld.get_entrance("New Run", self.player).connect(
                self.multiworld.get_region("Run Section 1", self.player))
            for i in range(1, num_of_sections):
                needed = round(i * ((self.collectible_item_count * self.required_prog_item_factor) / (
                        (2 - ((i - 1) / (num_of_sections - 1))) * num_of_sections)))
                self.connect_regions(f"Run Section {i}", f"Run Section {i + 1}",
                                     lambda state, n=needed: state.has(f"Progression Collectible", self.player, n))
        if self.options.stage_unlocks.value > 0:
            stages = stage_names + alt_stage_names
            # setup regions
            for v in stages:
                locations = self.get_locations_for_stage(v)
                # self.item_counts[f"{v}"] = len(locations)
                self.multiworld.regions.append(self.create_region(f"{v}", locations))

    def get_locations_for_stage(self, stage):
        if self.options.locations_by_stage.value == 1:
            if self.options.locations_by_room_type.value == 0:
                return [f"{stage} Item {i + 1}" for i in range(self.location_counts[f"{stage}"])]
            else:
                locs = []
                for k, v in self.location_counts[f"{stage}"].items():
                    locs += [f"{stage} {k} Item {i + 1}" for i in range(v)]
                return locs
        elif self.options.locations_by_room_type.value == 1:
            return [f"{k} Item {i + 1}" for k, v in self.location_counts[f"{stage}"].items() for i in range(v)]
        else:
            # ToDo: figure out what to do with locs_by_stage == 0 and locations_by_room_type == 0 but unlock stages?
            #  Use stages and place all ItemPickup locs except the goal on Basement I??
            assert False, "NYI"

    def connect_regions(self, source_region_name, target_region_name, access_rule=None):
        source_region = self.multiworld.get_region(source_region_name, self.player)
        target_region = self.multiworld.get_region(target_region_name, self.player)
        connection = Entrance(self.player, f"From {source_region.name} To {target_region.name}", source_region)
        if access_rule is not None:
            connection.access_rule = access_rule
        source_region.exits.append(connection)
        connection.connect(target_region)

    def combine_connections(self, source_region_name, target_region_name, access_rule=None):
        connection = self.multiworld.get_entrance(f"From {source_region_name} To {target_region_name}", self.player)
        add_rule(connection, access_rule)

    def create_region(self, name: str, locations=None, exits=None):
        ret = Region(name, self.player, self.multiworld)
        ret.world = self
        if locations:
            for location in locations:
                loc_id = location_table[location]
                location = TheBindingOfIsaacRepentanceLocation(self.player, location, loc_id, ret)
                ret.locations.append(location)
        if exits:
            for _exit in exits:
                ret.exits.append(Entrance(self.player, _exit, ret))

        return ret

    def fill_slot_data(self):
        return {
            "stageUnlocks": self.options.stage_unlocks.value,
            "includeAltStageUnlocks": self.options.include_alt_stage_unlocks.value,
            "includeAltStageLocations" :self.options.include_alt_stage_locations.value,
            "locationsByStage": self.options.locations_by_stage.value,
            "locationsByRoomType": self.options.locations_by_room_type.value,
            "locationCounts": self.location_counts,
            "itemPickupStep": self.options.item_pickup_step.value,
            "seed": "".join(self.random.choice(string.digits) for _ in range(16)),
            "totalLocations": self.total_locations,
            "requiredLocations": self.required_locations,
            "goal": self.options.goal.value,
            "additionalBossRewards": self.options.additional_boss_rewards.value,
            "deathLink": self.options.death_link.value,
            "teleportTrapCanError": self.options.teleport_trap_can_error.value,
            "fullNoteAmount": self.options.full_note_amount.value,
            "noteMarksAmount": self.options.note_marks_amount.value,
            "noteMarkRequireHardMode": self.options.note_marks_require_hard_mode.value,
            "splitStartItems": self.options.split_start_items.value
        }

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = TheBindingOfIsaacRepentanceItem(name, item_data.classification, item_data.id, self.player)
        return item

    def collect_item(self, state: "CollectionState", item: "Item", remove: bool = False):
        if item.advancement and item.code and item.name in collectible_items.keys():
            return "Progression Collectible"

        return super(TheBindingOfIsaacRepentanceWorld, self).collect_item(state, item, remove)

    def generate_output(self, output_directory: str) -> None:
        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player),
                          f"{output_directory}\\world_{self.multiworld.seed_name}_P{self.player}.puml")
