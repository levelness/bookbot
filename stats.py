class Stats:
    def get_num_words(self, text):
        return len(text.split())

    def get_num_characters(self, text):
        dict = {}
        for char in text:
            char = char.lower()
            if char in dict:
                dict[char] = dict[char] + 1
            else:
                dict[char] = 1
        return dict
    
    def get_sorted_characters(self, dict):
        dictionaries = []
        for key in dict:
            dictionaries.append({ "char": key, "count": dict[key] })

        def sort_on(dict):
            return dict["count"]

        dictionaries.sort(key=sort_on, reverse=True)
        return dictionaries
