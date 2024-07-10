# README

## Greek Gematria Calculator

Manual and Programme written in ChatGPT for Greek Gematria Correspondence Program using Liddell-Scott Dictionaries. This repository was added by 23-777.

## Introduction

Welcome to the manual for the Greek Gematria Correspondence Program. This program allows you to explore Greek words and their definitions using the Liddell-Scott dictionary.

## Requirements

To use this program, ensure you have the following installed:

- Python 3.x
- Required libraries:
  - tkhtmlview
  - tkinter
  - pandas
- Files:
  - attic.txt
  - atticdef.txt
- UTF-8 Encoding

## Usage

### Step 1: Installation and Setup

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/vucjipastir/GreekGematria.git
    ```

2. Install the required libraries and dependencies as specified in the requirements.txt file, if available.

### Step 2: Running the Program

1. Navigate to the directory where the program is located:

    ```bash
    cd GreekGematria
    ```

2. Run the program using Python:

    ```bash
    python PythGematria.py
    ```

### Step 3: Using the Program

Upon running the program, it will prompt you with a menu or an input prompt. Follow the prompts as described below:

1. Click "Load Words and Definitions".
2. Load "Attic.txt".
3. Click "Load Words and Definitions".
4. Load "atticdef.txt".

Now the program is armed for use.

#### Menu Options:

- **Option 1: Input a number to seek the Greek gematria correspondence in the Liddell-Scott dictionary.**
  - Enter a number corresponding to a word's gematria value.
  - The program will output the words with that gematria value.
  - Copy-paste the word you're interested in and proceed to search.

- **Option 2: Enter a particular word directly.**
  - Type the word you want to search for in the dictionary.
  - The program will provide the exact definitions below.

#### Example Usage:

**Choosing Options:**

```plaintext
ΓΞΘΠΕΗΑ

Select option:
1
Enter the number to seek gematria correspondence:
166
Gematria value of 'ΓΞΘΠΕΗΑ': 166
Words with the same gematria value:
αἰγοπόδης, εὐνομία, εὐποιία, κεραμίς, λαπαδνός, ληίζομαι, μελίπαις, παιγνιώδης

Paste the word you want to search:

Select option:
2
Enter the word to search:
Λόγος
Select option:
2
Enter the word to search:
Λόγος


Step 4: Exiting the Program

To exit the program, use the appropriate command (e.g., Ctrl+C in the terminal).


### Additional Notes

    Loading the libraries in the correct sequence is crucial for the proper functioning of the program. Please follow the steps below:
        Launch the program.
        Select "Load Words and Definitions".
        Upload the file "Attic.txt".
        Repeat the process and upload the file "atticdef.txt".
    The program reads only words in the Greek Alphabet, and Latin/Arabic numerals.
    If you copy a word to get a definition or a numerical value, please ensure you use the Greek Alphabet input.
    Make sure the attic.txt and atticdef.txt files are accessible and correctly formatted according to the program's requirements.
    For further customization or troubleshooting, refer to the program's documentation or GitHub repository.

Thank you.

