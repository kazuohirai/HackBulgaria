import requests
from graph import Graph
import copy


class GitHubApp:
    MAX_DEPTH = 4

    def __init__(self, root_user):
        self.graph = Graph("Git Profile")
        self.root_user = root_user

    def fill_user_graph(self, root_user):
        with open('url.txt', 'r') as f:
            url = f.read()
        url = url.format(root_user)
        info = requests.get(url)
        following = info.json()
        for item in following:
            self.graph.add_edge(root_user, item["login"])
        return self.graph.edges

    def fill_followees_graph(self, username):
        self.fill_user_graph(username)
        count = 1
        while count <= GitHubApp.MAX_DEPTH:
            temp = copy.deepcopy(self.graph.edges)
            for item in temp:
                if temp[item] == []:
                    self.fill_user_graph(item)
            count += 1

    def following(self, user):
        if user not in self.graph.edges:
            return "User not in graph."
        return self.graph.edges[user]

    def is_following(self, username):
        if username not in self.graph.edges:
            return False
        if username in self.graph.edges:
            if username in self.graph.edges[self.root_user]:
                return True
            else:
                return False

    def steps_to(self, username):
        if username not in self.graph.edges:
            return "Username not in graph."
        current_depth = [self.root_user]
        depth_count = 0
        while depth_count <= GitHubApp.MAX_DEPTH:
            deeper = set()
            if username in current_depth:
                return depth_count
            for item in current_depth:
                deeper = deeper.union(self.graph.get_neighbours_for(item))
            current_depth = deeper
            depth_count += 1
