# Text Analysis

## Assigned: Tuesday, April 18, 2022
## Due: Tuesday, April 26, 2022

After cloning this repository to your computer, please take the following steps:

- Follow the instructions on the Proactive Programmers web site for this project
- Use the `cd` command to change into the directory for this repository.
- Change into the program directory by typing `cd datauniquifier`.
- Install the dependencies for the project by typing `poetry install`
- Run the program with the correct input file by typing:
  - Generate the text: `poetry run textanalysis --output-file text/generated_one.txt --generate`
  - Analyze the text: `poetry run textanalysis --input-file text/input_one.txt --analyze`
  - Please note that the program will not work unless you add the required source code
  - You should also try to run the program with only the `--help` flag
  - What happens when you run the program but specify an incorrect file?
- Confirm that the program is producing the expected output
- Remember that this program produces a graphical visualization that you will need to load and understand
- When you commit to your GitHub repository, please use descriptive commit messages
- Make sure that you try your program on all four inputs described in the `reflection.md` file
- Make sure that you understand all of the console and graphical output created by `textanalysis`
- Use a `docker run` command for your operating system to run GatorGrader
- Provide all of the required responses in the `writing/reflection.md` file
