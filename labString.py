class string :
    """
        A simple class to represent a string default method.
        with this class string manipulation is implemented.
    """
    def capital(s):
        """
        This function returns the Capitalized version of the string.
        input : s is a string
        """
        return s.capitalize()
          
    def upperCase(s):
        """
        This function returns the Upper case version of the string.
        """
        return s.upper()
          
    def lowerCase(s):
        """
        This function returns the Lower case version of the string.
        """
        return s.lower()
          
    def trim(s):
        """
        This function returns the trimmed version of the string.
        """
        return s.strip()
        
    def replace(s, value, replacement):
        """
        This function returns the replace a part of the string to another.
        """
        return s.replace(value, replacement)
          
    def split(s):
        """
        This function returns splinted array of string elements..
        """
        return s.split()
          
    def join(s, option):
        """
        This function returns joined splinted array of string elements..
        """
        if option == ',':
            return ','.join(s)
        else :
            return ''.join(s)