# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import random
from datetime import datetime

class ActionInformBookedFlightOrNot(Action):

    def name(self) -> Text:
        return "action_inform_booked_flight_or_not"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        random.seed(datetime.now().strftime("%m %d %Y, %H:%M:%S"))
        
        current_destination = tracker.get_slot("destination")

        if not current_destination:
            msg = "I didn't receive any destination. Could you provide me the location again?"
            dispatcher.utter_message(text=msg)
            return []
        
        #Logic for checking Flight availablity
        #Just randomly picks for now
        if random.choice([True,False]):
            #if possible to book a flight:
            #book the flight and inform that you booked the flight
            msg = f"Booking a flight to {current_destination}. Happy travelling!"
            dispatcher.utter_message(text=msg)
            return []
        else:
            #if not possible to book a flight:
            #inform the use that no flights are available
            msg = f"Sorry, no flights available to {current_destination}. \nI could help you with booking flights to other destinations if you want."
            dispatcher.utter_message(text=msg)
            return []
        
