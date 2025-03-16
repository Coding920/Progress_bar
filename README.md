# Loading progress bar
## Made for easy intergration into your python command line project!

### Usage

In order to use this progress bar for your own, first you must import and initialize a `ProgressBar` object.
Optionally, you can modify the characters used by providing new characters. 
E.g. `(empty_char = ' ', full_char = '#', head_char = '*')`

Next, prior to printing out your loading screen, you must call the `ProgressBar.prep()` method.
This hides the cursor, otherwise the cursor will do lots of flashing and the messages will be hard to read.

Then you must call the `ProgressBar.display()` method. This, of course, shows the progress bar
You must pass in `(filled_amount, full_size, message_to_display)`
You can do this in a for loop and pass in new messages while updating the filled and full sizes.
Alteratively, you can also write it all out manually and update it as you go.

Once you are done with all your loading you must call `ProgressBar.end_display()`
in order to show the cursor again and set everything back to normal.

### WIP

Eventually I plan on making a "SimpleBar" where you hand it a list of messages and it handles the rest of it for you. 

I also plan on simplifying the proccess to be simpler and not requiring to call so many steps
