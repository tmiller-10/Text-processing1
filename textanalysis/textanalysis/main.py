# Make sure that you understand all of the provided source code in
# this file and the way in which it provides the entire command-line interface!

"""Define the command-line interface for the textanalysis program."""

from rich.console import Console

from pathlib import Path

from textanalysis import extract
from textanalysis import visualize

import typer

cli = typer.Typer()

console = Console()


@cli.command()
def main(
    input_file: Path = typer.Option(None),
    # output_file: Path = typer.Option(None),
    analyze: bool = typer.Option(False, "--analyze"),
):
    """Automatically analyze the words inside of text through the use of the set."""
    # the analyze flag was specified
    if analyze:
        # the file was not specified so we cannot continue using program
        if input_file is None:
            console.print("No output file specified!")
            raise typer.Abort()
        # the file was specified and it is valid so we should analyze it
        if input_file.is_file():
            # break up the text into lines and count the lines, including blank lines
            input_text = input_file.read_text()
            input_line_count = len(extract.extract_lines_including_blanks(input_text))
            # this statement prints the sparkles segment of the output of the code
            console.print(":sparkles: Let's characterize the file and its words!")
            # this is part for the output
            console.print()
            # this is for the output of the data
            console.print(
                f"\tThe input file contains {input_line_count} lines, including blank lines!"
            )
            # break up the text into lines, exclude blanks, and count the lines
            input_line_count_no_blanks = len(
                extract.extract_lines_not_including_blanks(input_text)
            )
            console.print(
                f"\tThe input file contains {input_line_count_no_blanks} lines, not including blank lines!"
            )
            # break up the text into paragraphs and count the paragraphs
            input_paragraphs = extract.extract_paragraphs(input_text)
            # this takes care of the length of the paragraph of the input
            input_paragraphs_count = len(input_paragraphs)
            console.print(
                f"\tThe input file contains {input_paragraphs_count} paragraphs!"
            )
            # create a set of words for each paragraph
            list_of_paragraph_sets = extract.extract_unique_words_paragraphs(
                input_paragraphs
            )
            # extract and display the count of the number of unique words across all of the paragraphs
            unique_words_set = extract.extract_unique_words(list_of_paragraph_sets)
            # this segment of is the len of the unique words set
            unique_words_set_count = len(unique_words_set)
            console.print(
                f"\tThe input file contains {unique_words_set_count} unique words across all sets!"
            )
            # extract and display the words that are in common for all of the sets
            common_words_set = extract.extract_common_words(list_of_paragraph_sets)
            console.print(
                f"\tThe words that are found across all sets are: {common_words_set}"
            )
            console.print()
            # visualize the sets and then show all of the computed subsets
            console.print(
                ":paintbrush: Saving the visualization in graphics/set-visualization.png"
            )
            # this is a seperation for the console.print statement
            console.print()
            # this console.print statement gives the part of the output when you run the code
            console.print(":microscope: Get ready, here is the analysis of the sets!")
            console.print()
            set_chunks = visualize.visualize_sets(list_of_paragraph_sets)
            console.print(set_chunks)
