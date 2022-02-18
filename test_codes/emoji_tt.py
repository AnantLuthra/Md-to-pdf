import emoji

class EmojiConverter:
    """
    This class is used to convert all emoji short names and emoticons known as short emojies.
    
    Usage - 

    data = "> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum: \n\
    > \n\
    > Shortcuts (emoticons): :-) :-( 8-) ;)\n\
    test :clap: thanks\n\
    Thank to all who are contributed in this project :100: :)"

    First make an instance of class, and pass a string with multiple lines which contains emojie names
    to be converted.

    a = EmojiConverter(data)

    And run convert_emoji function.

    print(a.convert_emoji())

    OUTPUT - 
    > Classic markup: 😉 :crush: 😢 :tear: 😆 😋 
    >
    > Shortcuts (emoticons): 😊 😞 8-) 😉
    test 👏 thanks
    Thank to all who are contributed in this project 💯 😊

    """
    EMOJI = {
        '😊': ':) :-) :] :-] =) =] ^^ ^_^ ☺'.split(),
        '😉': ';) ;-) ;] ;-]'.split(),
        '😄': ':D :-D =D'.split(),
        '😂': ":,D :'D =,D ='D".split(),
        '😆': 'xD XD'.split(),
        '😛': ':p :-p :P :-P =p =P'.split(),
        '😜': ';p ;-p ;P ;-P'.split(),
        '😏': ':> :->'.split(),
        '😞': ':( :-( ;( ;-( =( =[ ☹'.split(),
        '😣': 'x( X('.split(),
        '😢': ":,( :'( =,( ='(".split(),
        '😠': '>:( >=('.split(),
        '😲': ':O :-O 8-O =O'.split(),
        '😵': 'x-O X-O'.split(),
        '😳': ':$ :-$ :">'.split(),
        '😴': ':zzz:'.split(),
        '😓': ':-X :X :-# :# :-& :&'.split(),
        '😇': 'O:) O:-)'.split(),
        '😈': '3:) 3:-) >:) >:-) >;) >;-)'.split(),
        '😎': '8)'.split(),
        '😖': ':s :-s :S :-S'.split(),
        '😒': ':/ :-/ :\\ :-\\ =/ =\\ :L'.split(),
        '😚': ':* :-*'.split(),
        '😘': ';* ;-*'.split(),
        '❤': '<3'.split(),
        '💔': '</3'.split(),
        '👍': ':y: :Y: :+1:'.split(),
        '👎': ':n: :N: :-1:'.split(),
        '🙌': '\\o/'.split(),
        '🍰': ':cake:'.split(),
        '😸': ':^) :} :-} :3 :-3'.split(),
        '😺': ':^D =^D'.split(),
        '😿': ':^( :{'.split(),
    }

    def __init__(self, data:str) -> None:

        self.data = data
    
    def __search_emoji(self, data:str) -> list:

        """This Function searches where the emojies are present in the given string
        through spliting the string with splitlines and searching for ':' in lines 
        and it returns a list of index of those lines who contains ':' in them, and 
        list of those lines."""

        # Spliting lines
        __lines = data.splitlines()
        __colon = 0
        __line_having_colon = []
        
        # Searching for ':' in those lines for emoji replacement.
        for index, i in enumerate(__lines):
            for character in i:
                if character == ":":
                    if __colon != 0:
                        __line_having_colon.append(index)
                        __colon = 0
                        break
                    else:
                        __colon += 1
                    
        return __line_having_colon, __lines
    

    @classmethod
    def __convert_emoticons(cls, word: str) -> str:

        """This function takes one argument string and check there is any emoticons in it
        or not if yes it will convert it in emoji and return it as a string"""

        for item,values in cls.EMOJI.items():
            for i in values:
                if i == word:
                    return item
        
        else:
            return 0

    def __search_emoticons(self, data: str) -> list:
        """This function searches for shortcut (emoticons) in the given data."""

        # Spliting all lines of code into a list elements through .splitlines()
        __data = data.splitlines()

        # Checking each element of list.
        for i in range(len(__data)):

            # Spliting each line with " " so every word will be in seperate element of list
            __line = __data[i].split(" ")

            for x in range(len(__line)):

                if "https:/" in __line[x]:
                    ...

                else:
                    # Getting converted emojies from this fuction.
                    check = self.__convert_emoticons(__line[x])

                    if check == 0: ...
                    else: __line[x] = check

            else:
                __line = " ".join(__line)
                __data[i] = __line

        return "\n".join(__data)

    def __give_emoji(self, emojii: str):
        """This function returns emoji at the place of this :sweat_smile:"""

        try:
            emojii = emoji.emojize(emojii, use_aliases=True)
        except Exception as e:
            print(e)

        return emojii

    def __main_emoji_function(self, data:str) -> str:
        """This function contains main implementation of emoji segment"""

        __content = self.__search_emoji(data)

        # Sending those lines of list which contains ':' to convert them into emoji
        for i in __content[0]:
            __content[1][i] = self.__give_emoji(__content[1][i])

        return "\n".join(__content[1])

    def convert_emoji(self):
        """This function takes string in which all lines are present including emojies
        whether it is like - :"""

        # Getting emoticons shortcut emojies converted into emoji
        __emoticon_converted = self.__search_emoticons(self.data)

        # Sending whole data for conversion of emoji names to emoji
        return self.__main_emoji_function(__emoticon_converted)
