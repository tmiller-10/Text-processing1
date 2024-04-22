# Text Analysis Project

Welcome to my Text Analysis project repository. Follow these steps to set up and run the project after cloning it to your local machine.

## Setup Instructions

1. **Navigate to the project directory**:
   - Change to the cloned repository directory: `cd path-to-cloned-repo`
   - Then, move to the specific program directory: `cd datauniquifier`

2. **Install Dependencies**:
   - Run the command `poetry install` to install the required dependencies for this project.

## Running the Program

1. **Generate Analysis**:
   - First, generate the necessary text file:
     ```bash
     poetry run textanalysis --output-file text/generated_one.txt --generate
     ```
   - Then, analyze the generated text file:
     ```bash
     poetry run textanalysis --input-file text/generated_one.txt --analyze
     ```

2. **Analyze Existing Text**:
   - To analyze an existing text file, use the following command:
     ```bash
     poetry run textanalysis --input-file text/input_one.txt --analyze
     ```

   Upon successful execution, you should see the following output:

 **Output**:

## Here is how to run the program:


### Generate Text Data:
Use the following command to generate the text file:

```
poetry run textanalysis --output-file text/generated_one.txt --generate
```
```
poetry run textanalysis --input-file text/input_one.txt --analyze
```
```
 ✨ Let's characterize the file and its words!

The input file contains 23 lines, including blank lines!
The input file contains 19 lines, not including blank lines!
The input file contains 5 paragraphs!
The input file contains 118 unique words across all sets!
The words that are found across all sets are: {'Make', 'to'}

🖌 Saving the visualization in graphics/set-visualization.png

🔬 Get ready, here is the analysis of the sets!
```