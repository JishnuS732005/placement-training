#  https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    num_substring=len(string)//k
    for i in range(num_substring):
        t=string[i*k:(i+1)*k]
        seen=set()
        u=''
        for char in t:
            if char not in seen:
                seen.add(char)
                u+=char
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
