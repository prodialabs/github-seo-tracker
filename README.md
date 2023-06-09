# Github SEO Tracker
Track the top 10 results for a particular keyword in github search

This repo used GPT4 to create this tool using the prompt

You are an AI Programming assistant.

- Follow the user requirements & to the letter.
- First think step-by-step - describe your plan for what to build in pseudocode, written out in great detail.
- Then output the code in a single code block.
- Minimize any other prose.

Write me a tool that to track search results on Github in Python 3

- Use the github search API https://api.github.com/search/repositories to return the top 10 results for a particular keyword
- Support bulk upload of keywords
- Convert the results into a csv where the first column is the keyword and the next 10 columns are the github repo in decending order

And then a few back and forth conversations getting it to include data/time and better understanding of file structure (this could have been done in the first step with a better prompt)

Remember to replace YOUR_PERSONAL_ACCESS_TOKEN with your actual personal access token that you generated from your GitHub account.
