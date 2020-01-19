import re

string = "abcdef acegik bdfhjl fedcba"
print(re.sub("[ad]", "S", string)) #a or d will be replaced by S all times
print(re.sub("[ad]", "S", string, 2)) #a or d will be replaced by S for first 2 times
print(re.sub("ab", "S", string)) #ab will be replaced by S for all times
print(re.sub("[af][be]", "S", string)) #If first char is a or f and second char is b or e
print(re.sub("a.c", "#", string)) #First a, 2nd any and 3rd c replaced by #
print(re.sub("a..g", "#", string)) #First a, 2nd, 3rd any and 4th g replaced by #
print(re.sub("AB+", "$", "AB BABB AC ABBBBBB")) #AB occurances of any will be replaced by $
print(re.sub("AB{2,5}", "$", "AB BABB AC ABBBBBB ABBBBBBBBBB")) #AB occurances of 2 to 5 will be replaced by $

some = "abcdefabcabc"
print(re.sub("abc", "%", some)) #Replace all abc with %
print(re.sub("^abc", "%", some)) #Replace all abc only if at start
print(re.sub("abc$", "%", some)) #Replace all abc only if at end

string = "here is a string"
print(re.search("ng$", string)) #Matches pattern anywhere in string
print(re.search("is", string)) #Matches pattern anywhere in string
print(re.search("id", string))
print(re.match("is", string)) #Matches only at start of string
print(re.match("he", string)) #Matches only at start of string
print(re.search("^he", string)) #Matches only at start of string which is same as match