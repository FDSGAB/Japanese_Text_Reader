import fugashi

class Japanese_Text_Reader():
    
    ignored_characters = ['（', '`', '.', '(', '"', '」', '④', '26', '『', '？', '!', '5', '「', '』', '。', 
                          '\u3000', '1293', '―', '6', '②', '【', '17', '4', '22', '12', '》', '?', '！', 
                          ' 』', '~', '〈', '8', '①', '※', '15', ',', ')', '〉', '  、', '986', ';', '】', 
                          '⑤', '、', ' 。', '③', ':', '´', ' \u3000', '23', '3807', '3', '○', '～', '）', 
                          '《', '\u2009', '19', "'",'／','+', '-', '1', '59', '64', '77', '84', '85', '87', 
                          '88', '…','］', '［', 'Ｋ', '＋', '＃', '：']
    tagger = None

    def __init__(self) -> None:
        self.tagger = fugashi.Tagger()

    def create_word_list(self, txt_file : str) -> list:
        with open(txt_file, 'r', encoding='utf-8') as f:
            text = f.read()
            words = [word.surface for word in self.tagger(text)] #Need more research on what does .surface do
            words = [word for word in words if word not in self.ignored_characters]
            return words
    
    def create_word_set(self, txt_file : str) -> set:
        words = self.create_word_list(txt_file)
        word_set = sorted(set(words), reverse=True)
        return word_set
    
    def create_frequency_counter_list(self, txt_file : str) -> list:
        word_list = self.create_word_list(txt_file)
        word_set = self.create_word_set(txt_file)
        word_set_frequency_list = list()
        word_no = 0
        for word in word_set:
            frequency = 0
            word_no = word_no + 1
            for word_element in word_list:
                if word_element == word:
                    frequency = frequency + 1
            word_set_frequency_list.append((word,frequency)) 
        return word_set_frequency_list

    """ def create_word_frequency_list(self, txt_file : str) -> dict:      
        word_set = self.create_word_set(txt_file)
        frequency_counter_list = self.frequency_counter_list(txt_file)
        word_frequency_dictionary = dict()
        for counter in range(0,len(word_set),1):
            word_frequency_dictionary[frequency_counter_list[counter]] = word_set[counter]
        return word_frequency_dictionary """
        

if __name__ == '__main__':
    reader = Japanese_Text_Reader()
    print(reader.create_word_set(txt_file='./Japanese_Text_Reader/test_txt_files/makuranosoushi.txt'))
    #word_set = reader.create_frequency_counter_list(txt_file='./Japanese_Text_Reader/test_txt_files/makuranosoushi.txt')
    #print(word_set)
    #print(len(word_set))
  