# a(n) plugin
Simple anki plugin to not give away how a word starts when doing 
fill-in-the-gap cards. Shows "a(n)" in the front and "a" or "an" in the back.

A word of warning: setting this up assumes familiarity with Anki and web technologies.

## Usage
When the setup is done (read below), you use the `a(n)` toolbar button to select
what you want to see in the back (e.g. `a`)

![img.png](doc/1_select.png)

Then you can complete the card.

![img.png](doc/2_complete.png)

And enjoy the result:

![img.png](doc/3_preview_front.png)
![img.png](doc/4_preview_back.png)

You can also download this [sample card](doc/example.apkg).

## Setup
For the plugin to work you need to adapt the note type you want to use for
English clozes.

First, include this CSS by:

* Go to the card browser and select one card of the note type you want to use
* Click on `Cards...` > `Styling`
* Add this:

      .front-only {
        display: show;
      }
      .answer .front-only {
        display: none;
      }
    
Then, you need to have the back template marked with class `answer`. To do so,
click in `Back template` and surround the content with:

       <div class="answer">
         ... your template...
       </div>
