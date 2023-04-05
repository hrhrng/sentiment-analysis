import json
ids = [
        'Lxf4ZFp0I','LxqLO5jL0','LAxTPBkO5','KkDDY5Wp6',
        'KkLPBf6F5','MxU0gdVSX','Io6pMhCFm','IoQNhzBKy',
        'HD7Tacdz0','H9ttovdft','Gpp686uXS','HEydnk3Bd',
        'ICyHU5YSl','IDsGWARJs','IFHK7gym7','J1gRiyLAu',
        'J8zR7pGvA','J8CmR8zwf','JbWt79Lzy','JoXXvhwwV',
        'JoXf00tap','JBbM3bs8Z','JzZ5moYdL','MjyCK3fjR',
        'MjCbcBxxV','LE5n091bP','LvriorSMO','GaRDRahC6',
        'GaVUmodao','HFjgRh7Sy','JlDDLl5Dg','GFplcu3WU'
    ]
ids1 = ['J8CmR8zwf','JbWt79Lzy','JzZ5moYdL','MjyCK3fjR','MjCbcBxxV','LvriorSMO',]
ids2 = ['MjyCK3fjR','MjCbcBxxV','LvriorSMO']


file1_path = 'E:\WeiboSpider\output\comment_20230402211453.jsonl'
file2_path = 'E:\WeiboSpider\output\comment_20230402213258.jsonl'

data = []

with open(file2_path, 'r', encoding='utf-8') as f:
    for line in f:
        item = json.loads(line)
        if item['tweet_id'] not in ids2:
            data.append(json.loads(line))

with open(file1_path, 'r', encoding='utf-8') as f:
    for line in f:
        item = json.loads(line)
        if item['tweet_id'] not in ids1:
            data.append(json.loads(line))

data2 = sorted(data,key=lambda x:(x['tweet_id'], -x['like_counts']))

file_to = open('./output/all2.json','wt',encoding='utf-8')
file_to.write(json.dumps(data2, ensure_ascii=False))
file_to.flush()
file_to.close()


with open('./output/all2.json','r',encoding='utf-8') as f:
    data = json.loads(f)
    print(data[0])