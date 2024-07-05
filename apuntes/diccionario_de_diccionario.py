myfamily = {
"1" : {
    "name" : "Emil",
    "year" : 2004
},
"2" : {
    "name" : "Tobias",
    "year" : 2007
},
"3" : {
    "name" : "Linus",
    "year" : 2011
}
} 

print(myfamily["2"]["name"]) 

for p_id, p_info in myfamily.items():
    print("\nFamily ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])