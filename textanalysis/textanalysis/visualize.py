# Make sure that you understand all of the provided source code in
# this file and the way in which it performs set visualization with supervenn!

"""Visualize the sets using the supervenn package."""

from typing import List
from typing import Set

from supervenn import supervenn  # type: ignore
import matplotlib.pyplot as plot  # type: ignore


def visualize_sets(sets: List[Set[str]]):
    """Create a visualization of sets."""
    # create a matplotlib figure space
    plot.figure(figsize=(16, 8))
    # compute all of the subsets and then visualize them
    # NOTE: note that there are many different parameters that
    # you can pass to the supervenn function; please explore those
    # options through the GitHub repository for the project. Note
    # that different options may make it easier/harder for you
    # to understand the overlap between the sets in the file.
    supervenn_plot = supervenn(
        sets, side_plots=True, widths_minmax_ratio=1, sets_ordering="minimize gaps"
    )
    # save the visualization in the output/ directory
    # NOTE: if you want to make the program more configurable, please
    # consider making this directory and file name a parameter to
    # the program instead of being hard-coded as a string
    # NOTE: you are not required to complete this task; however,
    # adding this feature to the program will make it easier for
    # you to complete the analysis of the text files using sets
    # plot.savefig(
    #     "/Users/tylermiller/Desktop/Allegheny /CMPSC/CMPSC102/EE/EE7/computer-science-102-spring-2022-ee7-text-processing-tmiller-10/textanalysis/textanalysis/graphics/graphicsset-visualization-generated.png"
    # )
    plot.savefig("graphics/set-visualization.png")
    # plot.savefig("textanalysis/textanalysis/graphics/set-visualization-generated.png")
    plot.close()
    # return the dictionary of chunks for visualization purposes
    return supervenn_plot.chunks
