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
* thank
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
## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_ingreds
    - action_ingred_list

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_ingreds
    - action_ingred_list

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_ingreds
    - action_ingred_list
    - slot{"ingred_list": ["¾ cup white sugar", "⅓ cup all-purpose flour", "¼ teaspoon salt", "2 cups milk", "3  egg yolks, beaten", "2 tablespoons butter", "1 ¼ teaspoons vanilla extract", "1 (9 inch) baked pastry shell, cooled", "4  bananas, sliced"]}
* thank
    - utter_youre_welcome
* ask_what_is{"what_is": "butter"}
    - slot{"what_is": "butter"}
    - action_what_is

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna"}
    - action_check_url
    - slot{"recipe_valid": false}
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_ingreds
    - action_ingred_list
    - slot{"ingred_list": ["1 pound sweet Italian sausage", "¾ pound lean ground beef", "½ cup minced onion", "2 cloves garlic, crushed", "1 (28 ounce) can crushed tomatoes", "2 (6 ounce) cans tomato paste", "2 (6.5 ounce) cans canned tomato sauce", "½ cup water", "2 tablespoons white sugar", "1 ½ teaspoons dried basil leaves", "½ teaspoon fennel seeds", "1 teaspoon Italian seasoning", "1 ½ teaspoons salt, divided, or to taste", "¼ teaspoon ground black pepper", "4 tablespoons chopped fresh parsley", "12  lasagna noodles", "16 ounces ricotta cheese", "1  egg", "¾ pound mozzarella cheese, sliced", "¾ cup grated Parmesan cheese"]}

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna"}

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna"}
    - action_check_url
    - slot{"recipe_valid": false}

## interactive_story_1
* greet
    - utter_greet

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_ingreds
    - action_ingred_list
    - slot{"ingred_list": ["¾ cup white sugar", "⅓ cup all-purpose flour", "¼ teaspoon salt", "2 cups milk", "3  egg yolks, beaten", "2 tablespoons butter", "1 ¼ teaspoons vanilla extract", "1 (9 inch) baked pastry shell, cooled", "4  bananas, sliced"]}
* ask_next_step
    - action_next_step
    - slot{"step_num": 1}
* ask_next_step
    - action_next_step
    - slot{"step_num": 2}
* ask_next_step
    - action_next_step
    - slot{"step_num": 3}
* ask_next_step
    - action_next_step
    - slot{"step_num": 4}

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_next_step
    - action_next_step
    - slot{"step_num": 1}
* ask_next_step
    - action_next_step
    - slot{"step_num": 2}
* ask_prev_step
    - action_prev_step
    - slot{"step_num": 1}

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_next_step
    - action_next_step
    - slot{"step_num": 1}
* ask_next_step
    - action_next_step
    - slot{"step_num": 2}
* ask_prev_step
    - action_prev_step
    - slot{"step_num": 1}

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - slot{"recipe_url": "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"}
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_next_step
    - action_next_step
    - slot{"step_num": 1}
    - utter_suggest_next_step
* affirm
    - action_next_step
    - slot{"step_num": 2}
    - utter_suggest_next_step
* affirm
    - action_next_step
    - slot{"step_num": 3}
    - utter_suggest_next_step
* affirm
    - utter_suggest_next_step
* affirm
    - action_next_step
    - slot{"step_num": 4}
    - utter_suggest_next_step
* affirm
    - action_next_step
    - slot{"step_num": 5}

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url
    - action_check_url

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url
    - action_check_url

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_next_step
    - action_next_step
    - slot{"step_num": 1}

## interactive_story_2
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_steps
    - action_next_step
    - slot{"step_num": 1}
* ask_what_is{"what_is":"butter"}
  - action_what_is
* thank
  - utter_youre_welcome

## interactive_story_1
* greet
    - utter_greet
* greet
    - utter_purpose
    - utter_ask_url
* give_url
    - action_check_url
    - slot{"recipe_valid": true}
    - slot{"step_num": 0}
    - utter_options
* ask_ingreds
    - action_ingred_list
    - slot{"ingred_list": ["12 whole wheat lasagna noodles", "1 pound lean ground beef", "2 cloves garlic, chopped", "1/2 teaspoon garlic powder", "1 teaspoon dried oregano, or to taste", "salt and ground black pepper to taste", "1 (16 ounce) package cottage cheese", "2 eggs", "1/2 cup shredded Parmesan cheese", "1 1/2 (25 ounce) jars tomato-basil pasta sauce", "2 cups shredded mozzarella cheese"]}
* ask_what_is{"what_is": "pasta sauce"}
    - slot{"what_is": "pasta sauce"}
    - action_what_is
    - slot{"what_is": "We could not find a Merriam-Webster definition for 'pasta sauce'.\nInstead, we will look up each word individually.\npasta: paste in processed form (such as macaroni) or in the form of fresh dough (such as ravioli)\nsauce: a condiment or relish for food\n"}
* ask_next_step
    - action_next_step
    - slot{"step_num": 1}
    - utter_suggest_next_step
* affirm
    - action_next_step
    - slot{"step_num": 2}
    - utter_suggest_next_step
* affirm
    - action_next_step
    - slot{"step_num": 3}
    - utter_suggest_next_step
* affirm
    - action_next_step
    - slot{"step_num": 4}
    - utter_suggest_next_step
* ask_how_to{"how_to": "cook pasta"}
    - slot{"how_to": "cook pasta"}
    - action_how_to

## interactive_story_1
* ask_how_to{"how_to": "cook pasta"}
    - slot{"how_to": "cook pasta"}
    - action_how_to

## interactive_story_1
* ask_how_to{"how_to": "cook pasta"}
    - slot{"how_to": "cook pasta"}
    - action_how_to

## interactive_story_1
* ask_how_to{"how_to": "peel onions"}
    - slot{"how_to": "peel onions"}
    - action_how_to

## interactive_story_1
* ask_how_to{"how_to": "fry meatballs"}
    - slot{"how_to": "fry meatballs"}
    - action_how_to

## interactive_story_1
* ask_how_to{"how_to": "chop an onion"}
    - slot{"how_to": "chop an onion"}
    - action_how_to
    - slot{"what_is": "Check out this tutorial: /watch?v=dCGS067s0zo"}

## interactive_story_1
* ask_how_to{"how_to": "chop an onion"}
    - slot{"how_to": "chop an onion"}
    - action_how_to
    - slot{"what_is": "Check out this tutorial: https://www.youtube.com//watch?v=dCGS067s0zo"}

## interactive_story_1
* greet
    - utter_greet
