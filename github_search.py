import requests
import csv
import json

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
        header = ["Keyword"] + [f"Repo {i}" for i in range(1, 11)]
        csv_writer.writerow(header)

        for keyword in keywords:
            top_repos = get_top_repos(keyword, token)
            row = [keyword] + top_repos
            csv_writer.writerow(row)

def main():
    token = "YOUR_PERSONAL_ACCESS_TOKEN"
    keywords = bulk_upload_keywords("keywords.txt")
    convert_to_csv(keywords, "github_search_results.csv", token)

if __name__ == "__main__":
    main()
