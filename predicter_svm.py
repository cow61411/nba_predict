import os
import json
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier

class predicter:


    def __init__(self , player_dict_path , team_dict_path , game_detail_path , time_data_path):
        with open(player_dict_path , "rb") as fp:
            self.player_dict = json.load(fp)

        with open(game_detail_path , "rb") as fp:
            self.game_detail = json.load(fp)

        with open(team_dict_path , "rb") as fp:
            self.team_dict = json.load(fp)

        with open(time_data_path , "rb") as fp:
            self.time_data = json.load(fp)

    def _prepare_data_players(self):
        train_data = list()
        train_label = list()
        test_data = list()
        test_label = list()
        for date , games in self.game_detail.items():
            year = int(date[:4])
            for game , teams in games.items():
                data_temp = list()
                points = list()
                for team , players in teams.items():
                    points.append(players["Team Totals"]["PTS"])
                    ps = list()
                    ms = list()
                    for player , number in players.items():
                        if player != "Team Totals":
                            ps.append(player)
                            ms.append(number["MP"])
                    status = zip(ps , ms)
                    #print status
                    sort_status = sorted(status , key = lambda x : x[1] , reverse = True)
                    #print test
                    names = map(lambda x : x[0] , sort_status)[:5]
                    keys = map(lambda x : self.player_dict[x] , names)
                    data_temp += keys
                label_temp = points.index(max(points))
                if year == 2016:
                    test_data.append(data_temp)
                    test_label.append(label_temp)
                else:
                    train_data.append(data_temp)
                    train_label.append(label_temp)

        #print len(train_label)
        #print len(train_data)
        #print len(test_label)
        #print len(test_data)
        return train_data , train_label , test_data , test_label
    def _prepare_data_players_with_MP_weight(self):
        train_data = list()
        train_label = list()
        train_weight = list()
        test_data = list()
        test_label = list()
        test_weight = list()
        average_mp = [0] * 5
        for date , games in self.game_detail.items():
            year = int(date[:4])
            for game , teams in games.items():
                data_temp = list()
                weight_temp = list()
                points = list()
                for team , players in teams.items():
                    points.append(players["Team Totals"]["PTS"])
                    ps = list()
                    ms = list()
                    for player , number in players.items():
                        if player != "Team Totals":
                            ps.append(player)
                            ms.append(number["MP"])
                    status = zip(ps , ms)
                    #print status
                    sort_status = sorted(status , key = lambda x : x[1] , reverse = True)
                    #print test
                    names = map(lambda x : x[0] , sort_status)[:5]
                    keys = map(lambda x : self.player_dict[x] , names)
                    data_temp += keys

                    mps = map(lambda x : x[1] , sort_status)[:5]
                    weight_temp += mps

                #print data_temp
                label_temp = points.index(max(points))
                if year == 2016:
                    test_data.append(data_temp)
                    test_label.append(label_temp)
                else:
                    train_data.append(data_temp)
                    train_label.append(label_temp)
                    train_weight.append(sum(weight_temp) / 10.0)

        #print len(train_label)
        #print len(train_data)
        #print len(test_label)
        #print len(test_data)
        return train_data , train_label , test_data , test_label , train_weight

    def _prepare_data_teams(self):
        train_data = list()
        train_label = list()
        test_data = list()
        test_label = list()
        for date , games in self.game_detail.items():
            year = int(date[:4])
            for game , teams in games.items():
                data_temp = list()
                points = list()
                for team , players in teams.items():
                    points.append(players["Team Totals"]["PTS"])
                    data_temp.append(self.team_dict[team])
                label_temp = points.index(max(points))
                if year == 2016:
                    test_data.append(data_temp)
                    test_label.append(label_temp)
                else:
                    train_data.append(data_temp)
                    train_label.append(label_temp)

        #print len(train_label)
        #print len(train_data)
        #print len(test_label)
        #print len(test_data)
        return train_data , train_label , test_data , test_label

    def _prepare_data_PERs(self):
        train_data = list()
        train_label = list()
        test_data = list()
        test_label = list()
        for date , games in self.game_detail.items():
            year = int(date[:4])
            for game , teams in games.items():
                data_temp = list()
                points = list()
                for team , players in teams.items():
                    points.append(players["Team Totals"]["PTS"])
                    ps = list()
                    ms = list()
                    for player , number in players.items():
                        if player != "Team Totals":
                            ps.append(player)
                            ms.append(number["MP"])
                    status = zip(ps , ms)
                    #print status
                    sort_status = sorted(status , key = lambda x : x[1] , reverse = True)
                    #print test
                    names = map(lambda x : x[0] , sort_status)[:5]
                    for name in names:
                        if year != 2016:
                            data_temp.append(players[name]["PER"])
                        else:
                            judge = False
                            for temp_year in map(str , range(2006 , 2016)[::-1]):
                                for temp_month in map(str , range(1 , 13)[::-1]):
                                    if temp_year in self.time_data[name]:
                                        if temp_month in self.time_data[name][temp_year]:
                                            data_temp.append(self.time_data[name][temp_year][temp_month]["PER"])
                                            judge = True
                                            break
                                if judge:
                                    break
                            if not judge:
                                print "failed to get PER"
                                data_temp.append(0)
                label_temp = points.index(max(points))
                #'''
                #if len(data_temp) != 12:
                    #print "error"
                if year == 2016:
                    test_data.append(data_temp)
                    test_label.append(label_temp)
                else:
                    train_data.append(data_temp)
                    train_label.append(label_temp)
                #'''
                #train_data.append(data_temp)
                #train_label.append(label_temp)

        return train_data , train_label , test_data , test_label

    def _prepare_data_EFFs(self):
        train_data = list()
        train_label = list()
        test_data = list()
        test_label = list()
        for date , games in self.game_detail.items():
            year = int(date[:4])
            for game , teams in games.items():
                data_temp = list()
                points = list()
                for team , players in teams.items():
                    points.append(players["Team Totals"]["PTS"])
                    ps = list()
                    ms = list()
                    for player , number in players.items():
                        if player != "Team Totals":
                            ps.append(player)
                            ms.append(number["MP"])
                    status = zip(ps , ms)
                    #print status
                    sort_status = sorted(status , key = lambda x : x[1] , reverse = True)
                    #print test
                    names = map(lambda x : x[0] , sort_status)[:5]
                    for name in names:
                        data_temp.append(players[name]["EFF"])
                label_temp = points.index(max(points))
                #'''
                if year == 2016:
                    test_data.append(data_temp)
                    test_label.append(label_temp)
                else:
                    train_data.append(data_temp)
                    train_label.append(label_temp)
                #'''
                #train_data.append(data_temp)
                #train_label.append(label_temp)

        return train_data , train_label , test_data , test_label

    def _prepare_data_GmScs(self):
        train_data = list()
        train_label = list()
        test_data = list()
        test_label = list()
        for date , games in self.game_detail.items():
            year = int(date[:4])
            for game , teams in games.items():
                data_temp = list()
                points = list()
                for team , players in teams.items():
                    points.append(players["Team Totals"]["PTS"])
                    ps = list()
                    ms = list()
                    for player , number in players.items():
                        if player != "Team Totals":
                            ps.append(player)
                            ms.append(number["MP"])
                    status = zip(ps , ms)
                    #print status
                    sort_status = sorted(status , key = lambda x : x[1] , reverse = True)
                    #print test
                    names = map(lambda x : x[0] , sort_status)[:5]
                    for name in names:
                        data_temp.append(players[name]["GmSc"])
                label_temp = points.index(max(points))
                '''
                if year == 2016:
                    test_data.append(data_temp)
                    test_label.append(label_temp)
                else:
                    train_data.append(data_temp)
                    train_label.append(label_temp)
                '''
                train_data.append(data_temp)
                train_label.append(label_temp)

        return train_data , train_label , test_data , test_label

    def _prepare_data_PER_EFF_GmSc(self):
        train_data = list()
        train_label = list()
        test_data = list()
        test_label = list()
        for date , games in self.game_detail.items():
            year = int(date[:4])
            for game , teams in games.items():
                data_temp = list()
                points = list()
                for team , players in teams.items():
                    points.append(players["Team Totals"]["PTS"])
                    ps = list()
                    ms = list()
                    for player , number in players.items():
                        if player != "Team Totals":
                            ps.append(player)
                            ms.append(number["MP"])
                    status = zip(ps , ms)
                    #print status
                    sort_status = sorted(status , key = lambda x : x[1] , reverse = True)
                    #print test
                    names = map(lambda x : x[0] , sort_status)[:5]
                    for name in names:
                        data_temp.append(players[name]["PER"])
                        data_temp.append(players[name]["EFF"])
                        data_temp.append(players[name]["GmSc"])
                label_temp = points.index(max(points))
                '''
                if year == 2016:
                    test_data.append(data_temp)
                    test_label.append(label_temp)
                else:
                    train_data.append(data_temp)
                    train_label.append(label_temp)
                '''
                train_data.append(data_temp)
                train_label.append(label_temp)

        return train_data , train_label , test_data , test_label

    def predict(self):
        #train_data , train_label , test_data , test_label = self._prepare_data_players()
        #train_data , train_label , test_data , test_label , weight = self._prepare_data_players_with_MP_weight()
        train_data , train_label , test_data , test_label = self._prepare_data_PERs()
        #train_data , train_label , test_data , test_label = self._prepare_data_EFFs()
        #train_data , train_label , test_data , test_label = self._prepare_data_PER_EFF_GmSc()
        '''
        print len(train_data)
        print len(train_label)
        print len(test_data)
        print len(test_label)
        print test_data[0]
        '''
        clf = svm.SVC(C = 0.1)
        #clf = SGDClassifier(loss="modified_huber" , penalty="l1")
        #scores = cross_val_score(clf , train_data , train_label , cv = 5)
        #'''
        clf.fit(train_data , train_label )
        predict_result = clf.predict(test_data)

        count = 0
        for x , y in zip(test_label , predict_result):
            if x == y :
                count += 1
        #'''
        print "Accurancy : " , count / float(len(predict_result))
        #print("Accuracy: %f" % (scores.mean()))



test = predicter("./../data/player_dict.json" , "./../data/team_dict.json" , "./../data/player_data_with_per_eff_gmsc.json" , "./../data/player_monthly_PER.json")
test.predict()



                    



