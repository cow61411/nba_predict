
def get_four_factorys(team_data , oppo_data):
    result = dict()
    result["offense"] = dict()
    result["offense"]["off_shooting"] = (team_data["FG"] + 0.5 * team_data["3P"]) / team_data["FGA"]
    result["offense"]["off_turnovers"] = team_data["TOV"] / (team_data["FGA"] + 0.44 * team_data["FTA"] + team_data["TOV"])
    result["offense"]["off_rebounding"] = team_data["DRB"] / (oppo_data["ORB"] + team_data["DRB"])
    result["offense"]["off_freeTrows"] = team_data["FT"] / team_data["FGA"]

    result["defence"] = dict()
    result["defence"]["def_shooting"] = (oppo_data["FG"] + 0.5 * oppo_data["3P"]) / oppo_data["FGA"]
    result["defence"]["def_turnovers"] = oppo_data["TOV"] / (oppo_data["FGA"] + 0.44 * oppo_data["FTA"] + oppo_data["TOV"])
    result["defence"]["def_rebounding"] = oppo_data["DRB"] / (team_data["ORB"] + oppo_data["DRB"])
    result["defence"]["def_freeTrows"] = oppo_data["FT"] / oppo_data["FGA"]

    return result
