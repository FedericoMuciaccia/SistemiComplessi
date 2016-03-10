
# coding: utf-8

# In[37]:

import pandas

from matplotlib import pyplot

get_ipython().magic(u'matplotlib inline')


# ## Esempio di dati tabulati

# In[38]:

# esempio di tabella da inserire in HTML nella relazione


# In[39]:

esempio = pandas.read_csv("../data/cell_towers_diff-2016012100.csv")
esempio[0:10]


# In[40]:

with open('../doc/diff_troncato.html', 'w') as tabella:
    tabella.write(esempio[0:10].to_html(index=False))


# In[ ]:




# In[41]:

# TODO svuotare il notebook Fede e mettere qua la roba del data selection


# In[ ]:




# In[ ]:




# # Scatterplot preliminare non georeferenziato

# In[43]:

roma = pandas.read_csv("../data/Roma_towers.csv")

roma.plot(kind='scatter',
          x='lon',
          y='lat',
          marker='.',
          color='#3333ff',
          label='Roma towers',
          #xlim=(12.34, 12.64),
          #ylim=(41.74,42.04),
          xlim=(12.30, 12.70),
          ylim=(41.75,42.05),
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


# In[44]:

roma[0:10]


# In[45]:

with open('../doc/roma_troncato.html', 'w') as tabella:
    tabella.write(roma[0:10].to_html(index=False))


# In[36]:

# TODO i file html vanno puliti un po' a mano e va aggiunto il riferimento al foglio di stile CSS appropriato per le tabelle


# In[ ]:



