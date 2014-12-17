from pyleus.storm import Spout

class BidsSpout(Spout):

    OUTPUT_FIELDS = ['campaign_id', 'prices']

    def next_tuple(self):
        #get campaign_id, last 20 prices from Kafka
        self.emit((campaign_id, prices))

if __name__ == '__main__':
    BidsSpout().run()
