# Text Analysis

Make sure that you delete all of the markers in this file and either
rewrite or delete all of the prompts. Ultimately, this file should contained
polished writing that is free of mistakes in grammar, spelling, or Markdown
syntax. It should also be a polished article that is suitable for publication on
your professional web site.

Make sure that your GitHub repository contains the following text files:

- `generated_one.txt`: generated text from the `aitextgen` program provided as a part of this project
- `generated_two.txt`: generated text from the `aitextgen` program provided as a part of this project
- `input_one.txt`: human-written text provided as part of this project
- `input_two.txt`: human-written text that you excerpt from an external source or write yourself

Make sure that your GitHub repository contains the following graphics files:

- `set-visualization-generated.png`: visualization created by `textanalysis` for the file `generated_one.txt`
- `set-visualization-input.png`: visualization created by `textanalysis` for the file `input_one.txt`

You must use a command like `git add` to ensure that certain files exist in the repository.

## Tyler Miller

## Program Input and Output

### What is the output from running the following command?

`poetry run textanalysis --input-file text/input_one.txt --analyze`

```python
✨ Let's characterize the file and its words!

        The input file contains 23 lines, including blank lines!
        The input file contains 19 lines, not including blank lines!
        The input file contains 5 paragraphs!
        The input file contains 118 unique words across all sets!
        The words that are found across all sets are: {'Make', 'to'}

🖌 Saving the visualization in graphics/set-visualization.png

🔬 Get ready, here is the analysis of the sets!
```

### What is the output from running the following command?

`poetry run textanalysis --input-file text/generated_one.txt --analyze`

```python
✨ Let's characterize the file and its words!

        The input file contains 15 lines, including blank lines!
        The input file contains 8 lines, not including blank lines!
        The input file contains 8 paragraphs!
        The input file contains 106 unique words across all sets!
        The words that are found across all sets are: set()


🖌 Saving the visualization in graphics/set-visualization.png

🔬 Get ready, here is the analysis of the sets!
```

### What is inside of the `generated_two.txt` file that `aitextgen` created?

```python
The Federal Reserve has been trying to figure out how much money will be available to the economy of the United States from the Federal Reserve, although the Fed is pushing back its efforts.

The Federal Reserve Board is pushing back on the idea that the U.S. economy has reached a point where it is no longer "in an economy of money," according to a report released by the Fed last week.

The report, titled "The American Economy: The Federal Reserve Is Making a Mistake," points to a few key facts.

The Fed has no plans to raise interest rates.

"In fact, the Federal Reserve expects to raise rates before the next set of economic growth rates are set and before the next monetary policy cycle begins," the report said.

The Fed didn't make any specific announcement about how much money will be available to the economy in the report, which was released just before the third quarter in which the government's unemployment rate was at its lowest level in more than a decade.

But it did say that if policymakers are willing to raise rates, "there is no reason to expect that the monetary policy rate will be substantially lower than at present."

The Fed has been trying to figure out how much money
```

### What is inside of the `input_two.txt` file that you downloaded/wrote and saved?

```python
These Songs all have in common is that they were recorded at the same studio.They were recorded at Sun Studio which is located in Memphis, Tennessee.
 It was formerly known as Memphis Recording Service and
 was housed in the same building as the Sun Records label business.

 The 1933 Version gives a sense of how musicals were back in that time frame. 
 This tends to be something on how you look and see what the dances were like for much older musicals. 
 To me it was interesting to see how the newer one has a little more intense movements compared to the older version.

The first one is the White Christmas version that you hear on the radio during the holiday season. 
It’s such a staple and everyone loves it. It has good rhythm and good tempo. 
The White Christmas version with Michael Buble is a new and inviting tune as it implements new age music to such a holiday classic. 
Personally, when listening to this song while writing this, it was hard to not like jam out to such a classic of a song but with Michael Buble.

In this song Rock Island Line, It clearly uses the call and response technique that we discussed in class. 
This also sounds like a work song that the slaves would sing. 
The song is sung with the intention being a work song and how it is repeated on and off again the same saying over and over again.

This song really gives the feel of the european Medieval time period as it has it has various instruments in the background and has one person singing and then a few more people join in. 
To me it sounds like it could be a church song . While this song is long it could be like a long church song. 
This is also a very calming song to overall listen to.

In this song Rock Island Line, It clearly uses the call and response technique that we discussed in class. 
This also sounds like a work song that the slaves would sing. 
The song is sung with the intention being a work song and how it is repeated on and off again the same saying over and over again.
```

