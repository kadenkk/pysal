import unittest
import pysal
from pysal.core.IOHandlers.dat import DatIO
import tempfile
import os

class test_DatIO(unittest.TestCase):
    def setUp(self):
        self.test_file = test_file = '../../../examples/wmat.dat'
        self.obj = DatIO(test_file, 'r')

    def test_close(self):
        f = self.obj
        f.close()
        self.failUnlessRaises(ValueError, f.read)

    def test_read(self):
        w = self.obj.read()
        self.assertEqual(49, w.n)
        self.assertEqual(4.7346938775510203, w.mean_neighbors)
        self.assertEqual([0.5, 0.5], w[5.0].values())

    def test_seek(self):
        self.test_read()
        self.failUnlessRaises(StopIteration, self.obj.read)
        self.obj.seek(0)
        self.test_read()

    def test_write(self):
        w = self.obj.read()
        f = tempfile.NamedTemporaryFile(suffix='.dat',dir="../../../examples")
        fname = f.name
        f.close()
        o = pysal.open(fname,'w')
        o.write(w)
        o.close()
        wnew =  pysal.open(fname,'r').read()
        self.assertEqual( wnew.pct_nonzero, w.pct_nonzero)
        os.remove(fname)

if __name__ == '__main__':
    unittest.main()
