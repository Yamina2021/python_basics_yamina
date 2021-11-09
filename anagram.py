class Anagram:
   def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted(i))
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Anagram()
print(ob1.groupAnagrams(['listen', 'enlists', 'google', 'inlets', 'banana']))
