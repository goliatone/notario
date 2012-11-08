import unittest, pprint
from cement.utils import test
import os, imp

#parentdir = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
import notable
#notable = imp.load_source('notable',parentdir)
#pprint.pprint(notable)

BANNER = """                                                                                       
     ***** *     **                                                                    
  ******  **    **** *                *                               *                
 **   *  * **    ****                **                              ***               
*    *  *  **    * *                 **                               *                
    *  *    **   *        ****     ********            ***  ****               ****    
   ** **    **   *       * ***  * ********     ****     **** **** * ***       * ***  * 
   ** **     **  *      *   ****     **       * ***  *   **   ****   ***     *   ****  
   ** **     **  *     **    **      **      *   ****    **           **    **    **   
   ** **      ** *     **    **      **     **    **     **           **    **    **   
   ** **      ** *     **    **      **     **    **     **           **    **    **   
   *  **       ***     **    **      **     **    **     **           **    **    **   
      *        ***     **    **      **     **    **     **           **    **    **   
  ****          **      ******       **     **    **     ***          **     ******    
 *  *****                ****         **     ***** **     ***         *** *   ****     
*     **                                      ***   **                 ***             
*                                                                                      
 ** 
 """

class NotableTest(test.CementTestCase):

	app_class = notable.Minion

	def setUp(self):
		super(NotableTest, self).setUp()
		# TODO: Before release, figure out if we want to have also a ~/notable.ini
		self.config_path = os.path.dirname(os.path.abspath(__file__))+'/testconfig.ini'

		self.app = notable.Minion(argv=[], config_files=[self.config_path])
		self.cmd_path = "python %s/notable.py"%parentdir
		

	def tearDown(self):
		pass

	def test_setup(self):
		# print BANNER
		pass

	def test_list(self):
		output = self._exec()
		print output

	def test_new(self):
		self.app = notable.Minion(argv=['-n','Testing'],config_files=[self.config_path])
		self.app.setup()
		self.app.run()
		self.app.close()

	def test_edit(self):
		pass

	def test_open(self):
		pass

	def test_show(self):
		pass

	def test_delete(self):
		pass

	def test_copy(self):
		pass

	def _exec(self, options = ""):
		from commands import getstatusoutput
		(status, output) = getstatusoutput(self.cmd_path)
		return output

def main():
	unittest.main()

if __name__ == '__main__':
	main()
