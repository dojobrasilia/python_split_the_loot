class Splitter(object):
    def split(self, loot, numberOfPirates):
        
        self.loot = loot
        self.loot.sort()
        self.numberOfPirates = numberOfPirates
        
        share = sum(loot)/numberOfPirates
        buckets = self.create_buckets()
        
        if self.is_unsolvable(): 
            return None
        
        
        while len(loot) > 0:
            for bucket in buckets:
                if(len(loot) > 0 and sum(bucket) < share ):
                    bucket.append(loot.pop())
          
        return buckets
    
    def is_loot_undivisible_by_number_of_pirates(self):
        return sum(self.loot) % self.numberOfPirates != 0
    
    def are_there_more_pirates_than_gems(self):
        return len(self.loot) < self.numberOfPirates
    
    def is_unsolvable(self):
        return self.is_loot_undivisible_by_number_of_pirates() or self.are_there_more_pirates_than_gems()
    
    def create_buckets(self):
        buckets = []
        for i in range(0,self.numberOfPirates):
            buckets.append([])
            
        return buckets