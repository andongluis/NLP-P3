# NLP-P3

This is our interactive conversational interface for walking through a recipe.

Team: Alexander Einarsson, Andong Luis Li Zhao, Quinn Shim
Github: https://github.com/andongluis/NLP-P3

## Requirements

The project uses Rasa as the main architecture for the conversational interface.

The requirements have been listed in the `requirements.txt` file.
(Note that running the most recent tensorflow version on Windows has provided some errors.
To rectify these in Windows, it might be necessary install some Visual Studios tools, as described
by [this](https://github.com/tensorflow/tensorflow/issues/22794) link)

## Supported Actions

- Greetings
e.g. "hello"
- Asking for purpose
e.g. "who are you"
- Giving a recipe URL
e.g. "https://www.allrecipes.com/recipe/12151/banana-cream-pie-i/"
- Asking for ingredients
e.g. "give me the ingredients"
- Asking for next step
e.g. "what is the next step"
- Asking for previous step
e.g. "what was the previous step"
- Asking for n-th step
e.g. "what is step 5"
- Asking "what is X"
e.g. "what is braising"
- Asking "how to Y"
e.g. "how to braise"
- Goodbye
e.g. "goodbye"

## How to Run

To run, you will need to have two terminal windows.
In one, you will run the command
```rasa run actions```

In the other, you will run
```rasa shell```
The `shell` terminal is where you will be talking with the interface.


### Training

To train this model, you will need to run the command

```rasa train```