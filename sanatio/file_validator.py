import os

from sanatio.base_class import BaseValidator


class FileValidator(BaseValidator):

    def isFile(self, value) -> bool:
        """ check if the string is file or not """
        return os.path.isfile(value)

    def isFileType(self, value, extensions) -> bool:
        """ check if the string is of a specific file type """
        return self.isFile(value) and value.endswith(extensions)

    def isImage(self, value) -> bool:
        """ check if the string is image or not """
        extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp')
        return self.isFileType(value, extensions)

    def isVideo(self, value) -> bool:
        """ check if the string is video or not """
        extensions = ('.mp4', '.mkv', '.avi', '.flv', '.wmv', '.mov')
        return self.isFileType(value, extensions)

    def isAudio(self, value) -> bool:
        """ check if the string is audio or not """
        extensions = ('.mp3', '.wav', '.ogg', '.aac', '.wma', '.flac')
        return self.isFileType(value, extensions)

    def isPDF(self, value) -> bool:
        """ check if the string is PDF or not """
        extensions = ('.pdf')
        return self.isFileType(value, extensions)

    def isCSV(self, value) -> bool:
        """ check if the string is CSV or not """
        extensions = ('.csv')
        return self.isFileType(value, extensions)

    def isExcel(self, value) -> bool:
        """ check if the string is Excel or not """
        extensions = ('.xls', '.xlsx')
        return self.isFileType(value, extensions)

    def isWord(self, value) -> bool:
        """ check if the string is Word or not """
        extensions = ('.doc', '.docx')
        return self.isFileType(value, extensions)

    def isPowerPoint(self, value) -> bool:
        """ check if the string is PowerPoint or not """
        extensions = ('.ppt', '.pptx')
        return self.isFileType(value, extensions)

    def isText(self, value) -> bool:
        """ check if the string is Text or not """
        extensions = ('.txt')
        return self.isFileType(value, extensions)

    def isZip(self, value) -> bool:
        """ check if the string is Zip or not """
        extensions = ('.zip')
        return self.isFileType(value, extensions)

    def isGzip(self, value) -> bool:
        """ check if the string is Gzip or not """
        extensions = ('.gz')
        return self.isFileType(value, extensions)

    def isTar(self, value) -> bool:
        """ check if the string is Tar or not """
        extensions = ('.tar')
        return self.isFileType(value, extensions)

    def isRar(self, value) -> bool:
        """ check if the string is RAR or not """
        extensions = ('.rar')
        return self.isFileType(value, extensions)

    def is7z(self, value) -> bool:
        """ check if the string is 7z or not """
        extensions = ('.7z')
        return self.isFileType(value, extensions)

    def isJSON(self, value) -> bool:
        """ check if the string is JSON or not """
        extensions = ('.json')
        return self.isFileType(value, extensions)

    def isXML(self, value) -> bool:
        """ check if the string is XML or not """
        extensions = ('.xml')
        return self.isFileType(value, extensions)

    def isYAML(self, value) -> bool:
        """ check if the string is YAML or not """
        extensions = ('.yaml', '.yml')
        return self.isFileType(value, extensions)

    def isINI(self, value) -> bool:
        """ check if the string is INI or not """
        extensions = ('.ini')
        return self.isFileType(value, extensions)

    def isConfig(self, value) -> bool:
        """ check if the string is Config or not """
        extensions = ('.config')
        return self.isFileType(value, extensions)

    def isLog(self, value) -> bool:
        """ check if the string is Log or not """
        extensions = ('.log')
        return self.isFileType(value, extensions)

    def isSQL(self, value) -> bool:
        """ check if the string is SQL or not """
        extensions = ('.sql')
        return self.isFileType(value, extensions)

    def isHTML(self, value) -> bool:
        """ check if the string is HTML or not """
        extensions = ('.html')
        return self.isFileType(value, extensions)

    def isCSS(self, value) -> bool:
        """ check if the string is CSS or not """
        extensions = ('.css')
        return self.isFileType(value, extensions)

    def isJS(self, value) -> bool:
        """ check if the string is JS or not """
        extensions = ('.js')
        return self.isFileType(value, extensions)

    def isPHP(self, value) -> bool:
        """ check if the string is PHP or not """
        extensions = ('.php')
        return self.isFileType(value, extensions)

    def isPython(self, value) -> bool:
        """ check if the string is Python or not """
        extensions = ('.py')
        return self.isFileType(value, extensions)

    def isJava(self, value) -> bool:
        """ check if the string is Java or not """
        extensions = ('.java')
        return self.isFileType(value, extensions)

    def isC(self, value) -> bool:
        """ check if the string is C or not """
        extensions = ('.c')
        return self.isFileType(value, extensions)

    def isCPP(self, value) -> bool:
        """ check if the string is CPP or not """
        extensions = ('.cpp')
        return self.isFileType(value, extensions)

    def isCSharp(self, value) -> bool:
        """ check if the string is CSharp or not """
        extensions = ('.cs')
        return self.isFileType(value, extensions)

    def isRuby(self, value) -> bool:
        """ check if the string is Ruby or not """
        extensions = ('.rb')
        return self.isFileType(value, extensions)

    def isSwift(self, value) -> bool:
        """ check if the string is Swift or not """
        extensions = ('.swift')
        return self.isFileType(value, extensions)

    def isKotlin(self, value) -> bool:
        """ check if the string is Kotlin or not """
        extensions = ('.kt')
        return self.isFileType(value, extensions)

    def isR(self, value) -> bool:
        """ check if the string is R or not """
        extensions = ('.r')
        return self.isFileType(value, extensions)

    def isGo(self, value) -> bool:
        """ check if the string is Go or not """
        extensions = ('.go')
        return self.isFileType(value, extensions)

    def isScala(self, value) -> bool:
        """ check if the string is Scala or not """
        extensions = ('.scala')
        return self.isFileType(value, extensions)

    def isPerl(self, value) -> bool:
        """ check if the string is Perl or not """
        extensions = ('.pl')
        return self.isFileType(value, extensions)

    def isShell(self, value) -> bool:
        """ check if the string is Shell or not """
        extensions = ('.sh')
        return self.isFileType(value, extensions)

    def isBatch(self, value) -> bool:
        """ check if the string is Batch or not """
        extensions = ('.bat')
        return self.isFileType(value, extensions)

    def isPowerShell(self, value) -> bool:
        """ check if the string is PowerShell or not """
        extensions = ('.ps1')
        return self.isFileType(value, extensions)
