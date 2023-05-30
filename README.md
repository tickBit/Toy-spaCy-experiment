# Toy spaCy experiment

You'll need to have the spaCy module installed. In this project "en_core_web_lg" model was used, but you can use "en_core_web_sm" instead, if you want. To download the large model type

* python -m spacy download en_core_web_lg

## Using the program

- Give a story to the system and ask "where" questions about the objects in the story
- The system understands only few verbs: go, travel, move, leave, drop, leave, get and take. Also the past tense of those verbs.

The system's ability to "understand" anything, is very limited.

I got inspired from the Babi dataset from Facebook research and have used as an example story the following: *Mary moved to the bathroom. Sandra took the apple. Mary went to the hallway. Mary got the milk. John moved to the bedroom. Mary dropped the milk. John took the milk. John moved to the kitchen. Sandra went to the bedroom.*

## Example picture of the program running

![toy-spaCy](https://github.com/tickBit/Toy-spacY-experiment/assets/61118857/fef6d1f0-ef27-4fc6-b213-55e7b7e2ec3f)
