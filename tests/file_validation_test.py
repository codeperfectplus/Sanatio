import os
import sys
import unittest
import shutil

sys.path.append('.')
from sanatio import Sanatio
validator = Sanatio()

test_files_path = r'tests/test_files'
os.makedirs(test_files_path, exist_ok=True)

def create_file(file_name, content='sample content'):
    with open(f'{test_files_path}/{file_name}', 'w') as file:
        file.write(content)


class FileValidationTest(unittest.TestCase):
    def test_isFile_true(self):
        filename = 'filename_exists.txt'
        create_file(filename)
        self.assertTrue(validator.isFile(os.path.join(test_files_path, filename)))

    def test_isFile_false(self):
        filename = 'filename_does_not_exist.txt'
        self.assertFalse(validator.isFile(os.path.join(test_files_path, 'filename_does_not_exist.txt')))

    def test_isImage_true(self):
        filename = 'filename_exists.png'
        create_file(filename)
        self.assertTrue(validator.isImage(os.path.join(test_files_path, filename)))

    def test_isVideo_true(self):
        filename = 'filename_exists.mp4'
        create_file(filename)
        self.assertTrue(validator.isVideo(os.path.join(test_files_path, filename)))
    
    def test_isAudio_true(self):
        filename = 'filename_exists.mp3'
        create_file(filename)
        self.assertTrue(validator.isAudio(os.path.join(test_files_path, filename)))

    def test_isPDF_true(self):
        filename = 'filename_exists.pdf'
        create_file(filename)
        self.assertTrue(validator.isPDF(os.path.join(test_files_path, filename)))

    def test_isCSV_true(self):
        filename = 'filename_exists.csv'
        create_file(filename)
        self.assertTrue(validator.isCSV(os.path.join(test_files_path, filename)))
    
    def test_isExcel_true(self):
        filename = 'filename_exists.xlsx'
        create_file(filename)
        self.assertTrue(validator.isExcel(os.path.join(test_files_path, filename)))

    def test_isWord_true(self):
        filename = 'filename_exists.docx'
        create_file(filename)
        self.assertTrue(validator.isWord(os.path.join(test_files_path, filename)))

    def test_isPowerPoint_true(self):
        filename = 'filename_exists.pptx'
        create_file(filename)
        self.assertTrue(validator.isPowerPoint(os.path.join(test_files_path, filename)))

    def test_isText_true(self):
        filename = 'filename_exists.txt'
        create_file(filename)
        self.assertTrue(validator.isText(os.path.join(test_files_path, filename)))

    def test_isZip_true(self):
        filename = 'filename_exists.zip'
        create_file(filename)
        self.assertTrue(validator.isZip(os.path.join(test_files_path, filename)))

    def test_isGzip_true(self):
        filename = 'filename_exists.tar.gz'
        create_file(filename)
        self.assertTrue(validator.isGzip(os.path.join(test_files_path, filename)))

    def test_isTar_true(self):
        filename = 'filename_exists.tar'
        create_file(filename)
        self.assertTrue(validator.isTar(os.path.join(test_files_path, filename)))

    def test_isRar_true(self):
        filename = 'filename_exists.rar'
        create_file(filename)
        self.assertTrue(validator.isRar(os.path.join(test_files_path, filename)))

    def test_is7z_true(self):
        filename = 'filename_exists.7z'
        create_file(filename)
        self.assertTrue(validator.is7z(os.path.join(test_files_path, filename)))

    def test_isXML_true(self):
        filename = 'filename_exists.xml'
        create_file(filename)
        self.assertTrue(validator.isXML(os.path.join(test_files_path, filename)))

    def test_isYAML_true(self):
        filename = 'filename_exists.yaml'
        create_file(filename)
        self.assertTrue(validator.isYAML(os.path.join(test_files_path, filename)))

    def test_isINI_true(self):
        filename = 'filename_exists.ini'
        create_file(filename)
        self.assertTrue(validator.isINI(os.path.join(test_files_path, filename)))

    def test_isConfig_true(self):
        filename = 'filename_exists.config'
        create_file(filename)
        self.assertTrue(validator.isConfig(os.path.join(test_files_path, filename)))

    def test_isHTML_true(self):
        filename = 'filename_exists.html'
        create_file(filename)
        self.assertTrue(validator.isHTML(os.path.join(test_files_path, filename)))

    def test_isCSS_true(self):
        filename = 'filename_exists.css'
        create_file(filename)
        self.assertTrue(validator.isCSS(os.path.join(test_files_path, filename)))

    def test_isJS_true(self):
        filename = 'filename_exists.js'
        create_file(filename)
        self.assertTrue(validator.isJS(os.path.join(test_files_path, filename)))

    def test_isPHP_true(self):
        filename = 'filename_exists.php'
        create_file(filename)
        self.assertTrue(validator.isPHP(os.path.join(test_files_path, filename)))

    def test_isPython_true(self):
        filename = 'filename_exists.py'
        create_file(filename)
        self.assertTrue(validator.isPython(os.path.join(test_files_path, filename)))

    def test_isJava_true(self):
        filename = 'filename_exists.java'
        create_file(filename)
        self.assertTrue(validator.isJava(os.path.join(test_files_path, filename)))

    def test_isC_true(self):
        filename = 'filename_exists.c'
        create_file(filename)
        self.assertTrue(validator.isC(os.path.join(test_files_path, filename)))

    def test_isCPP_true(self):
        filename = 'filename_exists.cpp'
        create_file(filename)
        self.assertTrue(validator.isCPP(os.path.join(test_files_path, filename)))

    def test_isCSharp_true(self):
        filename = 'filename_exists.cs'
        create_file(filename)
        self.assertTrue(validator.isCSharp(os.path.join(test_files_path, filename)))

    def test_isRuby_true(self):
        filename = 'filename_exists.rb'
        create_file(filename)
        self.assertTrue(validator.isRuby(os.path.join(test_files_path, filename)))

    def test_isGo_true(self):
        filename = 'filename_exists.go'
        create_file(filename)
        self.assertTrue(validator.isGo(os.path.join(test_files_path, filename)))

    def test_isSwift_true(self):
        filename = 'filename_exists.swift'
        create_file(filename)
        self.assertTrue(validator.isSwift(os.path.join(test_files_path, filename)))

    def test_isKotlin_true(self):
        filename = 'filename_exists.kt'
        create_file(filename)
        self.assertTrue(validator.isKotlin(os.path.join(test_files_path, filename)))

    def test_isScala_true(self):
        filename = 'filename_exists.scala'
        create_file(filename)
        self.assertTrue(validator.isScala(os.path.join(test_files_path, filename)))


if __name__ == '__main__':
    unittest.main()