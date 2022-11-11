"""Extract the paragraphs and other textual content from the paragraphs of text."""

# Add the required imports at the top of the file
from typing import List

import re


def extract_lines_including_blanks(input_lines: str) -> List[str]:
    """Extract all of the lines, including the blanks lines."""
    extract = []
    # This function will start the extraction process
    for line in input_lines.splitlines():
        # extract all of the lines in the file, using splitlines
        extract.append(line)
        # return all of the extracted lines
    return extract


def extract_lines_not_including_blanks(input_lines: str) -> List[str]:
    """Extract all of the lines, not including the blanks lines."""
    extract = []
    # extract all of the lines in the file, using splitlines
    for line in input_lines.splitlines():
        extract.append(line)
        # filter out all of the blank lines that have a length of zero
        # return the list of non-blank lines
    for i in extract:
        if i == "":
            extract.remove(i)
    return extract


def extract_paragraphs(input_lines: str) -> List[str]:
    """Extract all of the paragraphs from the lines of textual input."""
    # implement a function that uses, for instance, regular expressions to
    # break up a provided text in a string as a list of strings, with each
    # string representing a paragraph
    # consult the following reference:
    # you may use other online tutorials or responses in your implementation
    # of this function as long as you provide the needed references
    # remove leading and trailing newline characters
    return input_lines.split("\n\n")


def extract_unique_words_paragraphs(paragraphs: List[str]) -> List[set[str]]:
    """Extract all of the unique words in each one of the paragraphs."""
    # go through each of the strings inside of the list and
    # extract the unique words in each of the paragraphs
    unique = []
    # collect the unique words for each paragraph in a set of strings
    # store each set of unique words in a separate index of a list
    for word in paragraphs:
        unique.append(set(re.findall(r"[A-Za-z]+", word)))
        # return a list that contains at each index a set of strings
        # such that every one of the sets contains the unique words for a paragraph
    return unique


def extract_unique_words(sets: List[set[str]]) -> set[str]:
    """Extract all of the unique words shared across the sets in a list."""
    # create a single set of strings that includes all of the words
    # that that are unique across all of the sets for each of the paragraphs
    return sets[0].union(*sets)


def extract_common_words(sets: List[set[str]]) -> set[str]:
    """Extract all of the unique words shared in common by sets in a list."""
    # create a single set of strings that includes all of the words
    # that are found in every one of the sets for each paragraph in the text
    return sets[0].intersection(*sets)
