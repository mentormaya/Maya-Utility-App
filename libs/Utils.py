class Utils:
    def __init__(self) -> None:
        pass

    def split_characters(word):
        return [char for char in word]

    def join_characters(list_s, seprator = ''):
        if list_s != "" or list_s is not None:
            word = ""
            for item in list_s:
                word = word + seprator + item
            return word
        return list_s
    
    def string_reverse(string = ""):
        if string == "":
            return string
        return string[::-1]