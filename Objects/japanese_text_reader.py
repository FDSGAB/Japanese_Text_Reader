import fugashi

class Japanese_Text_Reader():

    tagger = None

    def __init__(self) -> None:
        self.tagger = fugashi.Tagger()

    def create_word_list(self, txt_file : str) -> list:
        with open(txt_file, 'r', encoding='utf-8') as f:
            text = f.read()
            words = self.tagger(text)
            return words
    
    def create_word_set(self, txt_file : str) -> set:
        words = self.create_word_list(txt_file)
        word_set = set(words)
        return word_set
    
    def frequency_counter_list(self, txt_file : str) -> list: #NOT WORKING PROPERLY
        word_list = self.create_word_list(txt_file)
        word_set = self.create_word_set(txt_file)
        word_set_frequency_list = list()
        for word in word_set:
            print(word)
            frequency = 0
            for word_element in word_list:
                if word_element == word:
                    frequency = frequency + 1
                    print(frequency)
            word_set_frequency_list.append(frequency) 
        return word_set_frequency_list

    def create_word_frequency_dictionary(self, txt_file : str) -> dict:      
        word_list = self.create_word_list(txt_file)
        word_frequency_dictionary = dict()
        for counter in range(0,len(word_list),1):
            word_frequency_dictionary[counter+1] = word_list[counter]
        return word_frequency_dictionary
        

if __name__ == '__main__':
    reader = Japanese_Text_Reader()
    word_set = reader.frequency_counter_list(txt_file='./test_txt_files/makuranosoushi.txt')
    print(word_set)