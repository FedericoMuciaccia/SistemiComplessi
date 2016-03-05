
# coding: utf-8

# In[20]:

import pandas

from matplotlib import pyplot

get_ipython().magic(u'matplotlib inline')


# ## Esempio di dati tabulati

# In[13]:

dataframe = pandas.read_csv("../data/cell_towers_diff-2016012100.csv")
troncato = dataframe[0:10]
troncato


# In[17]:

with open('../doc/dataframe_troncato.html', 'w') as tabella:
    tabella.write(troncato.to_html(index=False))


# In[ ]:




# In[ ]:

TODO svuotare il notebook Fede e mettere qua la roba del data selection


# In[ ]:




# In[ ]:




# # Scatterplot preliminare non georeferenziato

# In[49]:

roma = pandas.read_csv("../data/Roma_towers.csv")

roma.plot(kind='scatter',
          x='lon',
          y='lat',
          marker='.',
          color='#3333ff',
          label='Roma towers',
          #xlim=(12.34, 12.64),
          #ylim=(41.74,42.04),
          figsize=(10,10))

# pyplot.show()

# TODO mettere il grafico quadrato e con le scale uguali
# e con le coordinate del colosseo al centro

# TODO mettere output del comando in SVG
# TODO mettere interattività, magari utilizzando Bokeh o mpld3

# vedere
# http://stackoverflow.com/questions/24525111/how-can-i-get-the-output-of-a-matplotlib-plot-as-an-svg
# https://nickcharlton.net/posts/outputting-matplotlib-plots.html

pyplot.xlabel('Longitudine')
pyplot.ylabel('Latitudine')
pyplot.legend(loc='best', frameon=False)
pyplot.savefig('../img/map/Roma_non_georeferenziata.svg', format='svg', dpi=600, transparent=True)


# In[ ]:




# In[ ]:



