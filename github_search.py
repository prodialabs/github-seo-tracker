import requests
import csv
import json
import os
from datetime import datetime

def get_top_repos(keyword, token):
    api_url = f"https://api.github.com/search/repositories?q={keyword}&sort=stars&order=desc&per_page=10"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(api_url, headers=headers)
    data = json.loads(response.text)
    top_repos = [item["html_url"] for item in data["items"]]
    return top_repos

def bulk_upload_keywords(file_path):
    keywords = []
    with open(file_path, "r") as file:
        for line in file:
            keywords.append(line.strip())
    return keywords

def convert_to_csv(keywords, output_file, token):
    with open(output_file, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        header = ["Keyword", "Date"] + [f"Repo {i}" for i in range(1, 11)]
        csv_writer.writerow(header)

        current_date = datetime.now().strftime("%m/%d/%Y")

        for keyword in keywords:
            top_repos = get_top_repos(keyword, token)
            row = [keyword, current_date] + top_repos
            csv_writer.writerow(row)
            
def main():
    token = "YOUR-PERSONAL-TOKEN"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "keywords.txt")
    keywords = bulk_upload_keywords(file_path)
    convert_to_csv(keywords, "github_search_results.csv", token)

if __name__ == "__main__":
    main()