## Source Code

### Describe in detail how your provided source code works

#### Please explain each line of source code from the `extract` module

The particular extract module is something that is when it extracts the particular data that when it takes the data from the code and pulls it apart.
The code in the extract module takes the no newlines and then takes it and strips it from the input lines. This means that it takes out the necessary lines of the input.
Split_text is just splitting the lines into a new set of lines. of the functions.
It then takes the paragraphs of the multiple sets of texts and also strips that as well.
Then it will return the paragraphs.

```python
def extract_paragraphs(input_lines: str) -> List[str]:
    """Extract all of the paragraphs from the lines of textual input."""
    # Reference:
    # https://stackoverflow.com/questions/53240763/python-how-to-separate-paragraphs-from-text
    no_newlines = input_lines.strip("\n")
    split_text = NEWLINES_RE.split(no_newlines)
    paragraphs = [p + "\n" for p in split_text if p.strip()]
    return paragraphs
```

## Analyzing the Text

### According to the output of your program, what words does `input_one.txt` have in common across all paragraphs? How did you know?

The things that are in common across all the paragraphs is that they are both have large amounts of text that are all generated into multiple lines of the txt file.
This then means that the structures in each input of the files take in the same amount of text like likes of text that has breaks in it and then start back up again.
When looking at the overall files they tend to be similar like I said before. They both have the amount of text flowing into the next lines instead of any function values at hand.

### Using the console output and visualization for the `input_one.txt`, what trends do you see? Interpret these trends

The trends that I see in that particular file is how some letters are capitalzed. This tends to be something that usally sticks with someone on how they look at this particular file.
Trends are usally set by how similar something is when looking at two or more things in the same way or overtime.
Trends like this according to texts in the input files make this a trend on how similar they are when observing the criteria of how text is particularly processed.
For this reason the idea of text processing is very important for the implications of the coding structures in computer science.

### Using the console output and visualization for the `generated_one.txt`, what trends do you see? Interpret these trends

Something that I see that catches my eye of the `generated_one.txt file is the way that it tells a story. This particular txt file takes the generated file and has this way of outputting the data in the form of text and puts words together.
The file contains words in it itself and then is able to get the output with a command.
Output like this is rather interesting because of the way the words are able to be written in the sense of sentences.
That is why the generated one txt file is a rather intriguing file to say the least.

## Professional Development

### What are the similarities and differences between `set`, `FrozenSet`, and `FiniteSet`?

The similarities and differences between `set`, `FrozenSet`, and `FiniteSet`. The similarities of these are they are just other ways to have lists that are being called in the function. This way functions have a way of lists to be stored.
Sets are pretty simple they are able to be used for a few different things. Frozenset is able to have the set that is immutable within each sets of a function. A finiteset is able to take numbers and put them in a various discrete variations.

### How is the `set` discrete structure similar to and different from the `list` and the `tuple`?

A set is similar to the list and tuple way of creating functions. This takes they forms of functions that are able to be called into many ways of being iterable of the function.
This way functions have a place on where they are being called and then shown in the function of how they data is able to be returned in various forms of functions.
These particular functions are very useful on when and how to use them. They tend to sometimes be used different ways which can be helpful when experimenting with code but then also not helpful when messing up what kind of function you tend to be using.

### At your own option, do you have any other insights to share about this assignment?

I do not have anything to really add to this project. I thought it was a rather interesting and intriguing solution on how to get the text processing from various functions in the code.
