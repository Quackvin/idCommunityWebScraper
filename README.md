# idCommunityWebScraper
Tool I've been developing for a project to automatically download all demographic data for an area from the idCommunity atlas: https://atlas.id.com.au/

The provide an awesome amount of information about Australian municipalities, but it's a pain to get all the demographic data out. This tool allows the user to select SA1 areas they want to extract information about and relax while navigating the menus and downloading the biz is done automatically

# Current State
Able to automatically download a single defined file.

# Work Done
- Switched from beautiful soup to selenium
- Switched from selenium dom selectors to executing javascript
- Created algorithm to loop through all options and click download button.
- Broke loop into function so it can be called for each item when the previous is finished downloading

# Current Issue and Intended Fix
- The loop runs too fast and gets through all the options before the interface can update, so only the first option gets downloaded. Sometimes it gets downloaded multiple times
- Need to write function to check download location to see if a new file has appeared, it if has then rename it appropriately (seleniuim can't handle renaming file downloads) and run function to download next item
