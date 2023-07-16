class Config:
    def __init__(self):

        self.db_info = {
            # after connect the container to docker shared network, can use container name instead of machine public address to connect
            'localhost': 'mysql-for-superset',  
            'username': 'root',
            'pw': 'your password'
        }

        self.infotracer_token = 'your token'

        self.youtube_token = {
            "name1":"token1",
            "name2":"token2"
        }

        self.query_dict = {
            # use AND/OR to create query
            # use "" for exct match
            "candidate1":'("candidate1 keyword1") AND (candidate1 keyword2)',
            "candidate2":"(candidate2 keyword1) OR (candidate2 keyword2)",
            "candidate3":"query"
        }

        #  keep the same as template, do not modify
        self.database_name = 'dashboard'

        self.delete_all_table_and_restart = False

        self.date = {
            'predefined_period': True, # true for specified period historical data collection, if false, daily update
            'start_date': '2023-07-13',
            'end_date': '2023-07-14'
        }

        # the following part is for debug, user don't need to modify
        # run true means run the data collection
        # update true means update the collected data to db

        self.generate_helper_table = {
            'run': True,
            'update_db': True
        }
        
        # this should generally be false
        # generate infotracer and sentiment table takes care of both 
        self.generate_infotracer_table = {
            'run': False,
            'update_db': False
        }

        self.generate_infotracer_and_sentiment_table = {
            'run': True,
            'update_db': True
        }

        self.generate_wordcloud_table = {
            'last_n_days': 14, # what range of data to use to generate wordcloud
            'stop_word_file': 'spanish', # file name of stop word file, if want to add/rm words, can go to txt to modify
            'run': True,
            'update_db': True
        }

        self.generate_network_table = {
            'run': True,
            'update_db': True
        }

        # turn on of off daily refresh data 2 days ago
        self.refresh = {
            'run': True,
            'update_db': True
        }