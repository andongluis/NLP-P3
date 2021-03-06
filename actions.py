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

from p2_code import RecipeManager, is_url_valid, merriam_webster_search, _construct_how_to_tutorial


recipe_manager = None

class ActionCheckURL(Action):

    def name(self) -> Text:
        return "action_check_url"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):

        recipe_url = tracker.latest_message['text']

        print(recipe_url)

        global recipe_manager

        recipe_manager = RecipeManager(recipe_url)

        print(recipe_url)
        print(tracker.current_state())
        print(tracker.current_slot_values())

        return_slots = []
        if is_url_valid(recipe_url):
        	print("is valid")
        	validity = True
        	dispatcher.utter_message(text="Url {} is valid".format(recipe_url))

        	return_slots.append(SlotSet("recipe_valid", validity))
        	return_slots.append(SlotSet("step_num", 0))

        else:
        	validity = False
        	print("aint valid")
        	dispatcher.utter_message(text="Url {} is invalid".format(recipe_url))

        	return_slots.append(SlotSet("recipe_valid", validity))

        return return_slots

class ActionIngredList(Action):

    def name(self) -> Text:
        return "action_ingred_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ingred_list = recipe_manager.get_ingreds()

        dispatcher.utter_message(text="\n".join(ing for ing in ingred_list))

        return [SlotSet("ingred_list", ingred_list)]

class ActionNextStep(Action):

    def name(self) -> Text:
        return "action_next_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        step_num = tracker.get_slot("step_num")

        next_step = recipe_manager.get_step(step_num)

        dispatcher.utter_message(text=next_step)

        return [SlotSet("step_num", step_num+1)]

class ActionPrevStep(Action):

    def name(self) -> Text:
        return "action_prev_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



        step_num = tracker.get_slot("step_num")

        next_step = recipe_manager.get_step(step_num-2)

        dispatcher.utter_message(text=next_step)

        return [SlotSet("step_num", step_num-1)]

class ActionNthStep(Action):
    def name(self) -> Text:
            return "action_nth_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        step_num = next(tracker.get_latest_entity_values("step_num"), None) # from Rasa online

        dispatcher.utter_message(text=step_num)

        return [SlotSet("step_num", step_num)]

class ActionHowTo(Action):
    def name(self) -> Text:
            return "action_how_to"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        how_text = next(tracker.get_latest_entity_values("how_to"), None) # from Rasa online
        res = _construct_how_to_tutorial(how_text)

        dispatcher.utter_message(text=res)

        return [SlotSet("what_is", res)]

class ActionWhatIs(Action):
    def name(self) -> Text:
            return "action_what_is"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        what_text = next(tracker.get_latest_entity_values("what_is"), None) # from Rasa online
        res = merriam_webster_search(what_text)

        dispatcher.utter_message(text=res)

        return [SlotSet("what_is", res)]