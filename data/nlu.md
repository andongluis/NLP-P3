## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hello
- I'm well
- I'm well. How are you?
- I'm well, thanks
- Good
- I'm doing well
- Doing well
- I'm good

## intent:goodbye
- bye
- goodbye
- see you around
- see you
- that's all

## intent:thank
- thanks
- thank you
- thanks a lot
- awesome thanks
- Thank you
- that's great
- that's what I needed

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- yep
- uh-huh
- Yes

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- nope

## intent:ask_purpose
- who are you
- what are you
- what is your name
- what is this

## intent:ask_options
- what can you do
- give me options
- what are the options
- can I see the options

## intent:give_url
- the url is [https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/](recipe_url)
- the url is [https://www.allrecipes.com/recipe/258170/easy-white-chocolate-ganache/](recipe_url)
- the url is [https://www.allrecipes.com/recipe/33647/chocolate-ganache/](recipe_url)
- the url is [https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/](recipe_url)
- www.allrecipes.com/recipe/12151/banana-cream-pie-i/
- the url is [https://www.allrecipes.com/recipe/12720/grilled-salmon-i/](recipe_url)
- the url is [http://www.allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/](recipe_url)
- the url is [https://www.allrecipes.com/recipe/8302/banana-chocolate-chip-cake/](recipe_url)
- the url is [http://www.allrecipes.com/recipe/59661/spinach-enchiladas/](recipe_url)
- the url is [https://www.allrecipes.com/recipe/216564/swedish-meatballs-svenska-kottbullar/](recipe_url)
- the url is [https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/](recipe_url)
- the url is [https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/](recipe_url)
- url: [https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/](recipe_url)
- url: [https://www.allrecipes.com/recipe/258170/easy-white-chocolate-ganache/](recipe_url)
- url: [https://www.allrecipes.com/recipe/33647/chocolate-ganache/](recipe_url)
- url: [https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/](recipe_url)
- url: [https://www.allrecipes.com/recipe/12720/grilled-salmon-i/](recipe_url)
- url: [http://www.allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/](recipe_url)
- url: [https://www.allrecipes.com/recipe/8302/banana-chocolate-chip-cake/](recipe_url)
- url: [http://www.allrecipes.com/recipe/59661/spinach-enchiladas/](recipe_url)
- url: [https://www.allrecipes.com/recipe/216564/swedish-meatballs-svenska-kottbullar/](recipe_url)
- url: [https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/](recipe_url)
- url: [https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/](recipe_url)
- some-garbage-of-things-that-are-url-like.com
- www.sfsdkljdsliee.com
- [https://www.google.com/](recipe_url)
- [https://www.allrecipes.com/](recipe_url)
- url: [https://www.allrecipes.com/recipe/23600/worlds-best-lasagna](recipe_url)
- [https://www.allrecipes.com/recipe/23600/worlds-best-lasagna](recipe_url)
- [https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/](recipe_url)
- https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/
- https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/

## intent:ask_ingreds
- give me the ingredients
- what are the ingredients
- show ingredients
- ingredients
- Go over ingredients
- ingredient
- go over ingredients

## intent:ask_how_to
- how do you [chop an onion](how_to)
- how to [mince a tomato](how_to)
- how to [chop](how_to)
- how to [crack an egg](how_to)
- how to [cook the steak](how_to)
- how to [sear the beef](how_to)
- how to [puree the parsley](how_to)
- how to [mince garlic](how_to)
- how do I [preheat an over](how_to)
- how do I [peel a banana](how_to)
- how do I [mix the ingredients](how+to)
- How do I [cook pasta](how_to)?
- how to [cook pasta](how_to)
- how do i [cook pasta](how_to)
- how do i [peel onions](how_to)?
- how do i [fry meatballs](how_to)
- how do i [chop an onion](how_to)
- how do i [chop an onion](how_to)

## intent:ask_what_is
- what is [a cucumber](what_is)
- what is [an onion](what_is)
- what are [onions](what_is)
- what is [an oven](what_is)
- What is [butter](what_is)?
- what is [minced garlic](what_is)
- What is [pasta sauce](what_is)?

## intent:ask_steps
- show me the steps
- give me the steps
- what are the steps
- steps
- show steps
- can I see the steps

## intent:ask_next_step
- what is the next step
- next step
- next
- what do I do next
- show me the steps
- what are the steps
- steps
- give me the next step
- step
- Show me the steps
- Give me the next step
- Go over the steps

## intent:ask_prev_step
- what was the previous step
- can you go to the previous step
- previous step please
- take me back a step
- what was the last step
- give me the last step
- previous step

## intent:ask_nth_step
- give me the [6th](step_num) step
- what is the [first](step_num) step
- what is step [1](step_num)

## intent:clarify
- some garbage here that is not super clear what the user is saying
- is bernie sanders the best
- joe biden ate my sandwich
- bloomberg did not get me a lollipop
- can I see that
- what

## regex:recipe_url
- https?:\/\/www.allrecipes.com\/recipe\/\d+\/(.*?)
- https?:\/\/www.allrecipes.com\/recipe\/\d+\/(.*?)\/
