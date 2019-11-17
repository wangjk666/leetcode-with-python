def generateSentences(synonyms, text):
        p, text = {}, text.split()
        for i, j in synonyms:
            
            p[i], p[j] = p.get(i, [i]), p.get(j, [j])
            print(p[i],p[j])
            if p[i] is not p[j]:
                p[i].extend(p[j])
                for k in p[j]:
                    p[k] = p[i]
            print(p[i],p[j])
        ans, n = [], len(text)
        def f(i, t):
            if i == n:
                ans.append(' '.join(t))
            else:
                g = lambda x: f(i + 1, t + [x])
                [*map(g, p[text[i]] if text[i] in p else [text[i]])]
        f(0, [])
        return sorted(ans)
    


print(generateSentences([["happy","joy"],["sad","sorrow"],["joy","cheerful"]],"I am happy today but was sad yesterday"))