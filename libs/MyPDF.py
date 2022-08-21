import os
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter, PdfMerger, PdfReader, PdfWriter

class MyPDF():
    def __init__(self, path):
        self.calc_path(path)
        self.reader = PdfReader(path)
        self.total_page = len(self.reader.pages)
        self.metadata = self.reader.metadata
        self.pages = self.reader.pages
    
    def calc_path(self, path):
        if "/" in path:
            locs = path.split("/")
            self.sep = "/"
        else:
            locs = path.split("\\")
            self.sep = "\\"
        self.file_name = locs[len(locs) - 1]
        self.file_location = self.sep.join(locs[:len(locs) - 1])
        name = self.file_name.split(".")
        self.extension = name[len(name) - 1]
        self.name_only = ".".join(name[:len(name) - 1])
    
    def split_n(self, num = 2):
        split_at = self.total_page // num
        rem = self.total_page % num
        
        if rem > 0:
            split_at += 1
        
        out_loc = f'{self.file_location}{self.sep}{self.name_only}'
        
        try:
            os.mkdir(out_loc)
        except Exception as e:
            print(e)
        
        for index, file in enumerate(range(num)):
            writer = PdfWriter()
            start = file * split_at
            stop = self.total_page if file == (num - 1) else file * split_at + split_at
            print(f'{start} - {stop}')
            for page in range(start, stop):
                self.reader.pages[page].compress_content_streams()
                writer.add_page(self.reader.pages[page])
            with open(f'{out_loc}{self.sep}{index}.{self.extension}', "wb") as f:
                writer.write(f)
    
    