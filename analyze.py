# encoding: utf-8
import corpus
import htmltable

def unique_words (sentences, boundaries=False, reverse=False, punctuation=u"ᐨᐤᐦ"):
    words = set()
    for sentence in sentences:
        tokens = sentence.split()
        for glyph in punctuation:
            tokens = [token.replace(glyph, "") for token in tokens]
        if boundaries:
            words.update(["{" + word + "}" for word in tokens])
        else:
            words.update(tokens)

    if reverse:
        words = [word[::-1] for word in words]

    return words

def unique_glyphs (words):
    glyphs = set()
    for word in words:
        glyphs.update(word)

    return glyphs

def glyph_transitions (words, glyphs):
    # build empty transition table
    trans = {}
    for glyph in glyphs:
        temp = {}
        trans[glyph] = temp.fromkeys(glyphs, 0)

    # populate the transition table
    for word in words:
        for idx in range(len(word)-1):
            glyph_from, glyph_to = word[idx], word[idx+1]
            trans[glyph_from][glyph_to] += 1


    return trans

def output_transitions (trans, glyphs):
    print "<table>"
    htmltable.row(['Symbol', 'Transition', 'Occurrences (percentage)'])

    for glyph_from in glyphs:
        # sum total transitions
        count = 0
        for glyph_to in glyphs:
            count += trans[glyph_from][glyph_to]
        # output result
        if count == 0:
            continue

        first_entry = True
        for glyph_to in glyphs:
            t = trans[glyph_from][glyph_to]
            if t > 0:
                if not first_entry:
                    cells = ['&nbsp;', glyph_to, '%i (%.2f%%)' % (t, (t*100.)/count)]
                else:
                    cells = [glyph_from, glyph_to, '%i (%.2f%%)' % (t, (t*100.)/count)]
                    first_entry = False
                print htmltable.row(cells)
    print "</table>"    


def word_length (words):
    lengths = [len(word)-2 for word in words]
    print lengths

    for l in range(1, 15):
        print l, "->", lengths.count(l), lengths.count(l)/float(len(lengths))
    
if __name__ == "__main__":
    # collect initial information
    sentences = corpus.read_sentences()
    words = unique_words(sentences, boundaries=True)
    glyphs = unique_glyphs(words)

    # get transitions and output them
    transitions = glyph_transitions(words, glyphs)
    output_transitions(transitions, glyphs)

    #word_length(words)
