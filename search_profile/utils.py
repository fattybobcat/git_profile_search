from django.shortcuts import render
import requests
token = "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"
username = "fattybobcat"


def api_project_info(data):
    url_search = data
    project_info_api = requests.get(url_search, auth=(username, token)).json()
    project_info = {}
    project_info["name"] = project_info_api["name"]
    project_info["url_search"] = project_info_api["html_url"]
    project_info["stargazers_count"] = project_info_api["stargazers_count"]
    return project_info


def sort_data_by_params(data):
    projects = {}
    count = 0
    n_closed = 0
    n_open = 0
    for item in data:
        if item["repository_url"] not in projects:
            count += 1
            projects[item["repository_url"]] = api_project_info(
                item["repository_url"])
            projects[item["repository_url"]]["count"] = count
            projects[item["repository_url"]]["closed"] = {}
            projects[item["repository_url"]]["open"] = {}
        if item["state"] == "closed":
            projects[item["repository_url"]]["closed"][n_closed] = {
                "url": item["html_url"],
                "comment": item["comments"]}
            n_closed += 1
        else:
            projects[item["repository_url"]]["open"][n_open] = {
                "url": item["html_url"],
                "comment": item["comments"]}
            n_open += 1
    return projects


def api_page_paginator(link):
    page = {}
    list_link = link.split(',')
    if link:
        for rec in list_link:
            rec_l = rec.split(";")
            page[rec_l[1][6:-1]] = rec_l[0][1:-1].replace("<", "")
    return page


def api_pull_request_user(request, user, params_page):
    page_curent = "&{}".format(params_page)
    url_search = ("https://api.github.com/search/issues?q=author%3A{}"
                  "+type%3Apr&per_page=100{}").format(
        user,
        page_curent
    )
    data_r = requests.get(url_search, auth=(username, token))
    print(data_r.status_code)
    if data_r.status_code != 200:
        context = {}
        context["message"] = "Don't found user: {}".format(user)
        return render(request, 'index.html', context)
    data = data_r.json()
    list_info = ""
    if "Link" in data_r.headers:
        list_info = data_r.headers["Link"]
    page = api_page_paginator(list_info)
    page["page_curent"] = page_curent
    total_count = data["total_count"]
    data_pojects = data["items"]
    data_project = sort_data_by_params(data_pojects)
    return total_count, data_project, page
