import os

class FileValidator:
    
    def __init__(self) -> None:
        pass
    
    def isFile(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is file or not """
        if os.path.isfile(value):
            return True
        return False
        
    
    def isImage(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is image or not """
        extensions =('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
        
    
    def isVideo(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is video or not """
        extensions = ('.mp4', '.mkv', '.avi', '.flv', '.wmv', '.mov')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False

    def isAudio(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is audio or not """
        extensions = ('.mp3', '.wav', '.ogg', '.aac', '.wma', '.flac')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isPDF(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is PDF or not """
        extensions = ('.pdf')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isCSV(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is CSV or not """
        extensions = ('.csv')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isExcel(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Excel or not """
        extensions = ('.xls', '.xlsx')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isWord(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Word or not """
        extensions = ('.doc', '.docx')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isPowerPoint(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is PowerPoint or not """
        extensions = ('.ppt', '.pptx')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isText(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Text or not """
        extensions = ('.txt')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isZip(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Zip or not """
        extensions = ('.zip')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isGzip(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Gzip or not """
        extensions = ('.gz')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isTar(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Tar or not """
        extensions = ('.tar')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isRar(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is RAR or not """
        extensions = ('.rar')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def is7z(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is 7z or not """
        extensions = ('.7z')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isJSON(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is JSON or not """
        extensions = ('.json')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isXML(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is XML or not """
        extensions = ('.xml')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isYAML(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is YAML or not """
        extensions = ('.yaml', '.yml')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isINI(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is INI or not """
        extensions = ('.ini')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isConfig(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Config or not """
        extensions = ('.config')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isLog(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Log or not """
        extensions = ('.log')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isSQL(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is SQL or not """
        extensions = ('.sql')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isHTML(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is HTML or not """
        extensions = ('.html')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isCSS(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is CSS or not """
        extensions = ('.css')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isJS(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is JS or not """
        extensions = ('.js')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isPHP(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is PHP or not """
        extensions = ('.php')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isPython(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Python or not """
        extensions = ('.py')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isJava(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Java or not """
        extensions = ('.java')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isC(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is C or not """
        extensions = ('.c')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isCPP(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is CPP or not """
        extensions = ('.cpp')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isCSharp(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is CSharp or not """
        extensions = ('.cs')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isRuby(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Ruby or not """
        extensions = ('.rb')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isSwift(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Swift or not """
        extensions = ('.swift')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isKotlin(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Kotlin or not """
        extensions = ('.kt')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isR(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is R or not """
        extensions = ('.r')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isGo(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Go or not """
        extensions = ('.go')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isScala(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Scala or not """
        extensions = ('.scala')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isPerl(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Perl or not """
        extensions = ('.pl')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
    
    def isShell(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is Shell or not """
        extensions = ('.sh')
        if self.isFile(value):
            if value.endswith(extensions):
                return True
        return False
