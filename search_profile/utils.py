import requests

token = "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"
username = "fattybobcat"

def api_project_info(data):
    url_search = data
    #print("url_search", data)
    project_info_api = requests.get(url_search, auth=(username,token)).json()
    project_info = {}
    project_info["name"] = project_info_api["name"]
    project_info["url_search"] = url_search
    project_info["stargazers_count"] = project_info_api["stargazers_count"]
    #print(projects)
    return project_info

def sort_data_by_params(data):
    projects = {}
    #print("data", data["repository_url"])
    count = 0
    n_closed = 0
    n_open = 0
    for item in data:
        #print("item ", item['repository_url'])
        if item["repository_url"] not in projects:
            count += 1
            #projects[item["repository_url"]] = []
            projects[item["repository_url"]] = api_project_info(
                item["repository_url"])
            projects[item["repository_url"]]["count"] = count
            projects[item["repository_url"]]["closed"] = {}
            projects[item["repository_url"]]["open"] = {}
        if item["state"] == "closed":
            projects[item["repository_url"]]["closed"][n_closed] = {
                "url": item["url"],
                "comment": item["comments"]}
            n_closed += 1
        else:
            projects[item["repository_url"]]["open"][n_open] = {
                "url": item["url"],
                "comment": item["comments"]}
            n_open += 1
   # print(projects)
    return projects


def api_pull_request_user(user):
    url_search = "https://api.github.com/search/issues?q=author%3A{}+type%3Apr&per_page=100".format(user)
    data_i = requests.get(url_search, auth=(username,token))
    print(data_i)
    data = data_i.json()
    total_count = data['total_count']
    data_pojects = data['items']
  #  print("total_count", total_count)
    #print("data_pojects", data_pojects)
    data_project = sort_data_by_params(data_pojects)
    #issue = Github.search_issues('', state='open', author='AalaaHabib', type='pr')
    #print("issue", issue)
    #print(data_project)
    return total_count, data_project
