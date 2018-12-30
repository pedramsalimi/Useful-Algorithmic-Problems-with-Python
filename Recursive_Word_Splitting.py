def recursive_word_splitter(s,l,output=None):

    if output is None:
        output = []

    for word in l:
        if s.startswith(word):
            output.append(word)
            return recursive_word_splitter(s[len(word):],l,output)
    return output

print(recursive_word_splitter('whysoserious',['why','so','serious']))
