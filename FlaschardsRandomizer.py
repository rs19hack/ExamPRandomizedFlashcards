"""
Coaching Actuaries
Exam P Mobile Flashcards Randomized Program

Michael Goulet
Profile Insurance Group
goulet.michaelrobert@gmail.com
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

sys.setrecursionlimit(2000)
STARTPAGE = [3,37,47,49,63,91,119,131,151,153,157,191,213,225,247,267,289,311,321,327,349,367,399,417]
ENDPAGE = [36,46,48,60,90,118,130,150,152,156,190,212,222,246,266,288,310,320,326,348,364,398,416,422]
SECTION11 = list(range(3,37))
SECTION12 = list(range(37,47))
SECTION13 = list(range(47,49))
SECTION14 = list(range(49, 61))
SECTION21
SECTION22

inputpdf = PdfFileReader(open("C:/Users/Rochester/DesktopExamPFlashcards.pdf", "rb"))

