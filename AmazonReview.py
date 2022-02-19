def selectionOption(depo, query):
    result = [];
    if len(query) < 2:
        return result;
    query = query.lower()
    queryList = [query[0:idx] for idx in range(2,len(query)+1,1)]
    datamap = {key: [] for key in queryList}
    depo = [word.lower() for word in depo]
    for word in depo:
        for key in datamap.keys():
            subword = word[0:len(key)]
            if key == subword:
                datamap[key].append(word)
    for item in datamap:
        data = sorted(datamap[item])
        result.append(data[:3])
    return result
    
def main():
    depo = ["mobile","mouse","moneypot","monitor","mouseopad"];
    query = "mouse";
    print(selectionOption(depo, query))
    
    
if __name__=='__main__':
    main()