
from IPython.core.display import HTML
styles = open("./styles/custom.css", "r").read()
HTML(styles)

from IPython.core.display import HTML
import urllib2
HTML(urllib2.urlopen("http://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/styles/custom.css").read())

from IPython.display import HTML
table = "<table><tr><th>bar</th><th>bar</th></tr><tr><td>foo</td><td>foo</td></tr></table>"
HTML(table)

from IPython.core.display import HTML
import urllib2
HTML(urllib2.urlopen('http://bit.ly/1Bf5Hft').read())

# http://nbviewer.jupyter.org/
# This web site does not host notebooks, it only renders notebooks available on other websites. 







