def read_sentences ():
    handler = file("corpus.txt")
    lines = handler.readlines()
    handler.close()

    lines = [line.decode("utf-8") for line in lines]
    lines = [line.split("#")[0].strip() for line in lines]
    lines = [line for line in lines if line]

    return lines

if __name__ == "__main__":
    print "Showing Beanish corpus:"
    print "======================="
    for sentence in read_sentences():
        print sentence
