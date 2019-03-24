class ApiCall(object):
    def __init__(self, db, person_id):
        '''
        parameters
        :db a dict like object
        :person_id a unique identifier

        :return a list'''

        self.first_name = db[person_id]['first_name']
        self.last_name = db[person_id]['last_name']
        self.status = db[person_id]['status']
        self.money = db[person_id]['money']
        self.job = db[person_id]['job']

    def call(self, db, person_id):
        if person_id in db:
            return "{}, {}, {}, {}, {}".format(self.first_name, self.last_name, self.status, self.money, self.job)
        else:
            return "Your db sucks there's no id"