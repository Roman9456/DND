def vote(votes):
    count = []
    for i in votes:
        count.append(votes.count(i))
    max_times = max(count)
    n = count.index(max_times)
    return (votes[n])

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))