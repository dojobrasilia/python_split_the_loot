class Splitter(object):
    def split(self, loot, numberOfPirates):
        
        self.init(loot, numberOfPirates)
        
        if self.is_unsolvable(): 
            return None
        
        while len(self.loot) > 0:
            self.give_one_gem_for_each_bucket()
            
        return self.sort_buckets()
   
    def give_one_gem_for_each_bucket(self):
        len_before = len(self.loot)
        
        for bucket in self.buckets:
            if(len(self.loot) > 0 and sum(bucket) < self.share):
                bucket.append(self.loot.pop())
            if (sum(bucket) > self.share):
                self.loot.append(bucket.pop())
                
        if(len_before == len(self.loot)):
            self.rollback_share_decision()   
                    
    def rollback_share_decision(self):
        self.rollback_depth +=1
        for bucket in self.buckets:
            self.loot = self.reclaim_gems_from_pirate(bucket) + self.loot
    
    def reclaim_gems_from_pirate(self,bucket):
        reclaimed_gems = []
        for i in range(0,self.rollback_depth):
            reclaimed_gems.append(bucket.pop())
        return reclaimed_gems
    
    def sort_buckets(self):
        for bucket in self.buckets:
            bucket.sort()
            bucket.reverse()
        return self.buckets
    
    def init(self,loot,numberOfPirates):
        self.rollback_depth = 0;
        self.loot = loot
        self.loot.sort()
        self.numberOfPirates = numberOfPirates
        self.share = sum(loot)/numberOfPirates
        self.buckets = self.create_buckets()
    
    def is_loot_undivisible_by_number_of_pirates(self):
        return sum(self.loot) % self.numberOfPirates != 0
    
    def are_there_more_pirates_than_gems(self):
        return len(self.loot) < self.numberOfPirates
    
    def are_there_one_gem_greater_then_share(self):
        for gem in self.loot:
            if(gem > self.share):
                return True
        return False
    
    def is_unsolvable(self):
        return self.is_loot_undivisible_by_number_of_pirates() \
                or self.are_there_more_pirates_than_gems() \
                or self.are_there_one_gem_greater_then_share()
    
    def create_buckets(self):
        buckets = []
        for i in range(0,self.numberOfPirates):
            buckets.append([])
            
        return buckets