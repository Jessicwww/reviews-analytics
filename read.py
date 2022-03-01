data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('end of the reviews, total', len(data), 'reviews')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('average length of reviews is', sum_len/len(data))


new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('length is less than 100,', len(new), 'reviews')