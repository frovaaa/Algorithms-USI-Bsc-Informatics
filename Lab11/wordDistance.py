from collections import defaultdict, deque

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]


# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log"]

def wordDistance(beginWord, endWord, wordList) -> int:
    neighMap = createMap(wordList)
    bfsQueue = deque()
    visited = set()
    bfsQueue.append((beginWord, 1))
    visited.add(beginWord)

    while len(bfsQueue) > 0:
        (cW, cDist) = bfsQueue.popleft()

        for i in range(len(cW)):
            intrW = cW[:i] + "#" + cW[i + 1:]

            for neighbour in neighMap[intrW]:
                if neighbour not in visited:
                    if neighbour == endWord:
                        return cDist + 1
                    bfsQueue.append((neighbour, cDist + 1))
                    visited.add(neighbour)
    return 0

def createMap(wordList):
    d = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            intrW = word[:i] + "#" + word[i + 1:]
            d[intrW].append(word)
    return d


print(wordDistance(beginWord, endWord, wordList))
