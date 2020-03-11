# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from p2_code import RecipeManager, is_url_valid


recipe_manager = None

class ActionCheckURL(Action):

    def name(self) -> Text:
        return "action_check_url"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipe_url = tracker.get_slot("recipe_url")

        print(recipe_url)
        print(tracker.current_state())
        print(tracker.current_slot_values())

        return_slots = []
        if is_url_valid(recipe_url):
        	print("is valid")
        	validity = True
        	dispatcher.utter_message(text="Url {} is valid".format(recipe_url))

        	# Set up recipe_manager
        	recipe_manager = RecipeManager(recipe_url)

        	return_slots.append(SlotSet("recipe_valid", validity))
        	return_slots.append(SlotSet("step_num", 0))

        else:
        	validity = False
        	print("aint valid")
        	dispatcher.utter_message(text="Url {} is invalid".format(recipe_url))

        	return_slots.append(SlotSet("recipe_valid", validity))

        return return_slots