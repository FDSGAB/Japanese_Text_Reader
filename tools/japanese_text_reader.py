import fugashi

class Japanese_Text_Reader():
    
    ignored_characters = ['（', '`', '.', '(', '"', '」', '④', '『', '？', '!', '「', '』', '。', 
                          '\u3000', '―', '②', '【', '》', '?', '！', ' 』', '~', '〈', '①', '※', 
                          ',', ')', '〉', '  、', ';', '】', '⑤', '、', ' 。', '③', ':', '´', 
                          ' \u3000', '○', '～', '）', '《', '\u2009', "'",'／','+', '-','…','］', 
                          '［', 'Ｋ', '＋', '＃', '：'] 
    tagger = None

    def __init__(self) -> None:
        self.tagger = fugashi.Tagger()

    def create_word_list(self, txt_file : str, filtered : bool = True) -> list:
        with open(txt_file, 'r', encoding='utf-8') as f:
            text = f.read()
            words = [word.surface for word in self.tagger(text)] #Need more research on what does .surface do
            if filtered:
                words = [word for word in words if word not in self.ignored_characters]
                for word in words: #REMOVES NUMBERS
                    try:
                        float(word)
                        words.remove(word)
                    except:
                        pass
            return words
    
    def create_word_set(self, txt_file : str, filtered : bool = True) -> set:
        words = self.create_word_list(txt_file, filtered)
        word_set = sorted(set(words))
        return word_set
    
    def create_word_frequency_tuple_list(self, txt_file : str, filtered : bool = True) -> list:
        word_list = self.create_word_list(txt_file, filtered)
        word_set = self.create_word_set(txt_file, filtered)
        word_set_frequency_list = list()
        word_no = 0
        for word in word_set:
            frequency = 0
            word_no = word_no + 1
            for word_element in word_list:
                if word_element == word:
                    frequency = frequency + 1
            word_set_frequency_list.append((frequency,word)) 
        return sorted(word_set_frequency_list, reverse=True)

    def create_most_frequent_words_dictionary(self, txt_file : str, filtered : bool = True) -> dict: #STRANGE OUTPUT INVERSTS FREQUENCY AND WORD SOMETIMES
        frequency_word_list = self.create_word_frequency_tuple_list(txt_file, filtered)
        word_frequency_dictionary = dict()
        counter = 0
        for word in frequency_word_list:
            word_frequency_dictionary[counter + 1] = {word[1], word[0]}
            counter = counter + 1
        return word_frequency_dictionary
    
    def occurences_of_word(self, word : str, txt_file : str, filtered : bool = True) -> int:
        word_list = self.create_word_list(txt_file, filtered)
        occurences = 0
        for element in word_list:
            if word == element:
                occurences = occurences + 1
        return occurences
    
    def words_counter(self, txt_file : str, filtered : bool = True) -> int:
        return len(self.create_word_list(txt_file, filtered))
    
    def unique_words_counter(self, txt_file : str, filtered : bool = True) -> int:
        return len(self.create_word_set(txt_file, filtered))
    
    def __repr__(self) -> str:
        return "Object to help processing japanese text files."
        

if __name__ == '__main__':
    reader = Japanese_Text_Reader()
    #frequencies = reader.occurences_of_word(word='私',txt_file='./Japanese_Text_Reader/test_txt_files/makuranosoushi.txt')
    #print(frequencies)
    #print(frequencies)
    #word_set = reader.unique_words_counter(txt_file='./Japanese_Text_Reader/test_txt_files/kojiki.txt')
    #print(word_set)
    #print(len(word_set))
    word_set = reader.unique_words_counter(txt_file='./Japanese_Text_Reader/test_txt_files/makuranosoushi.txt')
    word_set_unfiltered = reader.unique_words_counter(txt_file='./Japanese_Text_Reader/test_txt_files/makuranosoushi.txt', filtered = False)
    print(word_set)
    print(word_set_unfiltered)
    frequencies = reader.create_word_set(txt_file='./Japanese_Text_Reader/test_txt_files/makuranosoushi.txt')
    frequencies_unfiltered = reader.create_word_set(txt_file='./Japanese_Text_Reader/test_txt_files/makuranosoushi.txt', filtered=False)
    print(frequencies)
    print(frequencies_unfiltered)