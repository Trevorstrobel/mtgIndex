# mtgIndex
Magic the Gathering card indexing tool


General Notes:
  - with the camera (logitec c920 webcam) about 6"-7" above the card, the area slider shoud be set to ~500,000 for accurate detection.
  - The upper value (U-V) slider needs to be adjusted depending on ambient light levels.
    -> Allow for manual adjustments, but on startup, maybe ramp up the U-V until a rectangle is detected.
      --> It may be necessary to do this for every card to account for variations in the black levels on the printed cards.
      --> again, this only works for black bordered cards so far.
    -> Will need to measure over a few frames as the detection is unstable at the lower bounds.



A list in no good order yet:

1. Download Database:
    - Scryfall's database seems like the most likely candidtate.
        -> its updated daily and is a larger database. downloading and updating should be an automated task.
    - Database comes as a CSV file, do we want to pump that CSV into a local DB? I would think so.
        -> does scryfall's csv download come with a changelog?


2. detect the overall card:
    - find rectangle shape.
    - Do I need to know which side is up?
    - read name of card
    - read set designator and card number

3.
