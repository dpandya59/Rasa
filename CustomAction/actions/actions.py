# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#

class ActionSearchBus(Action):

    def name(self) -> Text:
        return "action_search_bus"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return  ["from_loc","to_loc"]

    def slot_mapping(self) -> Dict[Text,Any]:
        return{"from_loc": self.from_entity(entity="from_location"),
                "to_loc":  self.from_entity(entity="to_location")
        }
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots  =   ["fromloc","toloc"]

        for slot in required_slots:
            if tracker.slots.get(slot)==None:
                return [SlotSet("RequestedSlot")]

        dispatcher.utter_message("Searching for Bus from "+tracker.get_slot("fromloc")+" to "+tracker.get_slot("toloc")
                                )
        return []

class ActionSubmitBusDetails(Action):
    def name(self)  ->  Text:
        return "action_submit_bus_details"
    
    def run(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any],
            ) -> List[Dict]:

        lcFromLoc = tracker.get_slot("fromloc")
        lcToLoc = tracker.get_slot("toloc")
        lcMessage = (f"Searching for bus from {lcFromLoc} to {lcToLoc}")
        dispatcher.utter_message(lcMessage)
        return []
