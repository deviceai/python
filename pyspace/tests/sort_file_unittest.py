import unittest

from mycode.sort_file import sort_file


class TestSort(unittest.TestCase):
    def test_sort_file(self):
        #assert sort_file('4,1,d') == '1,4,d'
        # assert sort_file('b\ny\na') == 'a\nb\ny'
        #
        # # A string with only one item per row
        # assert sort_file('b\ny\na') == 'a\nb\ny'
        # assert sort_file('b\ny\na', '\n') == 'a\nb\ny'
        # #
        # # # Providing some keyword arguments
        assert sort_file('b,b\ny,y\na,a', outsep=':') == 'a:a\nb:b\ny:y'
        assert sort_file('b,b\ny,y\na,a', outsep=':', outend='\t') == 'a:a\tb:b\ty:y'
        # #
        # # # # A string with only one item per row
        assert sort_file('b\ny\na') == 'a\nb\ny'
        # # #
        # # # # Providing some keyword arguments
        assert sort_file('b,b\ny,y\na,a', outsep=':', outend='\t') == 'a:a\tb:b\ty:y'
        # #
        # # # Blank lines and lines starting with '#' should not appear in the result
        assert sort_file('b,q\n\n#p,y\na,o', outsep='-') == 'a-o\nb-q'
        # #
        # # # Proper sorting and ignore blank lines at the end
        assert sort_file('2,3,d\n2,4,x\n2,4,a\n\n\n', outend=' -- end\n') == '2,3,d -- end\n2,4,a -- end\n2,4,x'
        #
        # #additional tests
        assert sort_file('2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a') == '1,4,d\n2,3,d\n2,4,a\n2,4,x\n8,2,z'

