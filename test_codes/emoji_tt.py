"""
Have to figure out what method to use for getting emoji from the emoticons
1. Directly pass out the 
"""


import emoji
import emot


class EmojiConverter:
    
    def __init__(self, data:str) -> None:
        self.data = data

    def _search_emoji(self, data:str) -> list:

        """This Function searches where the emojies are present in the given string
        through spliting the string with splitlines and searching for ':' in lines 
        and it returns a list of index of those lines who contains ':' in them."""

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
      
    def _emoticons_converter(self):
        """This function make emoji in the place of emoticons."""

        emot_obj = emot.core.emot() 
        bulk_test = ["I love python ☮ 🙂 ❤ :-) :-( :-)))", "I love python\
        🙂 ❤ :-) :-( :-)))", "I love python ☮ ❤ :-) :-( :-)))", "I love python ☮ 🙂 :-( :-)))"]
        # emot_obj.bulk_emoji(bulk_test) 
        return emot_obj.bulk_emoticons(bulk_test)
    
    def give_emoji(self, emojii: str):
        """This function returns emoji at the place of this :sweat_smile:"""

        try:
            emojii = emoji.emojize(emojii, use_aliases=True)
        except Exception as e:
            print(e)

        return emojii

    def main_emoji_function(self):
        """This function contains main implementation of emoji segment"""

        __content = self._search_emoji(self.data)

        # Sending those lines of list which contains ':' to convert them into emoji
        for i in __content[0]:
            __content[1][i] = self.give_emoji(__content[1][i])

        return "\n".join(__content[1])

if __name__ == "__main__":
    
    data = "> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum: \n\
> \n\
> Shortcuts (emoticons): :-) :-( 8-) ;)\n\
nacho :clap: thanks\n\
Thank to all who working in this project :100: :)"


    # How to use this class.
    a = EmojiConverter(data)                    # Just make an instance of class
    print(a.main_emoji_function())        # And run main_emoji_function and passing the data as argument.
                                                # To get the required output.
    
    print(a._emoticons_converter())
