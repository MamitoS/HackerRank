def mutate_string(string, position, character):
    liste=list(string)
    liste[position]=character
    last=''.join(liste)
    return last

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)