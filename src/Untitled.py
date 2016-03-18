
# coding: utf-8

# In[1]:

import pandas
import seaborn
from matplotlib import pyplot
get_ipython().magic(u'matplotlib inline')


# ## Faccio i grafici

# In[ ]:

#Attack
import seaborn
get_ipython().magic(u'matplotlib inline')
datiFinal = pandas.read_csv('/home/protoss/Documenti/SistemiComplessi/data/Iuri/GtoolAttackDataForSeaborn.csv')

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")

#diametro
seaborn.lmplot('percent', 'diameter', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
           #legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0, 80)
#pyplot.legend()
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackD_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackD_Final.svg', format='svg', dpi=1000)

#giant cluster
seaborn.lmplot('percent', 'GCsize', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
           #legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
#pyplot.legend()
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackGC_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackGC_Final.svg', format='svg', dpi=1000)

#average length
seaborn.lmplot('percent', 'average path length', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
           #legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: average path length')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,30)
#pyplot.legend()
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackl_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackl_Final.svg', format='svg', dpi=1000)

#clustering
seaborn.lmplot('percent', 'clustering', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
           #legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: coefficiente clustering')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
#pyplot.legend()
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackC_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackC_Final.svg', format='svg', dpi=1000)

#gradomedio
seaborn.lmplot('percent', 'average degree', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
           #legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: average degree')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,250)
#pyplot.legend()
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackk_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackk_Final.svg', format='svg', dpi=1000)

#CRITERION
seaborn.lmplot('percent', 'soglia percolativa', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
           #legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Attack: criterion')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,10)
#pyplot.legend()
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackc_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolAttackc_Final.svg', format='svg', dpi=1000)


# In[ ]:

#Failure
import seaborn
get_ipython().magic(u'matplotlib inline')
datiFinal = pandas.read_csv('/home/protoss/Documenti/SistemiComplessi/data/Iuri/GtoolFailureDataForSeaborn.csv')

seaborn.set_context("notebook", font_scale=1.1)
seaborn.set_style("ticks")

#diametro
seaborn.lmplot('percent', 'diameter', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
#           legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: diametro')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0, 15)
#pyplot.legend(loc = 2)
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailureD_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailureD_Final.svg', format='svg', dpi=1000)

#giant cluster
seaborn.lmplot('percent', 'GCsize', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
#           legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: dimensioni relative del GC')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
#pyplot.legend(loc = 3)
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailureGC_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailureGC_Final.svg', format='svg', dpi=1000)

#average length
seaborn.lmplot('percent', 'average path length', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
#           legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: average path length')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,3)
#pyplot.legend(loc = 3)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailurel_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailurel_Final.svg', format='svg', dpi=1000)

#clustering
seaborn.lmplot('percent', 'clustering', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
#           legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: coefficiente clustering')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,1.1)
#pyplot.legend(loc = 3)
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailureC_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailureC_Final.svg', format='svg', dpi=1000)

#gradomedio
seaborn.lmplot('percent', 'average degree', data=datiFinal, fit_reg=False,
           size = 9, aspect = 1.3333,
#           legend = False,
           hue='Provider', palette = colori,
           scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: average degree')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
#pyplot.ylim(0,100)
#pyplot.legend()
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailurek_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailurek_Final.svg', format='svg', dpi=1000)

#CRITERION
seaborn.lmplot('percent', 'soglia percolativa', data=datiFinal, fit_reg=False,
                size = 9, aspect = 1.3333,
#                legend = False,
                hue='Provider', palette = colori,
                scatter_kws={"marker": "D", "s": 100})
pyplot.title('Random failure: criterion')
pyplot.xlabel("%")
pyplot.ylabel("Valore")
pyplot.xlim(0, 100)
pyplot.ylim(0,100)
#pyplot.legend(loc = 2)
#pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailurec_Final.eps', format='eps', dpi=1000)
pyplot.savefig('/home/protoss/Documenti/SistemiComplessi/img/gToolFailurec_Final.svg', format='svg', dpi=1000)

