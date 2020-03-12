## invalid recipe
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "some-garbage-of-weird-things.com"}
  - action_check_url
  - slot{"recipe_valid": false}
  - utter_ask_url
* goodbye
  - utter_goodbye


## valid recipe
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
  - action_check_url
  - slot{"recipe_valid": true}
  - slot{"step_num": 0}
  - utter_options

## ask ingred
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
  - action_check_url
  - slot{"recipe_valid": true}
  - slot{"step_num": 0}
  - utter_options
* ask_ingreds
  - action_ingred_list
  - slot{"ingred_list": "[banana]"} <!-- not sure how to put ingred list here -->
* ask_what_is{"what is": "banana"}
  - action_what_is

## say welcome
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
  - action_check_url
  - slot{"recipe_valid": true}
  - slot{"step_num": 0}
  - utter_options
* ask_ingreds
  - action_ingred_list
  - slot{"ingred_list": "[banana]"} <!-- not sure how to put ingred list here -->
* ask_what_is{"what is": "banana"}
  - action_what_is
* thanks
  - utter_youre_welcome
  
## ask next step
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
  - action_check_url
  - slot{"recipe_valid": true}
  - slot{"step_num": 0}
  - utter_options
* ask_next_step
  - action_next_step


## ask previous step
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
  - action_check_url
  - slot{"recipe_valid": true}
  - slot{"step_num": 0}
  - utter_options
* ask_next_step
  - action_next_step
* ask_prev_step
  - action_prev_step

## ask nth step
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
  - action_check_url
  - slot{"recipe_valid": true}
  - slot{"step_num": 0}
  - utter_options
* ask_nth_step{"step_num": "2"}
  - action_nth_step

## say goodbye
* greet
  - utter_greet
* ask_purpose
  - utter_purpose
  - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
  - action_check_url
  - slot{"recipe_valid": true}
  - slot{"step_num": 0}
  - utter_options
* ask_nth_step{"step_num": "2"}
  - action_nth_step
* goodbye
  - utter_goodbye