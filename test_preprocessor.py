from unittest import TestCase
from preprocessor import cleanUp

class Test(TestCase):
    def test_clean_up_ToLower(self):
        self.assertEqual(cleanUp("hSJAasd"),"hsjaasd")

    def test_clean_up_ExcessSpaces(self):
        self.assertEqual(cleanUp("ht  ds. er.  sdf.     "),"ht ds. er. sdf. ")

    def test_clean_up_NoSpaceAfterPoint(self):
        self.assertEqual(cleanUp("this is very nice.The next time"), "this is very nice. the next time")

    def test_clean_up_Shorthand(self):
        self.assertEqual(cleanUp("this is very nice.The next time z.B."), "this is very nice. the next time z.b.")

    def test_clean_up_RemoveHTMLTags(self):
        self.assertEqual(cleanUp('type specimen<td class="played">0dsf</td> book. '), "type specimen book. ")

    def test_clean_up_ReplaceWithPoints(self):
        self.assertEqual(cleanUp('hallo! I am ? this is very interesting? how about !'), "hallo. i am. this is very interesting. how about.")

    def test_clean_up_RemoveExcessPoints(self):
        self.assertEqual(cleanUp('with desktop publishing software.....'), "with desktop publishing software...")