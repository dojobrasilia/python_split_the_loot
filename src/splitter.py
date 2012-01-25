class Splitter(object):
    def split(self,loot,pirate_number):
        #loot.sort()
        
        ret = self.init_answer(pirate_number)
        
        bucket_size = self.compute_bucket_size(loot, pirate_number)
        
        pirate_index = 0
        loot_size = loot.__len__()
        while loot.__len__()>0:
            pirate_bucket = ret[pirate_index]
            self.split_pirate(loot, ret[pirate_index], bucket_size)
            pirate_index += 1
                
        print bucket_size
        print loot
        print ret
        return ret
    
    def split_pirate(self, loot, pirate_bucket, bucket_size):
        
        sum = 0
        for g in pirate_bucket:
            sum += g
         
        tries = 0
        loot_size = loot.__len__()
        while sum < bucket_size and tries < loot_size:
            gem = loot.pop(0)
            if sum+gem > bucket_size:
                loot.append(gem)
            else:
                pirate_bucket.append(gem)
                sum += gem
            tries += 1
            
        if sum<bucket_size:
            loot.append(pirate_bucket.pop())
            self.split_pirate(loot, pirate_bucket, bucket_size)
            
        pirate_bucket.sort()
    
    def init_answer(self,pirate_number):
        ret = []
        i = 0
        #init answer
        while i < pirate_number:
            ret.append([])
            i += 1
        return ret
    
    def compute_bucket_size(self, loot, pirate_number):
        bucket_size = 0
        for l in loot:
            bucket_size += l
        return bucket_size/pirate_number