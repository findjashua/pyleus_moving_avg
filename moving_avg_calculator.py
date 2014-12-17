from pyleus.storm import SimpleBolt

class MovingAvgBolt(SimpleBolt):
    OUTPUT_FIELDS = ['campaign_id', 'moving_avg']

    def process_tuple(self, tup):
        try:
            campaign_id, prices = tup.values
            moving_avg = sum(prices)/len(prices)
            self.emit((campaign_id, moving_avg), anchors[tup])
        except:
            #log the error
            pass

if __name__ == '__main__':
    MovingAvgBolt().run()

