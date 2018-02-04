import proj1_w18

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m1.year, "No Year")
        self.assertEqual(m2.year, "No Year")
        self.assertEqual(len(m1), 0)
        self.assertEqual(len(m2), 0)

        s1 = proj1.Song()
        s2 = proj1.Song("Demons", "Kai Wachi", "2016", "Demons", "EDM", 251000)

        self.assertEqual(s1.title, "No Title")
        self.assertEqual(s2.title, "Demons")
        self.assertEqual(s1.author, "No Author")
        self.assertEqual(s2.author, "Kai Wachi")
        self.assertEqual(s1.release_year, "No Year")
        self.assertEqual(s2.release_year, "2016")
        self.assertEqual(s1.album, "No Album")
        self.assertEqual(s2.album, "Demons")

        mo1 = proj1.Movie()
        mo2 = proj1.Movie("Cars 3", "Brian Fee", "2017", "6.8", 6120000)

        self.assertEqual(mo1.title, "No Title")
        self.assertEqual(mo2.title, "Cars 3")
        self.assertEqual(mo1.author, "No Author")
        self.assertEqual(mo2.author, "Brian Fee")
        self.assertEqual(mo1.year, "No Release Year")
        self.assertEqual(mo2.year, "2017")
        self.assertEqual(mo1.rating, "No Rating")
        self.assertEqual(mo2.rating, "6.8")

        pass

    def testString(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Demons", "Kai Wachi", "2016", "Demons", "EDM", 251000)

        self.assertEqual(s1, "No Title by No Author(No Year)[No Genre]")
        self.assertEqual(s2, "Demons by Kai Wachi(2016)[EDM]")

        mo1 = proj1.Movie()
        mo2 = proj1.Movie("Cars 3", "Brian Fee", "2017", "6.8", 6120000)

        self.assertEqual(mo1, "No Title by No Author(No Release Year)[No Rating]")
        self.assertEqual(mo2, "Cars 3 by Brian Fee(2017)[6.8]")

        pass

    def testLength(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Demons", "Kai Wachi", "2016", "Demons", "EDM", 251000)

        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 251)

        mo1 = proj1.Movie()
        mo2 = proj1.Movie("Cars 3", "Brian Fee", "2017", "6.8", 6120000)

        self.assertEqual(mo1.length, 0)
        self.assertEqual(mo2.length, 102)

        pass

    def testRandom(self):

        pass


unittest.main()
