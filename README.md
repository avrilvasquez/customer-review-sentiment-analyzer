# Customer Review Sentiment Analyzer

A beginner Python project that analyzes customer reviews using keyword matching and basic negation handling. Includes a terminal version and a Streamlit web interface.

## Features

- Identifies positive and negative words
- Handles capitalization and punctuation at word edges
- Reverses a word’s sentiment when immediately preceded by “not”
- Shows positive points, negative points, and matched words
- Labels results Positive, Negative, Mixed, or No sentiment words detected
- Rejects empty reviews
- Allows multiple reviews in the terminal until you type `quit`

## Setup

You need Python and Git installed.

Clone the repository:

```bash
git clone https://github.com/avrilvasquez/customer-review-sentiment-analyzer.git
cd customer-review-sentiment-analyzer
```

Create and activate a virtual environment.

**macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows Command Prompt:**

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

Then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Web App

With the virtual environment activated:

```bash
python -m streamlit run web_app.py
```

Open the local URL shown in the terminal, enter a review, and click **Analyze**.

## Run the Terminal Version

With the virtual environment activated:

```bash
python app.py
```

Enter reviews one at a time. Type `quit` to exit.

## Example

Review: `friendly but not good`

- Matched words: friendly, good
- Positive points: 1
- Negative points: 1
- Sentiment: Mixed

## How It Works

`analyze_review()` checks the review against positive and negative word lists and applies a basic rule for “not.”

`get_sentiment()` compares the resulting point totals to choose a label. Equal nonzero totals produce Mixed; zero totals produce No sentiment words detected.

`web_app.py` imports these functions to display results in a webpage.

## Limitations

- Only recognizes words in the predefined lists.
- Handles “not good,” but not more complex phrases like “not very good.”
- Does not reliably understand sarcasm or sentence context.
- Unequal positive and negative totals receive the label with more points, even when both are present.
- Points are rule-based scores, not confidence percentages.

## What I Practiced

Python functions, loops, conditionals, lists, text processing, virtual environments, Git, GitHub, and Streamlit.