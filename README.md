# NLP-P3
CS337 Project 3

The goal of Project 3 is to create a (basic) conversational interface for interacting with Project 2.

Here's an illustrative user story comprising a set of user utterances and suitable bot responses:


## <USER STORY>

User: Walk me through a recipe from AllRecipes.com.

Bot: Sure. Please specify a URL.

User: https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/ (Links to an external site.)

Bot: Alright. So let's start working with "Classic and Simple Meat Lasagna." What do you want to do?

Bot: [1] Go over ingredients list or [2] Go over recipe steps.

User: 2.

Bot: The 1st step is: Preheat oven to 350 degrees F (175 degrees C).

User: How do I preheat the oven?

Bot: No worries. I found a reference for you: https://www.youtube.com/results?search_query=how+to+preheat+oven (Links to an external site.)

User: Thanks!

Bot: Should I continue to the 2nd step?

User: Show me the ingredients list.

Bot: Here are the ingredients for "Classic and Simple Meat Lasagna":

12 whole wheat lasagna noodles

1 pound lean ground beef

(...)

1 1/2 25 ounce jars tomato-basil pasta sauce

2 cups mozzarella cheese, shredded

User: Thanks again!

Bot: Should I continue to the 2nd step?

User: Yes, please.

Bot: (...)

</USER STORY>

 

Basic goals:

Recipe retrieval and display (see example above, including "Show me the ingredients list");
Navigation utterances ("Go back one step", "Go to the next step", "Take me to the 1st step", "Take me to the n-th step");
Simple "how to" questions ("How do I <technique being mentioned>?");
Simple "what is" questions ("What is a <tool being mentioned>?");
Name your bot :)
 

The typical solution for this project runs on terminal/console, just as in Project 2, and that's perfectly fine. However, there's a number of extra credit opportunities available if you design and deploy your conversational interface using Rasa (Links to an external site.) (references further below).