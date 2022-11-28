# Python Advanced-color_list, JSON, remove_dups, Pytest

### By Philip Kendall

#### This project creates fake colors, removes any duplicates, dumps the infomation to a JSON file, and uses Pytest to test remove_dups() function

## Technologies Used

* Python
* Pytest
* JSON
* Git

## Description

* The faker module is imported and used to create 20 fake colors, which are then put into a list.
* The remove_dups() function removes duplicate colors by converting the list into a set.
* color_list is then converted into a dictionary called color_dict using dictionary comprehension with the keys representing the colors, and the values representing the length of characters in that color.
* color_dict is then dumped onto a JSON file and the data is then read back. If there are colors whose length is greater than 4, the name of the color and its character length is printed to the terminal.
* The parametrize() function of Pytest is then used to test the remove_dups function. The tests include a list with duplicates, an empty list, and a string.

## Setup/Installation Requirements

* Fork over the the repository to your own Github account.
* Clone your Github repo down to your local machine and into the directory you would like this project to be stored.
* Navigate to the main.py file and open it in your text editor.
* At the same time, in a terminal window, install the requirements.txt file by typing pip install -r requirements.txt on the command line.
* After that, the application should be able to run.

## Known Bugs

N/A

## License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The below copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2022 Philip Kendall